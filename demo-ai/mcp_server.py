from fastmcp import FastMCP, Context

mcp = FastMCP(name="McpServerDemo")
transport = "stdio"
# transport = "streamable-http"


@mcp.tool(
    name="get_file_content",  # 唯一标识, 默认使用函数名
    description="返回demo-python指定文件的内容",  # 描述
    tags={"files", "tool"},  # 用于过滤的标签, 可选
)
def get_file_content(file: str) -> dict:
    """@mcp.tool用来暴露可调用的工具, 如果注解有指定了其它参数, 那么这个的注释将不会被使用"""
    print(f"get_file_content called with file name: {file}")
    return {"file": file, "content": "content"}


# resource和prompt, 目前还不清楚mcp client是如何能调用到这些方法
@mcp.resource(
    uri="files://files",  # 唯一标识, 必填
    name="get_file_content",  # 名称, 默认为函数名
    description="用来返回只读资源",  # 描述
    mime_type="application/json",  # content-type, 可选
    tags={"files", "resource"},  # 用于过滤的标签, 可选
)
def get_resources() -> dict:
    """mcp.resource用来暴露只读资源,如果注解有指定了其它参数, 那么这边的注释将不会被使用"""
    print(f"get_resources called")
    return {"file": "aaa", "context": "bbb"}


@mcp.resource("files://file/{file}/content")
def get_resource_template(file: str):
    """带参数的为resource模板"""
    print(f"get_resource_template called with name: {file}")
    return {"file": file, "context": "content"}


@mcp.prompt
def get_prompt(text: str) -> str:
    """mcp.prompt用来定义prompt"""
    print(f"get_prompt called with text: {text}")
    return f"Please summarize the following text:\n\n{text}"


if __name__ == "__main__":
    if transport == "stdio":
        # 使用标准输入输出来启动mcp server
        mcp.run(transport="stdio")
    elif transport == "streamable-http":
        # 使用streamable-http来启动mcp server
        mcp.run(transport="streamable-http", port=18000)
