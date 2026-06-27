## Context

在完整的录入和查询能力基础上，增加成绩统计和全局容错。新增 stats 子命令，复用 repository 的查询方法做聚合计算。

## Goals / Non-Goals

**Goals:**
- 个人总分和平均分计算
- 班级单科平均分统计
- 全局异常容错（非法输入、空数据、异常参数）

**Non-Goals:**
- 不涉及图表/可视化
- 不涉及成绩修改/删除
- 不涉及排名

## Decisions

### 1. 统计实现
```
cli.py (stats) → services.py (统计计算) → repository.py (查询/聚合 SQL)
```
- 个人统计：从 repository 取单条记录，Python 层做数学计算
- 班级统计：使用 SQL AVG() 聚合函数，减少数据传输

### 2. 全局容错策略
- main.py 添加全局异常捕获（try-except 兜底）
- argparse 参数类型校验由标准库处理
- 空数据在 services 层返回友好提示，不抛异常

## Risks / Trade-offs

| 风险 | 缓解措施 |
|------|---------|
| 浮点数精度 | 使用 round() 保留 2 位小数 |
| 非法参数穿透到 SQL | 所有用户输入经过 models 校验后再传递给 repository |