## 1. 业务逻辑层（services.py）

- [x] 1.1 编写 test_services.py：验证 add_student 的完整录入流程（校验 + 去重 + 写入）
- [x] 1.2 实现 services.py add_student()：调用 models 校验，校验通过则调用 repository 写入

## 2. CLI 录入命令（cli.py + main.py）

- [x] 2.1 编写 test_cli.py：验证 add 命令参数解析和错误输入处理
- [x] 2.2 实现 cli.py add 子命令：解析 --id/--name/--chinese/--math/--english 参数
- [x] 2.3 集成 main.py add 命令：完整录入流程
- [x] 2.4 运行全部测试，确保 v2 通过