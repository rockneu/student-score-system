"""Tests for database module."""

import os
import sqlite3
from pathlib import Path

import pytest


class TestDatabaseInit:
    """数据库初始化测试。"""

    def test_init_db_creates_file(self, tmp_path: Path):
        """首次运行自动创建数据库文件。"""
        db_path = tmp_path / 'test.db'
        from src.database import init_db
        init_db(str(db_path))
        assert db_path.exists()

    def test_init_db_creates_table(self, tmp_path: Path):
        """建表语句包含所有字段。"""
        db_path = tmp_path / 'test.db'
        from src.database import init_db
        conn = init_db(str(db_path))
        cursor = conn.execute("PRAGMA table_info(students)")
        columns = {row[1]: row[2] for row in cursor.fetchall()}
        assert columns['student_id'] == 'TEXT'
        assert columns['name'] == 'TEXT'
        assert columns['chinese'] == 'REAL'
        assert columns['math'] == 'REAL'
        assert columns['english'] == 'REAL'
        assert 'created_at' in columns
        conn.close()

    def test_init_db_idempotent(self, tmp_path: Path):
        """已存在数据库不覆盖。"""
        db_path = tmp_path / 'test.db'
        from src.database import init_db
        conn1 = init_db(str(db_path))
        conn1.execute("INSERT INTO students (student_id, name, chinese, math, english) VALUES (?, ?, ?, ?, ?)",
                      ('001', 'test', 90, 85, 88))
        conn1.commit()
        conn1.close()
        conn2 = init_db(str(db_path))
        cursor = conn2.execute("SELECT COUNT(*) FROM students")
        assert cursor.fetchone()[0] == 1
        conn2.close()

    def test_get_connection(self, tmp_path: Path):
        """get_connection 返回有效连接。"""
        db_path = tmp_path / 'test.db'
        from src.database import get_connection, init_db
        init_db(str(db_path))
        conn = get_connection(str(db_path))
        assert isinstance(conn, sqlite3.Connection)
        conn.close()

    def test_db_path_from_env(self, tmp_path: Path, monkeypatch):
        """环境变量 DB_PATH 生效。"""
        db_path = tmp_path / 'env_test.db'
        monkeypatch.setenv('DB_PATH', str(db_path))
        from src.database import get_db_path
        assert get_db_path() == str(db_path)