## 1. 统计业务逻辑（services.py）

- [x] 1.1 编写 test_services.py：验证 calc_student_stats（存在/不存在）和 calc_class_stats（有数据/空数据）
- [x] 1.2 实现 services.py calc_student_stats()：个人总分、平均分
- [x] 1.3 实现 services.py calc_class_stats()：班级单科平均分（SQL AVG 聚合）

## 2. CLI 统计命令（cli.py + main.py）

- [x] 2.1 编写 test_cli.py：验证 stats 命令（--id 可选参数）
- [x] 2.2 实现 cli.py stats 子命令
- [x] 2.3 集成 main.py stats 命令

## 3. 全局容错

- [x] 3.1 main.py 添加全局异常捕获兜底
- [x] 3.2 验证空数据、非法参数等场景的友好提示
- [x] 3.3 运行全部测试，确保 v4 通过