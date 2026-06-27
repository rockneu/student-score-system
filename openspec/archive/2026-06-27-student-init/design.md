## Context

学生成绩管理系统的基础层，负责项目初始化、SQLite 持久化、数据模型和基础 CRUD。使用 Python 3.10+ 标准库（sqlite3, argparse），零外部依赖。

## Goals / Non-Goals

**Goals:**
- 搭建完整项目目录结构
- SQLite 数据库自动初始化和连接管理
- 学生数据模型定义及校验
- 基础数据存取操作（增/查）
- CLI 入口骨架（init 命令可用）

**Non-Goals:**
- 不涉及录入交互逻辑（交由 student-add）
- 不涉及复杂查询（交由 student-query）
- 不涉及统计（交由 student-stats）

## Decisions

### 1. 技术栈：Python 3.10+ + SQLite + argparse
Python 标准库内置，零外部依赖。

### 2. 架构分层
```
main.py (入口) → repository.py (数据访问) → database.py (SQLite)
models.py (数据模型与校验) ← repository.py
```

### 3. 测试策略
- 使用 pytest + tmp_path fixture 创建临时数据库
- conftest.py 提供共享 fixture（db_path, db_connection）
- TDD：先写测试，再写实现

## Risks / Trade-offs

| 风险 | 缓解措施 |
|------|---------|
| SQLite 文件路径硬编码 | 默认 data/students.db，支持 DB_PATH 环境变量 |
| 建表变更导致数据不兼容 | v1 阶段无存量数据，后续版本用 migration 脚本 |