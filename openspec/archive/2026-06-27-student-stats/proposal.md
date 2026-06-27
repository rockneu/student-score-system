## Why

教务人员需要掌握班级整体的学习成绩情况，也需要关注单个学生的成绩水平。在已实现的录入和查询功能基础上，增加成绩统计能力和全局容错。

## What Changes

- 实现 stats 子命令：个人总分/平均分计算、班级单科平均分统计
- 全局容错处理：非法文字输入、空数据查询、异常参数拦截

## Capabilities

### New Capabilities
- `score-statistics`: 个人总分/平均分、班级单科平均分

### Modified Capabilities

无。

## Impact

- 修改文件：src/services.py（新增统计方法）、src/cli.py（新增 stats 命令）、src/main.py
- 依赖前三个提案完成的全部基础能力