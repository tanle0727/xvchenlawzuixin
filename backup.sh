#!/bin/bash
# 律师介绍系统 — SQLite 数据库自动备份脚本
# 用法: bash backup.sh
# 建议加入 crontab 每日执行: 0 2 * * * cd /项目路径 && bash backup.sh >> logs/backup.log 2>&1

set -euo pipefail

# 项目根目录（脚本所在目录）
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
DB_FILE="$PROJECT_DIR/db.sqlite3"
BACKUP_DIR="$PROJECT_DIR/backups"
LOG_FILE="$PROJECT_DIR/logs/backup.log"
KEEP_DAYS=30  # 保留最近30天的备份

# 检查数据库文件
if [ ! -f "$DB_FILE" ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ❌ 数据库文件不存在: $DB_FILE" | tee -a "$LOG_FILE"
    exit 1
fi

# 创建备份目录
mkdir -p "$BACKUP_DIR"

# 生成带时间戳的备份文件名
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
BACKUP_FILE="$BACKUP_DIR/db_${TIMESTAMP}.sqlite3"

# 使用 sqlite3 .backup 命令进行安全备份（避免复制过程中数据库被写入导致损坏）
if command -v sqlite3 &> /dev/null; then
    sqlite3 "$DB_FILE" ".backup '$BACKUP_FILE'"
else
    # 如果没有 sqlite3 命令，退化为 cp（开发环境可用，生产环境建议安装 sqlite3）
    cp "$DB_FILE" "$BACKUP_FILE"
fi

# 验证备份文件
if [ -f "$BACKUP_FILE" ] && [ -s "$BACKUP_FILE" ]; then
    SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ 备份成功: $BACKUP_FILE ($SIZE)" | tee -a "$LOG_FILE"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ❌ 备份失败: 文件为空或不存在" | tee -a "$LOG_FILE"
    exit 1
fi

# 清理过期备份
DELETED=$(find "$BACKUP_DIR" -name "db_*.sqlite3" -mtime +$KEEP_DAYS -delete -print | wc -l)
if [ "$DELETED" -gt 0 ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 🗑️  清理了 $DELETED 个超过 ${KEEP_DAYS} 天的旧备份" | tee -a "$LOG_FILE"
fi

# 显示当前备份数量
TOTAL=$(ls -1 "$BACKUP_DIR"/db_*.sqlite3 2>/dev/null | wc -l)
echo "[$(date '+%Y-%m-%d %H:%M:%S')] 📦 当前共有 $TOTAL 个备份" | tee -a "$LOG_FILE"
