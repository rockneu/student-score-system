## Why

学生成绩管理系统需要稳定的技术底座。先完成项目规范化初始化、SQLite 持久化能力和基础架构搭建，为后续录入、查询、统计功能提供支撑。

## What Changes

- 创建 Python 项目目录结构（src/、tests/、data/）
- 配置 pyproject.toml 和 pytest.ini
- 实现 SQLite 数据库初始化与连接管理
- 实现学生数据模型与校验规则
- 实现基础 CRUD 操作（repository 层）
- 实现 CLI 入口骨架（init 命令可用）

## Capabilities

### New Capabilities
- `data-persistence`: SQLite 数据库初始化、表结构、连接管理、数据持久化

### Modified Capabilities

无。

## Impact

全新项目，无现有代码影响。
- 新增依赖：Python 3.10+, pytest
- 新增文件：src/database.py, src/models.py, src/repository.py, src/main.py
- 数据存储：data/students.db（SQLite）