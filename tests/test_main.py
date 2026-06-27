"""Tests for main CLI entry point."""

from pathlib import Path

import pytest


class TestInitCommand:
    """init 命令测试。"""

    def test_init_creates_db(self, tmp_path: Path, monkeypatch):
        """init 命令创建数据库文件。"""
        db_path = str(tmp_path / 'test.db')
        monkeypatch.setenv('DB_PATH', db_path)
        from src.main import main
        main(['init'])
        assert (tmp_path / 'test.db').exists()

    def test_init_idempotent(self, tmp_path: Path, monkeypatch):
        """init 多次执行不报错。"""
        db_path = str(tmp_path / 'test.db')
        monkeypatch.setenv('DB_PATH', db_path)
        from src.main import main
        main(['init'])
        main(['init'])  # 第二次不报错

    def test_invalid_command(self, tmp_path: Path, monkeypatch):
        """非法命令返回非零退出码。"""
        monkeypatch.setenv('DB_PATH', str(tmp_path / 'test.db'))
        from src.main import main
        with pytest.raises(SystemExit):
            main(['unknown'])