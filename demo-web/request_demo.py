import requests
import unittest
import json
import requests.utils
from .fastapi_demo import start_server_for_test, stop_server_for_test
import time

# 调用fastapi_demo.py的启动的后端
host = "http://127.0.0.1:8080/rest"


class RequestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        start_server_for_test()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls) -> None:
        stop_server_for_test()

    def test_get(self):
        """get和query parameter"""
        # 请求参数跟url一起
        res = requests.get(f"{host}/get/path?required_query_parameters=required value")
        print(res.text)

        # 请求参数使用params传参
        res = requests.get(f"{host}/get/path", params={"required_query_parameters": "required value", "optional_query_parameters": "optional value"})
        print(res.text)

    def test_post(self):
        """post和request body,response body"""
        # 使用data传参, 需要先转换为json字符串
        res = requests.post(f"{host}/post", data=json.dumps({"required_field": "required value"}))
        # 读取成dict
        result_json = res.json()
        self.assertTrue(isinstance(result_json, dict))
        print(result_json)

    def test_put(self):
        """put"""
        # 需要先转换为json字符串
        res = requests.put(f"{host}/put/1", data=json.dumps({"required_field": "required value"}))
        print(res.json())

    def test_delete(self):
        """delete"""
        res = requests.delete(f"{host}/delete/1")
        print(res.json())

    def test_form_data(self):
        """form表单请求(文件上传也是使用此格式)"""
        # form表单不需要转换成json字符串
        res = requests.post(f"{host}/form-data", data={"form_field": "form field value"})
        print(res.text)

    def test_form_urlencoded(self):
        """普通的form表单请求"""
        # 多个参数使用&连接
        res = requests.post(f"{host}/form-data", headers={"Content-Type": "application/x-www-form-urlencoded"}, data="form_field=form field value&k2=v2")
        print(res.text)

    def test_header(self):
        """header 请求头和响应头"""
        # 这边也可以设置cookie,并且这边设置的会覆盖使用cookie设置的值
        res = requests.get(f"{host}/headers", headers={"simple-header": "simple header value"})
        # 响应头
        print(res.headers)
        print(res.text)

    def test_cookie(self):
        """cookie 请求cookie和响应cookie"""
        # 这边设置的cookie可以被使用headers设置的cookie覆盖
        res = requests.get(f"{host}/cookies", cookies={"simple_cookie": "simple cookie value"})
        # 响应的cookie
        print(res.cookies)
        print(res.text)

    def test_session(self):
        """session可以保存会话中的cookie"""
        session = requests.session()
        # 这边的header可以认为是默认的header,会与请求指定的header进行整合
        # 可以使用update,也可以直接使用session.headers[header_name]=header_value进行赋值
        session.headers.update({"simple-header": "simple-header session value"})

        # 为session的cookie设置默认值
        requests.utils.add_dict_to_cookiejar(session.cookies, {"simple_cookie": "simple cookie session value"})

        # 可以为session设置代理
        # session.proxies = {"http": "localhost:8888", "https": "localhost:8888"}
        # 取消ssl的校验
        # session.verify = False

        res = session.get(f"{host}/headers")
        print(res.json())

        # 这边的header会与session的header进行整合
        res = session.get(f"{host}/headers", headers={"simple-header": "simple-header request value"})
        print(res.json())

        res = session.get(f"{host}/cookies")
        print(res.json())

        # 这边可以使用上面设置的cookie
        res = session.get(f"{host}/cookies")
        print(res.json())

        session.close()
