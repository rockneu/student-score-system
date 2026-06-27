## 1. 项目初始化与配置

- [x] 1.1 创建项目目录结构（src/、tests/、data/）
- [x] 1.2 创建 pyproject.toml 和 pytest.ini 配置文件
- [x] 1.3 创建 src/__init__.py 和 tests/__init__.py
- [x] 1.4 创建 .gitignore

## 2. 数据库层（database.py）

- [x] 2.1 编写 test_database.py：验证数据库初始化、建表、连接、环境变量配置
- [x] 2.2 实现 database.py：get_connection()、init_db()、自动建 students 表

## 3. 数据模型层（models.py）

- [x] 3.1 编写 test_models.py：验证学号、姓名、成绩的校验规则
- [x] 3.2 实现 models.py：validate_student() 函数，校验学号非空唯一、姓名非空、成绩 0-100

## 4. 数据访问层（repository.py）

- [x] 4.1 编写 test_repository.py：验证 add_student、get_by_id、get_all
- [x] 4.2 实现 repository.py：insert、select_by_id、select_all

## 5. CLI 入口骨架（main.py）

- [x] 5.1 编写 test_main.py：验证 init 命令执行和子命令路由
- [x] 5.2 实现 main.py：argparse 子命令骨架，init 命令可运行
- [x] 5.3 运行全部测试，确保 v1 通过