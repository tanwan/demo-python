from mitmproxy import http
from mitmproxy import ctx
from mitmproxy.coretypes import multidict
from mitmproxy.script import concurrent
import json
import time

# 可以直接在脚本声明方法, 也可以使用addons的方法
def request(flow: http.HTTPFlow) -> None:
    """请求的入口"""
    # 启动后使用按E可以查看到日志
    # host: 域名/ip, path: 请求path(以/开头)和地址栏参数, 需要去掉地址栏参数才能拿到path
    ctx.log.info(f"host:{flow.request.host}, path:{flow.request.path.split('?')[0]}")

    # pretty_host: 优先使用请求头的Host的值, pretty_url: 同pretty_host
    ctx.log.info(f"pretty_host:{flow.request.pretty_host}, pretty_url:{flow.request.pretty_url}")


def response(flow: http.HTTPFlow):
    """响应的入口"""
    # content: 响应体,是字节数组
    ctx.log.info(f"content:{flow.response.content},{type(flow.response.content)}")


class RedirectAddon:
    def request(self, flow: http.HTTPFlow):
        """修改scehme, host, port, path, method"""
        if flow.request.path.split("?")[0] == "test_redirect":
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


class ProxyAddon:
    def request(self, flow: http.HTTPFlow) -> None:
        if flow.request.path == "/rest/proxy":
            # 直接给response赋值
            flow.response = http.Response.make(200, b'{"k1":"v1","k2":"v2"}', {"Content-Type": "application/json"})


class ConcurrentAddon:
    # 目前有bug,用不了
    # @concurrent
    def request(self, flow: http.HTTPFlow) -> None:
        if flow.request.query.get("addon") == "concurrent":
            key = flow.request.query.get("required_query_parameters")
            ctx.log.info(f"{time.time()},{key} start")
            time.sleep(5)
            ctx.log.info(f"{time.time()},{key} end")


# 也可以使用addons的方法,addons类中的方法跟直接在脚本声明的方法是一样的
addons = [
    RedirectAddon(),
    QueryParameters(),
    RequestBodyAddon(),
    RequestFormAddon(),
    HeaderAddon(),
    CookieAddon(),
    ResponseAddon(),
    ProxyAddon(),
    ConcurrentAddon(),
]


# 直接执行此脚本,会启动mitmweb,这样就可以debug
if __name__ == "__main__":
    import sys

    # 也可以使用mitmproxy
    # mitmproxy要求interactive shell environment
    # 在pycharm中需要使用terminal进行启动: python web/mitmproxy_script.py
    # 所以这边先使用mitmweb
    from mitmproxy.tools.main import mitmweb

    # 使用当前脚本当成mitmweb的脚本
    sys.argv = ["mitmweb", "-s", __file__, "-p", "18888"]
    if sys.argv[0] == "mitmweb":
        sys.argv += ["--web-port", "18081"]
    mitmweb()
