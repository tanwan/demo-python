from fastapi import FastAPI, Request, Header, Response, Cookie, Form
from typing import Optional
import uvicorn
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

# 访问http://127.0.0.1:8080/docs可以查看接口文档


class RequestBody(BaseModel):
    required_field: str
    optional_field: Optional[str] = "default value"


# 所有请求都可以有request: Request, response: Response入参


@app.get("/rest/get/{path_parameters}")
def simple_get(path_parameters, required_query_parameters, optional_query_parameters=None):
    """get请求,地址参数,没有默认值的为必填参数,也可以定义为optional_query_parameters:Optional[str]=None"""
    return {
        "method": "simple_get",
        "path_parameters": path_parameters,
        "required_query_parameters": required_query_parameters,
        "optional_query_parameters": optional_query_parameters,
    }


@app.post("/rest/post")
def simple_post(request_body: RequestBody):
    """post请求,RequestBody为request body"""
    return {"method": "simple_post", "request_body": request_body}


@app.put("/rest/put/{id}")
def simple_put(id, request_body: RequestBody):
    return {"method": "simple_put", "id": id, "request_body": request_body}


@app.delete("/rest/delete/{id}")
def simple_delete(id):
    return {"method": "simple_delete", "id": id}


@app.post("/rest/form-data")
async def simple_form_data(request: Request, form_field: str = Form(...)):
    """form-data(文件上传)/x-www-form-urlencoded(普通form表单请求),需要安装pip install python-multipart"""
    # 如果需要使用request.form()获取到所有form的请求参数,需要使用async和await,否则只能在方法的参数把所有请求参数都列出来
    from_data = await request.form()
    from_data_json = jsonable_encoder(from_data)
    return {"method": "simple_form_data", "form_field": form_field, "forms": from_data_json}


@app.get("/rest/headers")
def simple_headers(request: Request, response: Response, simple_header: Optional[str] = Header(None)):
    """
    请求头
    如果有相同的请求头,则使用Optional[List[str]]
    入参这边会默认将-转为_,所以请求中的请求头应该传simple-header(不区分大小写),如果不要这个转换,则使用Header(None, convert_underscores=False)
    """
    # 为response设置header
    response.headers["simple-header"] = "simple_header override"
    # request.headers可以拿到所有header
    return {"method": "simple_headers", "simple_header": simple_header, "headers": request.headers}


@app.get("/rest/cookies")
def simple_cookies(request: Request, response: Response, simple_cookie: Optional[str] = Cookie(None)):
    """
    cookie
    """
    # 设置cookie
    response.set_cookie("add_cookie", "add cookie value")
    return {"method": "simple_cookies", "simple_cookie": simple_cookie, "cookies": request.cookies}


if __name__ == "__main__":
    """启动"""
    # 这边的fastapi_demo:app是当前文件名和FastAPI()的实例名称
    uvicorn.run(app="fastapi_demo:app", host="0.0.0.0", port=8080)
