import requests
import unittest
import json
import requests.utils

# 调用fastapi_demo.py的启动的后端, 代理使用mitmproxy.scipt.py
host = "http://127.0.0.1:8080/rest"

proxies = {"http": "127.0.0.1:18888"}


class MitmproxyDemo(unittest.TestCase):
    def test_redirect(self):
        """修改scehme, host, port, path, method"""
        res = requests.get(f"{host}/test_redirect", proxies=proxies)
        print(res.text)

    def test_query_parameters(self):
        """修改请求参数"""
        res = requests.get(f"{host}/get/path?required_query_parameters=required value&addon=query_parameters", proxies=proxies)
        print(res.text)

    def test_request_body(self):
        """修改请求体"""
        payload = json.dumps({"required_field": "required value"})
        res = requests.post(f"{host}/post?addon=request_body", data=payload, proxies=proxies)
        print(f"result:{res.json()}")
        res = requests.post(f"{host}/post?addon=request_body_replace", data=payload, proxies=proxies)
        print(f"result:{res.json()}")

    def test_form(self):
        """修改form表单"""
        # application/x-www-form-urlencoded
        payload = "form_field=form field value&k2=v2"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = requests.post(f"{host}/form-data?addon=form", headers=headers, data=payload, proxies=proxies)
        print(res.text)

        # form-data
        payload = {"form_field": "form field value"}
        res = requests.post(f"{host}/form-data?addon=form", data=payload, proxies=proxies)
        print(res.text)

    def test_header(self):
        """修改header"""
        headers = {"simple-header": "simple header value", "delete-header": "delete"}
        res = requests.get(f"{host}/headers?addon=header", headers=headers, proxies=proxies)
        # 响应头
        print(res.headers)
        print(res.text)

    def test_cookie(self):
        """修改cookie"""
        cookies = {"simple_cookie": "simple cookie value", "delete_cookie": "cookie"}
        res = requests.get(f"{host}/cookies?addon=cookie", cookies=cookies, proxies=proxies)
        # 响应的cookie
        print(res.cookies)
        print(res.text)

    def test_response(self):
        """修改响应"""
        payload = json.dumps({"required_field": "required value"})
        res = requests.post(f"{host}/post?addon=response_body", data=payload, proxies=proxies)
        print(f"result:{res.json()}")
        res = requests.post(f"{host}/post?addon=response_body_replace", data=payload, proxies=proxies)
        print(f"result:{res.json()}")

    def test_proxy(self):
        """mitm直接当成代理"""
        res = requests.post(f"{host}/proxy", proxies=proxies)
        print(f"result:{res.json()}")

    def test_concurrent(self):
        """并发"""
        res = requests.get(f"{host}/get/path?required_query_parameters=first&addon=concurrent", proxies=proxies)
        print(res.text)
        res = requests.get(f"{host}/get/path?required_query_parameters=second&addon=concurrent", proxies=proxies)
        print(res.text)
