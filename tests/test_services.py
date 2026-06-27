"""Tests for services module."""

from pathlib import Path

import pytest


class TestAddStudent:
    """录入学生测试。"""

    def test_add_student_success(self, tmp_path: Path):
        """录入完整有效学生信息。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import add_student
        init_db(db_path)
        success, msg = add_student(db_path, '001', '张三', 90, 85, 88)
        assert success is True
        assert '成功' in msg

    def test_add_student_id_empty(self, tmp_path: Path):
        """学号为空拒绝录入。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import add_student
        init_db(db_path)
        success, msg = add_student(db_path, '', '张三', 90, 85, 88)
        assert success is False
        assert '学号不能为空' in msg

    def test_add_student_name_empty(self, tmp_path: Path):
        """姓名为空拒绝录入。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import add_student
        init_db(db_path)
        success, msg = add_student(db_path, '001', '', 90, 85, 88)
        assert success is False
        assert '姓名不能为空' in msg

    def test_add_student_duplicate(self, tmp_path: Path):
        """学号重复拒绝录入。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import add_student
        init_db(db_path)
        add_student(db_path, '001', '张三', 90, 85, 88)
        success, msg = add_student(db_path, '001', '李四', 80, 80, 80)
        assert success is False
        assert '已存在' in msg

    def test_add_student_score_negative(self, tmp_path: Path):
        """成绩为负数拒绝录入。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import add_student
        init_db(db_path)
        success, msg = add_student(db_path, '001', '张三', -1, 85, 88)
        assert success is False
        assert '成绩' in msg

    def test_add_student_score_over_100(self, tmp_path: Path):
        """成绩大于100拒绝录入。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import add_student
        init_db(db_path)
        success, msg = add_student(db_path, '001', '张三', 90, 101, 88)
        assert success is False
        assert '成绩' in msg

    def test_add_student_score_boundary(self, tmp_path: Path):
        """成绩为边界值正常录入。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import add_student
        init_db(db_path)
        success, msg = add_student(db_path, '001', '张三', 0, 100, 88)
        assert success is True


class TestQueryStudent:
    """按学号查询测试。"""

    def test_query_exists(self, tmp_path: Path):
        """学号存在返回学生完整信息。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import add_student, query_student
        init_db(db_path)
        add_student(db_path, '001', '张三', 90, 85, 88)
        success, data = query_student(db_path, '001')
        assert success is True
        assert data['student_id'] == '001'
        assert data['name'] == '张三'
        assert data['chinese'] == 90
        assert data['math'] == 85
        assert data['english'] == 88

    def test_query_not_exists(self, tmp_path: Path):
        """学号不存在给出友好提示。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import query_student
        init_db(db_path)
        success, msg = query_student(db_path, '999')
        assert success is False
        assert '不存在' in msg


class TestListStudents:
    """全部学生列表测试。"""

    def test_list_with_data(self, tmp_path: Path):
        """数据库有数据返回全部学生。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import add_student, list_students
        init_db(db_path)
        add_student(db_path, '001', '张三', 90, 85, 88)
        add_student(db_path, '002', '李四', 80, 75, 82)
        success, data = list_students(db_path)
        assert success is True
        assert len(data) == 2

    def test_list_empty(self, tmp_path: Path):
        """数据库无数据给出友好提示。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import list_students
        init_db(db_path)
        success, msg = list_students(db_path)
        assert success is False
        assert '暂无' in msg


class TestCalcStudentStats:
    """个人成绩统计测试。"""

    def test_stats_exists(self, tmp_path: Path):
        """计算已存在学生的总分和平均分。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import add_student, calc_student_stats
        init_db(db_path)
        add_student(db_path, '001', '张三', 90, 85, 88)
        success, data = calc_student_stats(db_path, '001')
        assert success is True
        assert data['total'] == 263
        assert data['average'] == round(263 / 3, 2)

    def test_stats_not_exists(self, tmp_path: Path):
        """不存在的学号给出提示。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import calc_student_stats
        init_db(db_path)
        success, msg = calc_student_stats(db_path, '999')
        assert success is False
        assert '不存在' in msg


class TestCalcClassStats:
    """班级单科平均分测试。"""

    def test_class_stats_with_data(self, tmp_path: Path):
        """数据库有学生计算各科平均分。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import add_student, calc_class_stats
        init_db(db_path)
        add_student(db_path, '001', '张三', 90, 80, 70)
        add_student(db_path, '002', '李四', 80, 70, 60)
        success, data = calc_class_stats(db_path)
        assert success is True
        assert data['chinese_avg'] == 85
        assert data['math_avg'] == 75
        assert data['english_avg'] == 65

    def test_class_stats_empty(self, tmp_path: Path):
        """数据库无学生给出提示。"""
        db_path = str(tmp_path / 'test.db')
        from src.database import init_db
        from src.services import calc_class_stats
        init_db(db_path)
        success, msg = calc_class_stats(db_path)
        assert success is False
        assert '暂无' in msg