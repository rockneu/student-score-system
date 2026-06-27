## Context

在学生成绩管理系统的持久化层基础上，实现成绩录入功能。新增 services 层处理录入业务逻辑，新增 cli 层通过 argparse 解析 add 子命令。

## Goals / Non-Goals

**Goals:**
- 实现 CLI add 子命令
- 完整的数据校验（学号/姓名非空、学号唯一、成绩 0-100）
- 重复学号拦截
- 录入成功/失败的友好输出

**Non-Goals:**
- 不涉及查询功能（交由 student-query）
- 不涉及统计功能（交由 student-stats）

## Decisions

### 1. 职责分层
```
cli.py (参数解析) → services.py (业务校验+调用) → repository.py (数据写入)
models.py (数据校验) → services.py (调用)
```
- cli 层只负责参数解析和结果展示
- services 层负责业务逻辑组合（校验 → 去重 → 写入）

### 2. 错误处理
- models.validate_student() 返回错误列表（支持多条错误同时展示）
- services.add_student() 返回 (success, data_or_error)

## Risks / Trade-offs

| 风险 | 缓解措施 |
|------|---------|
| 参数类型错误（argparse 自动转 float） | argparse 的 type=float 自动处理，捕获 ValueError |
| 成绩精度问题 | 使用 REAL 类型，显示时保留 1 位小数 |