"""Tests for models module."""

import pytest


class TestValidateStudent:
    """数据校验测试。"""

    def test_valid_student(self):
        """录入完整有效学生信息。"""
        from src.models import validate_student
        errors = validate_student('001', '张三', 90, 85, 88)
        assert errors == []

    def test_student_id_empty(self):
        """学号为空拒绝录入。"""
        from src.models import validate_student
        errors = validate_student('', '张三', 90, 85, 88)
        assert '学号不能为空' in errors

    def test_name_empty(self):
        """姓名为空拒绝录入。"""
        from src.models import validate_student
        errors = validate_student('001', '', 90, 85, 88)
        assert '姓名不能为空' in errors

    def test_score_negative(self):
        """成绩为负数拒绝录入。"""
        from src.models import validate_student
        errors = validate_student('001', '张三', -1, 85, 88)
        assert any('成绩' in e for e in errors)

    def test_score_over_100(self):
        """成绩大于100拒绝录入。"""
        from src.models import validate_student
        errors = validate_student('001', '张三', 90, 101, 88)
        assert any('成绩' in e for e in errors)

    def test_score_boundary_zero(self):
        """成绩为边界值正常录入。"""
        from src.models import validate_student
        errors = validate_student('001', '张三', 0, 85, 88)
        assert errors == []

    def test_score_boundary_100(self):
        """成绩为边界值100正常录入。"""
        from src.models import validate_student
        errors = validate_student('001', '张三', 90, 85, 100)
        assert errors == []

    def test_score_not_number(self):
        """成绩为非数字拒绝录入（类型错误）。"""
        from src.models import validate_student
        errors = validate_student('001', '张三', 'abc', 85, 88)
        assert any('成绩' in e and '数字' in e for e in errors)

    def test_all_empty(self):
        """全部为空返回多条错误。"""
        from src.models import validate_student
        errors = validate_student('', '', -1, 101, 200)
        assert len(errors) >= 2