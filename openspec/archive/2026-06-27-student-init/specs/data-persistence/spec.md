## ADDED Requirements

### Requirement: 数据库初始化
系统首次使用时 SHALL 自动创建 SQLite 数据库及相关表结构，无需手动干预。

#### Scenario: 首次运行自动创建数据库
- **WHEN** 系统首次执行任意需要数据库的命令
- **THEN** 自动创建 data/students.db 文件及 students 表

#### Scenario: 已存在数据库不覆盖
- **WHEN** 数据库已存在且有数据
- **THEN** 系统复用现有数据库，不覆盖已有数据

### Requirement: 学生数据表结构
数据库 SHALL 包含 students 表，字段定义如下：
- student_id: TEXT PRIMARY KEY（学号，唯一标识）
- name: TEXT NOT NULL（姓名）
- chinese: REAL NOT NULL（语文成绩）
- math: REAL NOT NULL（数学成绩）
- english: REAL NOT NULL（英语成绩）
- created_at: TIMESTAMP DEFAULT CURRENT_TIMESTAMP（创建时间）

#### Scenario: 建表语句包含所有字段
- **WHEN** 执行数据库初始化
- **THEN** students 表包含上述全部字段及约束

### Requirement: 数据持久化
所有写入数据 SHALL 立即写入 SQLite 文件，程序重启后数据完整可读。

#### Scenario: 数据写入后重启可读
- **WHEN** 录入一条学生记录后关闭程序，重新启动并查询
- **THEN** 已录入的学生数据仍然存在且完整

#### Scenario: 数据库文件路径可配置
- **WHEN** 设置环境变量 DB_PATH
- **THEN** 数据库文件创建在 DB_PATH 指定的路径