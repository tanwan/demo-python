import unittest
from pathlib import Path
import os
import csv

curdir = Path(__file__).parent
original_workdir = os.getcwd()


class CSVDemo(unittest.TestCase):
    def setUp(self) -> None:
        os.chdir(curdir / ".file")
        print(f"work directory: {os.getcwd()}")

    def tearDown(self) -> None:
        os.chdir(original_workdir)

    def test_read_csv(self):
        """读取csv文件, 取读所有行, 每一行结果为list"""
        with open("csv.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
                print(f"len: {len(row)}, h1: {row[0]}, h2: {row[1]}")

    def test_dict_read_csv(self):
        """读取csv文件, 不包括第一行, 每一行结果为dict"""
        with open("csv.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
                print(f"len: {len(row)}, h1: {row['h1']}, h2: {row['h2']}")

    def test_write_csv(self):
        """写csv文件, 每一行为list"""
        with open("tmp/csv.csv", "w") as file:
            # delimiter指定分隔符
            writer = csv.writer(file, delimiter=",")
            row = ["a", "b", "c", "d"]
            # 写一行
            writer.writerow(row)
            # 写多行
            writer.writerows([row, row])

    def test_dict_write_csv(self):
        """写csv文件, 每一行为dict"""
        with open("tmp/dict-csv.csv", "w") as file:
            # delimiter指定分隔符
            fieldnames = ["h1", "h2", "h3", "h4"]
            writer = csv.DictWriter(file, delimiter=",", fieldnames=fieldnames)
            writer.writeheader()
            row = {"h1": "a", "h2": "b", "h3": "c", "h4": "d"}
            # 写一行
            writer.writerow(row)
            # 写多行
            writer.writerows([row, row])
