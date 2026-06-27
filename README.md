# 学生成绩管理系统

面向教务人员的轻量级 CLI 成绩管理工具，基于 Python + SQLite，支持成绩录入、查询、统计全流程。

## 快速开始

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest

# 初始化数据库
python3 -m src.main init

# 录入学生成绩
python3 -m src.main add --id 001 --name "张三" --chinese 90 --math 85 --english 88

# 查询单个学生
python3 -m src.main query --id 001

# 列出全部学生
python3 -m src.main list

# 成绩统计（个人）
python3 -m src.main stats --id 001

# 成绩统计（全班）
python3 -m src.main stats
```

## CLI 命令

| 命令 | 参数 | 说明 |
|------|------|------|
| `init` | - | 初始化数据库 |
| `add` | `--id --name --chinese --math --english` | 录入学生成绩 |
| `query` | `--id` | 按学号查询 |
| `list` | - | 列出全部学生 |
| `stats` | `--id` (可选) | 个人/班级成绩统计 |

## 项目结构

```
├── src/
│   ├── database.py    # SQLite 连接与初始化
│   ├── models.py      # 数据模型与校验
│   ├── repository.py  # 数据访问层（CRUD）
│   ├── services.py    # 业务逻辑层
│   └── main.py        # CLI 入口
├── tests/             # 测试（pytest）
├── data/              # SQLite 数据库文件
└── pyproject.toml
```

## 数据校验

- 学号：非空、唯一
- 姓名：非空
- 成绩：0-100 有效数字

## 开发

```bash
# 运行全部测试
python3 -m pytest

# 配置数据库路径（默认 data/students.db）
export DB_PATH=/path/to/students.db
```

## 技术栈

- Python 3.10+
- SQLite（内置）
- argparse（CLI 解析）
- pytest（测试）