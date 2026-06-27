## Why

教务人员需要一个命令行工具录入学生信息及三科成绩。在已完成的持久化层基础上，实现成绩录入 CLI 命令和完整的数据校验逻辑。

## What Changes

- 实现 CLI add 子命令：`python -m src.main add --id 001 --name "张三" --chinese 90 --math 85 --english 88`
- 实现数据校验：学号非空唯一、姓名非空、成绩 0-100 有效数字
- 重复学号自动拦截，避免数据重复录入

## Capabilities

### New Capabilities
- `student-add`: 学生成绩录入、数据校验、重复拦截

### Modified Capabilities

无。

## Impact

- 新增文件：src/services.py, src/cli.py
- 修改文件：src/main.py（新增 add 子命令）
- 依赖 student-init 的 database.py、models.py、repository.py