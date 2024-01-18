import unittest
import logging
from pathlib import Path

curdir = Path(__file__).parent


class LoggerDemo(unittest.TestCase):
    def test_logging(self):
        """日志"""
        tmp_dir = curdir / ".file/tmp"
        tmp_dir.mkdir(parents=True, exist_ok=True)
        formatter = "%(asctime)s - %(levelname)s - %(message)s"
        logging.basicConfig(filename=curdir / ".file/tmp/log.log", level=logging.DEBUG, format=formatter)
        logger = logging.getLogger()
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter(formatter))
        # 如果配置的是写入到文件的,默认不会输出到控制台,因此需要添加一个StreamHandler,把日志输入到控制台
        logger.addHandler(ch)
        logger.debug("test_logging message")
