"""数据访问层，封装 SQLite CRUD 操作。"""

import sqlite3

from src.database import get_connection


def add_student(
    db_path: str, student_id: str, name: str, chinese: float, math: float, english: float
) -> tuple[bool, str]:
    """新增学生记录，返回 (success, message)。"""
    conn = get_connection(db_path)
    try:
        conn.execute(
            'INSERT INTO students (student_id, name, chinese, math, english) VALUES (?, ?, ?, ?, ?)',
            (student_id, name, chinese, math, english),
        )
        conn.commit()
        return True, f'学生 {student_id} 录入成功'
    except sqlite3.IntegrityError:
        return False, f'学号 {student_id} 已存在'
    finally:
        conn.close()


def get_by_id(db_path: str, student_id: str) -> dict | None:
    """按学号查询学生，返回 dict 或 None。"""
    conn = get_connection(db_path)
    try:
        row = conn.execute(
            'SELECT student_id, name, chinese, math, english, created_at FROM students WHERE student_id = ?',
            (student_id,),
        ).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def get_all(db_path: str) -> list[dict]:
    """查询全部学生列表。"""
    conn = get_connection(db_path)
    try:
        rows = conn.execute(
            'SELECT student_id, name, chinese, math, english, created_at FROM students ORDER BY student_id'
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()