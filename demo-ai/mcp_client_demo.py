import unittest
from fastmcp import Client
from pathlib import Path

curdir = Path(__file__).parent


class MCPClientDemo(unittest.IsolatedAsyncioTestCase):
    """测试协程使用IsolatedAsyncioTestCase"""

    def setUp(self) -> None:
        # 使用http server的mcp server
        # self.client = Client("http://127.0.0.1:18000/mcp")
        # 使用本地python脚本的mcp server, 可以使用相对路径, 也可以使用绝对路径
        self.client = Client(curdir / "mcp_server.py")

    async def test_list_tools(self):
        """测试list_tools"""
        async with self.client:
            tools = await self.client.list_tools()
            print(tools)

    async def test_call_tool(self):
        """测试调用mcp server的tool"""
        async with self.client:
            result = await self.client.call_tool("get_file_content", {"file": "mcp_client_demo.py"})
            print(result)

    async def test_list_resources(self):
        """测试list resources"""
        async with self.client:
            resources = await self.client.list_resources()
            print(resources)
            resources_templates = await self.client.list_resource_templates()
            print(resources_templates)

    async def test_list_prompts(self):
        async with self.client:
            prompts = await self.client.list_prompts()
            print(prompts)
