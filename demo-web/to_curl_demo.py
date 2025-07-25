import re
import unittest
from http.server import BaseHTTPRequestHandler
from io import BytesIO
import pyperclip


class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, raw_http_request):
        self.rfile = BytesIO(raw_http_request.encode("utf-8"))
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

        try:
            self.data = raw_http_request[raw_http_request.index("\n\n") + 2 :].rstrip()
        except ValueError:
            self.data = None

        # Host
        self.url = self.headers.get("Host", "<hostname>")


def to_curl(raw_http_request):
    clipboard = raw_http_request is None
    if clipboard:
        raw_http_request = pyperclip.paste()
    request = HTTPRequest(raw_http_request.strip())
    print(raw_http_request)
    curl = f"curl --location --request {request.command} '{request.url}{request.path}' "
    boundary = None
    for k, v in sorted(request.headers.items()):
        if k == "Content-Length":
            continue
        if k == "Content-Type" and v.startswith("multipart/form-data"):
            boundary = v.split(";")[1].replace("boundary=", "").strip()
        curl += f"-H '{k}: {v}' "
    if request.data:
        data = request.data
        if boundary:
            params = data.split(boundary)
            for param in params:
                names = re.findall('name="(\w+)"', param)
                if names:
                    name = names[0]
                    values = re.findall(f'name="{name}"\n\n(\w+)\n', param)
                    if values:
                        curl += f"--form '{name}=\"{values[0]}\"'"
        else:
            if isinstance(data, bytes):
                data = data.decode("utf-8")
            curl += f"-d '{data}'"
    if clipboard:
        pyperclip.copy(curl)
    print("\n" + curl)


if __name__ == "__main__":
    # 可以在.zshrc中指定: alias tocurl="python to_curl_demo.py(使用绝对路径)", 就可以直接使用tocurl将剪切板的内容转为curl
    to_curl(None)


class ToCurlDemo(unittest.TestCase):
    def test_to_curl(self):
        str = """
POST /api/auth HTTP/1.1
Host: 127.0.0.1:9000
Connection: keep-alive
Content-Length: 42
Accept: application/json, text/plain, */*
Content-Type: application/json
Origin: http://127.0.0.1:9000
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1:9000/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7

{"username":"admin","password":"12345678"}
"""
        to_curl(str)
