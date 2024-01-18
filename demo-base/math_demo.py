import unittest
import math
import decimal


class MathDemo(unittest.TestCase):
    def test_approximate(self):
        """
        近似
        银行家舍入算法(四舍六入五取偶): 5后还有非0数字, 直接进1, 否则看5前面的数字, 奇数进1, 偶数舍弃
        浮点数使用round会有精度问题, 有精度要求的需要使用decimal
        round
        {:.nf}
        取整
        math.ceil: 向上
        math.floor: 向下
        其它近似方法
        decimal.ROUND_HALF_UP: 四舍五入
        decimal.ROUND_UP: 进一法
        decimal.ROUND_CEILING: 正数进一法, 负数去尾法
        decimal.ROUND_DOWN: 去尾法
        decimal.ROUND_FLOOR: 正数去尾法, 负数进一法
        """
        # 四舍六入五取偶
        self.assertEqual(2.68, round(2.676, 2))
        self.assertEqual(2.67, round(2.674, 2))

        # 5后有非0数字, 进1
        self.assertEqual(2.68, round(2.6751, 2))

        # 5后无非0数字, 5前为奇数, 进1, 这边正确应该是2.68, 但是由于浮点数并不能精确地表示出来, 因此这边可能会有误差, decimal.Decimal(2.675)可以看出实际的值
        self.assertEqual(2.67, round(2.675, 2))
        # 使用Decimal解决精度问题, 需要传入字符串, 否则还是会有精度问题
        self.assertEqual(decimal.Decimal("2.68"), round(decimal.Decimal("2.675"), 2))

        # 5后无非0数字, 5前为偶数, 舍弃, 这边正确应该是2.68, 浮点数不能精确地表示出来, decimal.Decimal(2.685)可以看出实际的值
        self.assertEqual(2.69, round(2.685, 2))
        self.assertEqual(decimal.Decimal("2.68"), round(decimal.Decimal("2.685"), 2))

        # format同样也是银行家舍入算法
        self.assertEqual("2.67", "{:.2f}".format(2.674))

        # 向上取整
        self.assertEqual(2, math.ceil(1.3))
        self.assertEqual(-1, math.ceil(-1.3))

        # 向下取整
        self.assertEqual(1, math.floor(1.3))
        self.assertEqual(-2, math.floor(-1.3))

        # 其它近似方法使用quantize, .01表示保留两位小数
        self.assertEqual(decimal.Decimal("2.68"), decimal.Decimal("2.675").quantize(decimal.Decimal(".01"), rounding=decimal.ROUND_HALF_UP))

    def test_convertion_between_float_deciaml(self):
        """
        decimal与浮点的转换
        浮点 -> decimal: 需要转为字符串,否则有精度问题
        decimal -> 浮点: float(decimal)
        """
        # 浮点->decimal, 浮点要先转为字符串
        print(decimal.Decimal(str(2.685)))
        print(float(decimal.Decimal("2.685")))

    def test_decimal_conversion(self):
        """
        进制转换
        bin 二进制
        oct 八进制
        hex 十六进制
        int 10进制, 0b|0o|0x可以省略
        """
        self.assertEqual("0b1010", bin(10))
        self.assertEqual("0o12", oct(10))
        self.assertEqual("0x20", hex(32))

        # 其它进制转10进制,0b|0o|0x可以省略
        self.assertEqual(32, int("0x20", 16))
