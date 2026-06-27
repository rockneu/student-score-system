"""Tests for repository module."""

from pathlib import Path

import pytest


class TestAddStudent:
    """新增学生测试。"""

    def test_add_student_success(self, tmp_path: Path):
        """成功新增一条学生记录。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.repository import add_student
        init_db(db_path)
        success, msg = add_student(db_path, '001', '张三', 90, 85, 88)
        assert success is True
        assert '成功' in msg

    def test_add_duplicate_id(self, tmp_path: Path):
        """重复学号拒绝。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.repository import add_student
        init_db(db_path)
        add_student(db_path, '001', '张三', 90, 85, 88)
        success, msg = add_student(db_path, '001', '李四', 80, 80, 80)
        assert success is False
        assert '已存在' in msg


class TestGetById:
    """按学号查询测试。"""

    def test_get_by_id_exists(self, tmp_path: Path):
        """查询已存在的学生。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.repository import add_student, get_by_id
        init_db(db_path)
        add_student(db_path, '001', '张三', 90, 85, 88)
        student = get_by_id(db_path, '001')
        assert student is not None
        assert student['student_id'] == '001'
        assert student['name'] == '张三'
        assert student['chinese'] == 90
        assert student['math'] == 85
        assert student['english'] == 88

    def test_get_by_id_not_exists(self, tmp_path: Path):
        """查询不存在的学号返回 None。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.repository import get_by_id
        init_db(db_path)
        student = get_by_id(db_path, '999')
        assert student is None


class TestGetAll:
    """全部查询测试。"""

    def test_get_all_with_data(self, tmp_path: Path):
        """有数据时返回全部学生。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.repository import add_student, get_all
        init_db(db_path)
        add_student(db_path, '001', '张三', 90, 85, 88)
        add_student(db_path, '002', '李四', 80, 75, 82)
        students = get_all(db_path)
        assert len(students) == 2

    def test_get_all_empty(self, tmp_path: Path):
        """无数据时返回空列表。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.repository import get_all
        init_db(db_path)
        students = get_all(db_path)
        assert students == []