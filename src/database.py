"""数据库连接与初始化模块。"""

import os
import sqlite3


def get_db_path() -> str:
    """获取数据库文件路径，默认 data/students.db，可通过 DB_PATH 环境变量覆盖。"""
    return os.environ.get('DB_PATH', 'data/students.db')


def get_connection(db_path: str | None = None) -> sqlite3.Connection:
    """获取数据库连接。"""
    path = db_path or get_db_path()
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: str | None = None) -> sqlite3.Connection:
    """初始化数据库，自动建表，返回连接。"""
    path = db_path or get_db_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    conn = get_connection(path)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            chinese REAL NOT NULL,
            math REAL NOT NULL,
            english REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    return conn