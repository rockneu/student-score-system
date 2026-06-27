## Context

在学生成绩录入功能的基础上，实现查询能力。新增 query/list 子命令，复用已有的 repository 层查询方法。

## Goals / Non-Goals

**Goals:**
- 按学号精准查询（单个学生完整信息）
- 批量展示全部学生列表
- 异常场景友好提示（学号不存在、空列表）

**Non-Goals:**
- 不涉及模糊搜索
- 不涉及统计计算（交由 student-stats）
- 不涉及分页

## Decisions

### 1. 查询路由
```
cli.py (query/list) → services.py (查询 + 格式化) → repository.py (SQL 查询)
```
- query 调用 get_by_id()
- list 调用 get_all()
- services 层做结果后处理（格式化、空结果判断）

### 2. 输出格式
- 单条查询：逐行打印各字段
- 全部列表：表格形式，每条记录一行

## Risks / Trade-offs

| 风险 | 缓解措施 |
|------|---------|
| 大量数据时列表输出过长 | 当前使用场景（班级级）数据量不大，无需分页 |