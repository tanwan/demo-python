import requests
import unittest
import json
import requests.utils
from .fastapi_demo import start_server_for_test, stop_server_for_test
from .mitmproxy_script import start_mitm_for_test, stop_mitm_for_test
import time

# 需要先启动fastapi_demo.py(后端)和mitmproxy_scipt.py(代理)

host = "http://127.0.0.1:8080/rest"

proxies = {"http": "http://127.0.0.1:18888"}


class MitmproxyDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        start_server_for_test()
        start_mitm_for_test()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls) -> None:
        stop_server_for_test()
        time.sleep(2)
        stop_mitm_for_test()

    def test_redirect(self):
        """修改scehme, host, port, path, method See RedirectAddon"""
        res = requests.get(f"{host}/test_redirect", proxies=proxies)
        print(res.text)

    def test_query_parameters(self):
        """修改请求参数 See QueryParameters"""
        res = requests.get(f"{host}/get/path?required_query_parameters=required value&addon=query_parameters", proxies=proxies)
        print(res.text)

    def test_request_body(self):
        """修改请求体 See RequestBodyAddon"""
        payload = json.dumps({"required_field": "required value"})
        res = requests.post(f"{host}/post?addon=request_body", data=payload, proxies=proxies)
        print(res.json())

        res = requests.post(f"{host}/post?addon=request_body_replace", data=payload, proxies=proxies)
        print(res.json())

    def test_form(self):
        """修改form表单 See RequestFormAddon"""
        # application/x-www-form-urlencoded
        payload = "form_field=form field value&k2=v2"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = requests.post(f"{host}/form-data?addon=form", headers=headers, data=payload, proxies=proxies)
        print(res.text)

        # form-data
        res = requests.post(f"{host}/form-data?addon=form", data={"form_field": "form field value"}, proxies=proxies)
        print(res.text)

    def test_header(self):
        """修改header See HeaderAddon"""
        res = requests.get(f"{host}/headers?addon=header", headers={"simple-header": "simple header value", "delete-header": "delete"}, proxies=proxies)
        # 响应头
        print(res.headers)
        print(res.text)

    def test_cookie(self):
        """修改cookie CookieAddon"""
        res = requests.get(f"{host}/cookies?addon=cookie", cookies={"simple_cookie": "simple cookie value", "delete_cookie": "cookie"}, proxies=proxies)
        # 响应的cookie
        print(res.cookies)
        print(res.text)

    def test_response(self):
        """修改响应 ResponseAddon"""
        payload = json.dumps({"required_field": "required value"})
        res = requests.post(f"{host}/post?addon=response_body", data=payload, proxies=proxies)
        print(res.json())
        res = requests.post(f"{host}/post?addon=response_body_replace", data=payload, proxies=proxies)
        print(res.json())

    def test_proxy_as_server(self):
        """mitm当成服务器,直接给出响应 ProxyAsServerAddon"""
        res = requests.post(f"{host}/proxy_as_server", proxies=proxies)
        print(res.json())
