## 1. 查询业务逻辑（services.py）

- [x] 1.1 编写 test_services.py：验证 query_student（存在/不存在）和 list_students（有数据/空数据）
- [x] 1.2 实现 services.py query_student()：按学号查询，不存在返回友好提示
- [x] 1.3 实现 services.py list_students()：全部列表，空数据返回友好提示

## 2. CLI 查询命令（cli.py + main.py）

- [x] 2.1 编写 test_cli.py：验证 query/list 命令参数解析和输出格式
- [x] 2.2 实现 cli.py query/list 子命令
- [x] 2.3 集成 main.py query/list 命令
- [x] 2.4 运行全部测试，确保 v3 通过