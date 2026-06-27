## Why

教务人员需要快速查询学生成绩。在已完成的录入功能基础上，实现按学号精准查询和全部学生列表批量展示，并处理异常场景。

## What Changes

- 实现 query 子命令：按学号查询单个学生完整信息
- 实现 list 子命令：批量展示全部已录入学生
- 异常场景友好提示：学号不存在、无录入数据

## Capabilities

### New Capabilities
- `student-query`: 按学号查询、全部列表展示、异常提示

### Modified Capabilities

无。

## Impact

- 修改文件：src/services.py（新增查询方法）、src/cli.py（新增 query/list 命令）、src/main.py
- 依赖 student-add 完成的录入功能和底层持久化层