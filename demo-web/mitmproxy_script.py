from mitmproxy import http
from mitmproxy import ctx
from mitmproxy.coretypes import multidict
from mitmproxy.script import concurrent
import json
from multiprocessing import Process
import psutil

# mitmproxy的插件有两种方式
# 1. 完整的Addon类
# 2. 简化的脚本语法(将整个模块当做是一个插件对象）


# 简化的脚本语法, 只需要定义request/response方法
def request(flow: http.HTTPFlow) -> None:
    """请求的入口"""
    ctx.log.info(f"host:{flow.request.host}, path:{flow.request.path.split('?')[0]}")
    # pretty_host: 优先使用请求头的Host的值, pretty_url: 同pretty_host
    ctx.log.info(f"pretty_host:{flow.request.pretty_host}, pretty_url:{flow.request.pretty_url}")


def response(flow: http.HTTPFlow):
    """响应的入口"""
    # content: 响应体,是字节数组
    ctx.log.info(f"content:{flow.response.content},{type(flow.response.content)}")


# 完整的Addon类
class RedirectAddon:
    def request(self, flow: http.HTTPFlow):
        """修改scehmehost, port, path, method"""
        # path是包括query param的
        if flow.request.path.split("?")[0].endswith("test_redirect"):
            flow.request.scheme = "http"
            flow.request.host = "localhost"
            flow.request.port = 8080
            flow.request.path = "/rest/post"
            flow.request.method = "POST"
            payload = json.dumps({"required_field": "mitmproxy value"})
            flow.request.content = payload.encode(encoding="utf-8")


class QueryParameters:
    def request(self, flow: http.HTTPFlow):
        """地址栏参数"""
        if flow.request.query.get("addon") == "query_parameters":
            # query: 地址栏参数,就是个dict
            ctx.log.info(f"query:{flow.request.query}, type:{type(flow.request.query)}")
            del flow.request.query["addon"]
            flow.request.query["required_query_parameters"] = "mitm value"
            flow.request.query["optional_query_parameters"] = "mitm optional"


class RequestBodyAddon:
    def request(self, flow: http.HTTPFlow):
        if flow.request.query.get("addon") == "request_body":
            """请求体"""
            # flow.request.content: 字节数组的请求体
            ctx.log.info(f"content:{flow.request.content}, type:{type(flow.request.content)}")
            # 字节需要先转成字符串
            body = json.loads(flow.request.content.decode())
            body["required_field"] = "mitm value"
            flow.request.content = json.dumps(body).encode("utf-8")
        if flow.request.query.get("addon") == "request_body_replace":
            """请求体直接替换"""
            flow.request.content = flow.request.content.replace(b"required value", b"mitm value")


class RequestFormAddon:
    def request(self, flow: http.HTTPFlow):
        """修改form表单,x-www-form-urlencoded和form-data都可以,文件上传的暂时没试"""
        if flow.request.query.get("addon") == "form":
            # urlencoded_form: x-www-form-urlencoded参数,也是个dict
            ctx.log.info(f"urlencoded_form:{flow.request.urlencoded_form}, type:{type(flow.request.urlencoded_form)}")
            flow.request.urlencoded_form["form_field"] = "mitm value"
            flow.request.urlencoded_form["k1"] = "mitm v1"


class HeaderAddon:
    def request(self, flow: http.HTTPFlow):
        if flow.request.query.get("addon") == "header":
            """修改请求header"""
            # headers: 请求头, Headers类型的
            ctx.log.info(f"header:{flow.request.headers}, type:{type(flow.request.headers)}")
            del flow.request.headers["delete-header"]
            flow.request.headers["simple-header"] = "mitm request header"
            flow.request.headers["mitm-request-add-header"] = "mitm request add header"

    def response(self, flow: http.HTTPFlow):
        if flow.request.query.get("addon") == "header":
            """修改响应header"""
            flow.response.headers["mitm-response-add-header"] = "mitm response add header"


class CookieAddon:
    def request(self, flow: http.HTTPFlow):
        if flow.request.query.get("addon") == "cookie":
            """修改请求cookie"""
            # cookies: cookie
            ctx.log.info(f"cookie:{flow.request.cookies}, type:{type(flow.request.cookies)}")
            del flow.request.cookies["delete_cookie"]
            flow.request.cookies["simple_cookie"] = "mitm cookie value"
            flow.request.cookies["mitm_request_add_cookie"] = "mitm request add cookie"

    def response(self, flow: http.HTTPFlow):
        if flow.request.query.get("addon") == "cookie":
            """修改响应cookie"""
            # 需要使用MultiDict设置cookie的属性
            flow.response.cookies["mitm-response-add-cookie"] = ("mitm response add cookie", multidict.MultiDict())


class ResponseAddon:
    def response(self, flow: http.HTTPFlow):
        if flow.request.query.get("addon") == "response_body":
            """响应体"""
            # 字节需要先转成字符串
            body = json.loads(flow.response.content.decode())
            body["request_body"]["required_field"] = "mitm value"
            flow.response.content = json.dumps(body).encode("utf-8")
        if flow.request.query.get("addon") == "response_body_replace":
            """响应体直接替换"""
            flow.response.content = flow.response.content.replace(b"required value", b"mitm value")


class ProxyAsServerAddon:
    def request(self, flow: http.HTTPFlow) -> None:
        if flow.request.path == "/rest/proxy_as_server":
            # 直接给response赋值
            flow.response = http.Response.make(200, b'{"k1":"v1","k2":"v2"}', {"Content-Type": "application/json"})


# 使用addon, 需要添加addon的实例到addons列表中
addons = [RedirectAddon(), QueryParameters(), RequestBodyAddon(), RequestFormAddon(), HeaderAddon(), CookieAddon(), ResponseAddon(), ProxyAsServerAddon()]


# 直接执行此脚本,会启动mitmweb,这样就可以debug
if __name__ == "__main__":
    # 也可以使用mitmproxy, mitmproxy要求interactive shell environment(交互式shell), 交互式shell在pycharm中需要使用terminal进行启动: python web/mitmproxy_script.py
    from mitmproxy.tools.main import mitmweb

    # 使用当前脚本当成mitmweb的脚本
    mitmweb(["-s", __file__, "-p", "18888", "--web-port", "18081"])


def start_mitm_for_test():
    """给测试使用, 需要新开进程,否则会阻塞住测试"""
    global proc
    from mitmproxy.tools.main import mitmweb

    proc = Process(target=mitmweb, kwargs={"args": ["-s", __file__, "-p", "18888", "--web-port", "18081"]})
    proc.start()
    print("start server")
    return proc


def stop_mitm_for_test():
    pid = proc.pid
    parent = psutil.Process(pid)
    for child in parent.children(recursive=True):
        child.kill()
    proc.terminate()
    print("stop mitm")
