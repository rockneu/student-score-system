"""数据模型与校验模块。"""


def validate_student(
    student_id: str, name: str, chinese: float, math: float, english: float
) -> list[str]:
    """校验学生信息，返回错误列表（空列表表示校验通过）。"""
    errors: list[str] = []

    if not student_id:
        errors.append('学号不能为空')

    if not name:
        errors.append('姓名不能为空')

    for label, score in [('语文', chinese), ('数学', math), ('英语', english)]:
        if not isinstance(score, (int, float)):
            errors.append(f'{label}成绩必须是有效数字')
            continue
        score_val = float(score)
        if score_val < 0 or score_val > 100:
            errors.append(f'{label}成绩必须在0-100之间')

    return errors