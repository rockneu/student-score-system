"""Tests for CLI module."""

from pathlib import Path

import pytest


class TestAddCommand:
    """add 命令测试。"""

    def test_add_success(self, tmp_path: Path, capsys, monkeypatch):
        """add 命令成功录入学生。"""
        db_path = str(tmp_path / 'test.db')
        monkeypatch.setenv('DB_PATH', db_path)
        from src.database import init_db
        from src.main import main
        init_db(db_path)
        main(['add', '--id', '001', '--name', '张三', '--chinese', '90', '--math', '85', '--english', '88'])
        captured = capsys.readouterr()
        assert '成功' in captured.out

    def test_add_duplicate(self, tmp_path: Path, capsys, monkeypatch):
        """add 命令重复学号拦截。"""
        db_path = str(tmp_path / 'test.db')
        monkeypatch.setenv('DB_PATH', db_path)
        from src.database import init_db
        from src.main import main
        init_db(db_path)
        main(['add', '--id', '001', '--name', '张三', '--chinese', '90', '--math', '85', '--english', '88'])
        main(['add', '--id', '001', '--name', '李四', '--chinese', '80', '--math', '80', '--english', '80'])
        captured = capsys.readouterr()
        assert '已存在' in captured.out

    def test_add_validation_error(self, tmp_path: Path, capsys, monkeypatch):
        """add 命令校验错误提示。"""
        db_path = str(tmp_path / 'test.db')
        monkeypatch.setenv('DB_PATH', db_path)
        from src.database import init_db
        from src.main import main
        init_db(db_path)
        with pytest.raises(SystemExit):
            main(['add', '--id', '', '--name', '', '--chinese', '-1', '--math', '101', '--english', 'abc'])


class TestQueryCommand:
    """query 命令测试。"""

    def test_query_exists(self, tmp_path: Path, capsys, monkeypatch):
        """query 命令查询已存在学生。"""
        db_path = str(tmp_path / 'test.db')
        monkeypatch.setenv('DB_PATH', db_path)
        from src.database import init_db
        from src.main import main
        init_db(db_path)
        main(['add', '--id', '001', '--name', '张三', '--chinese', '90', '--math', '85', '--english', '88'])
        main(['query', '--id', '001'])
        captured = capsys.readouterr()
        assert '001' in captured.out
        assert '张三' in captured.out

    def test_query_not_exists(self, tmp_path: Path, capsys, monkeypatch):
        """query 命令查询不存在学生。"""
        db_path = str(tmp_path / 'test.db')
        monkeypatch.setenv('DB_PATH', db_path)
        from src.database import init_db
        from src.main import main
        init_db(db_path)
        main(['query', '--id', '999'])
        captured = capsys.readouterr()
        assert '不存在' in captured.out


class TestListCommand:
    """list 命令测试。"""

    def test_list_with_data(self, tmp_path: Path, capsys, monkeypatch):
        """list 命令有数据时展示。"""
        db_path = str(tmp_path / 'test.db')
        monkeypatch.setenv('DB_PATH', db_path)
        from src.database import init_db
        from src.main import main
        init_db(db_path)
        main(['add', '--id', '001', '--name', '张三', '--chinese', '90', '--math', '85', '--english', '88'])
        main(['add', '--id', '002', '--name', '李四', '--chinese', '80', '--math', '75', '--english', '82'])
        main(['list'])
        captured = capsys.readouterr()
        assert '001' in captured.out
        assert '002' in captured.out

    def test_list_empty(self, tmp_path: Path, capsys, monkeypatch):
        """list 命令无数据时提示。"""
        db_path = str(tmp_path / 'test.db')
        monkeypatch.setenv('DB_PATH', db_path)
        from src.database import init_db
        from src.main import main
        init_db(db_path)
        main(['list'])
        captured = capsys.readouterr()
        assert '暂无' in captured.out


class TestStatsCommand:
    """stats 命令测试。"""

    def test_stats_student(self, tmp_path: Path, capsys, monkeypatch):
        """stats 命令查询个人统计。"""
        db_path = str(tmp_path / 'test.db')
        monkeypatch.setenv('DB_PATH', db_path)
        from src.database import init_db
        from src.main import main
        init_db(db_path)
        main(['add', '--id', '001', '--name', '张三', '--chinese', '90', '--math', '85', '--english', '88'])
        main(['stats', '--id', '001'])
        captured = capsys.readouterr()
        assert '263' in captured.out  # 总分

    def test_stats_class(self, tmp_path: Path, capsys, monkeypatch):
        """stats 命令查询全班统计。"""
        db_path = str(tmp_path / 'test.db')
        monkeypatch.setenv('DB_PATH', db_path)
        from src.database import init_db
        from src.main import main
        init_db(db_path)
        main(['add', '--id', '001', '--name', '张三', '--chinese', '90', '--math', '80', '--english', '70'])
        main(['add', '--id', '002', '--name', '李四', '--chinese', '80', '--math', '70', '--english', '60'])
        main(['stats'])
        captured = capsys.readouterr()
        assert '85' in captured.out  # 语文平均
        assert '75' in captured.out  # 数学平均

    def test_stats_empty(self, tmp_path: Path, capsys, monkeypatch):
        """stats 命令空数据提示。"""
        db_path = str(tmp_path / 'test.db')
        monkeypatch.setenv('DB_PATH', db_path)
        from src.database import init_db
        from src.main import main
        init_db(db_path)
        main(['stats'])
        captured = capsys.readouterr()
        assert '暂无' in captured.out