"""业务逻辑层，负责录入、查询、统计等核心业务。"""

from src.models import validate_student
from src.repository import add_student as repo_add
from src.repository import get_all, get_by_id


def add_student(
    db_path: str, student_id: str, name: str, chinese: float, math: float, english: float
) -> tuple[bool, str]:
    """录入学生：校验 → 去重 → 写入，返回 (success, message)。"""
    errors = validate_student(student_id, name, chinese, math, english)
    if errors:
        return False, '; '.join(errors)

    existing = get_by_id(db_path, student_id)
    if existing:
        return False, f'学号 {student_id} 已存在'

    return repo_add(db_path, student_id, name, chinese, math, english)


def query_student(db_path: str, student_id: str) -> tuple[bool, dict | str]:
    """按学号查询学生，返回 (success, data_or_message)。"""
    student = get_by_id(db_path, student_id)
    if student is None:
        return False, f'学号 {student_id} 不存在'
    return True, student


def list_students(db_path: str) -> tuple[bool, list[dict] | str]:
    """查询全部学生列表，返回 (success, data_or_message)。"""
    students = get_all(db_path)
    if not students:
        return False, '暂无学生数据'
    return True, students


def calc_student_stats(db_path: str, student_id: str) -> tuple[bool, dict | str]:
    """计算个人总分和平均分，返回 (success, data_or_message)。"""
    student = get_by_id(db_path, student_id)
    if student is None:
        return False, f'学号 {student_id} 不存在'
    total = student['chinese'] + student['math'] + student['english']
    average = round(total / 3, 2)
    return True, {'total': total, 'average': average}


def calc_class_stats(db_path: str) -> tuple[bool, dict | str]:
    """计算班级单科平均分，返回 (success, data_or_message)。"""
    from src.repository import get_all
    students = get_all(db_path)
    if not students:
        return False, '暂无学生数据'
    n = len(students)
    chinese_avg = round(sum(s['chinese'] for s in students) / n, 2)
    math_avg = round(sum(s['math'] for s in students) / n, 2)
    english_avg = round(sum(s['english'] for s in students) / n, 2)
    return True, {'chinese_avg': chinese_avg, 'math_avg': math_avg, 'english_avg': english_avg}