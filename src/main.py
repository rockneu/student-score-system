"""CLI 入口模块。"""

import argparse
import sys

from src.database import init_db, get_db_path
from src.services import add_student as svc_add
from src.services import calc_class_stats, calc_student_stats, list_students, query_student


def main(argv: list[str] | None = None) -> None:
    """CLI 主入口，路由到各子命令。"""
    parser = argparse.ArgumentParser(description='学生成绩管理系统')
    sub = parser.add_subparsers(dest='command', title='子命令')

    # init 命令
    sub.add_parser('init', help='初始化数据库')

    # add 命令
    add_parser = sub.add_parser('add', help='录入学生成绩')
    add_parser.add_argument('--id', required=True, help='学号')
    add_parser.add_argument('--name', required=True, help='姓名')
    add_parser.add_argument('--chinese', required=True, type=float, help='语文成绩')
    add_parser.add_argument('--math', required=True, type=float, help='数学成绩')
    add_parser.add_argument('--english', required=True, type=float, help='英语成绩')

    # query 命令
    query_parser = sub.add_parser('query', help='按学号查询学生')
    query_parser.add_argument('--id', required=True, help='学号')

    # list 命令
    sub.add_parser('list', help='列出全部学生')

    # stats 命令
    stats_parser = sub.add_parser('stats', help='成绩统计')
    stats_parser.add_argument('--id', help='学号（不指定则统计全班）')

    try:
        args = parser.parse_args(argv)
    except SystemExit:
        sys.exit(1)

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    if args.command == 'init':
        init_db()
        print('数据库初始化成功')

    elif args.command == 'add':
        success, msg = svc_add(get_db_path(), args.id, args.name, args.chinese, args.math, args.english)
        print(msg)

    elif args.command == 'query':
        success, data = query_student(get_db_path(), args.id)
        if success:
            s = data
            print(f'学号: {s["student_id"]}  姓名: {s["name"]}')
            print(f'语文: {s["chinese"]}  数学: {s["math"]}  英语: {s["english"]}')
            print(f'创建时间: {s["created_at"]}')
        else:
            print(data)

    elif args.command == 'list':
        success, data = list_students(get_db_path())
        if success:
            for s in data:
                print(f'{s["student_id"]}  {s["name"]}  语文:{s["chinese"]}  数学:{s["math"]}  英语:{s["english"]}')
        else:
            print(data)

    elif args.command == 'stats':
        if args.id:
            success, data = calc_student_stats(get_db_path(), args.id)
            if success:
                print(f'学号 {args.id} 总分: {data["total"]}  平均分: {data["average"]}')
            else:
                print(data)
        else:
            success, data = calc_class_stats(get_db_path())
            if success:
                print(f'班级统计 - 语文平均: {data["chinese_avg"]}  数学平均: {data["math_avg"]}  英语平均: {data["english_avg"]}')
            else:
                print(data)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()