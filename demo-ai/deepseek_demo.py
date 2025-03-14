import unittest
import os
import json
from openai import OpenAI


class DeepSeekDemo(unittest.TestCase):

    def setUp(self) -> None:
        # 设置环境变量: export DEEPSEEK_API_KEY=""
        # 这边使用deepseek, 符合openai的规范, 可以直接使用openai的sdk
        # See https://api-docs.deepseek.com/zh-cn/
        api_key = os.getenv("DEEPSEEK_API_KEY")
        self.model = "deepseek-chat"
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com/v1")

    def test_completion(self):
        """
        对话补全
        role:
            system: 设定整体对话的行为和风格, 比如告诉模型如何回应
            user: 用户输入的消息
            assistant: 模型的回复, AI生成的内容
            tool: 外部工具/函数调用返回的内容, 回传给ai时, 需要带上tool_call_id, 详见test_function_call
        response_format: 可以要求以严格的json返回
        """
        messages = [
            {"role": "system", "content": "你是一个AI助手,回复都使用json格式"},
            {"role": "user", "content": "写一首诗"},
        ]
        response_format = {"type": "json_object"}
        response = self.client.chat.completions.create(model=self.model, messages=messages, response_format=response_format)
        # 回答为response.choices[0].message.content
        print(response.choices[0].message)
        print(json.loads(response.choices[0].message.content))

    def test_multi_round(self):
        """
        多轮对话
        /chat/completions API 是一个无状态API, 即服务端不记录用户请求的上下文,用户在每次请求时,需将之前所有对话历史拼接好后,传递给对话API
        """
        # 第一轮
        messages = [{"role": "system", "content": "只需要给出答案"}, {"role": "user", "content": "世界第一高峰的哪一个"}]
        response = self.client.chat.completions.create(model=self.model, messages=messages)

        messages.append(response.choices[0].message)
        print(f"Messages Round 1: {messages}")

        # 第二轮
        messages.append({"role": "user", "content": "世界第二呢"})
        # 相当于[{"role": "system", "content": "只需要给出答案"}, {"role": "user", "content": "世界第一高峰的哪一个"}, {"role":"assistant", "content":"珠穆朗玛峰"}, {"role": "user", "content": "世界第二呢"}]
        response = self.client.chat.completions.create(model=self.model, messages=messages)
        print(f"Messages Round 2: {response.choices[0].message}")

    def test_reasoner(self):
        """
        推理模型
        message.reasoning_content: 推理过程
        message.content: 回答
        """
        messages = [{"role": "user", "content": "9.11和9.8,哪个比较大"}]
        response = self.client.chat.completions.create(model="deepseek-reasoner", messages=messages)
        # 比对话多了个reasoning_content的字段
        print(response.choices[0].message)

    def test_mock_rag(self):
        """模拟rag"""
        # 模拟从向量数据库检索出来的结果
        context = "数学成绩出来了, 小明考了100分, 小红考了99分, 小乐考了90分"
        question = "谁的成绩最好?"
        # 将上下文和问题一起传给ai, 上下文可以放在system也可以放在user
        messages = [{"role": "system", "content": "你会根据提供的上下文, 回答用户的问题, 上下文:{context}"}, {"role": "user", "content": f"{question}"}]
        response = self.client.chat.completions.create(model=self.model, messages=messages)
        print(response.choices[0].message.content)

    def test_function_call(self):
        """
        方法调用
        ai本身并不会调用方法,需要程序自己去调用,然后将函数返回值再传回给AI
        """
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get weather of an location",
                    "parameters": {
                        # 参数为json格式
                        "type": "object",
                        # 定义方法的各个参数
                        "properties": {
                            "location": {
                                # type支持: string, number, integer, boolean, array, object
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "date": {
                                "type": "string",
                                "description": "The date of the weather for this location",
                            },
                        },
                        "required": ["location"],
                    },
                },
            },
        ]
        messages = [{"role": "user", "content": "厦门2025-01-01的天气怎么样"}]
        response = self.client.chat.completions.create(model=self.model, messages=messages, tools=tools)
        message = response.choices[0].message
        print(message)
        tool_call = message.tool_calls[0]
        # 调用外部函数, 函数的参数也可以直接从json中一个一个提取出来
        answer = self.call_function(tool_call.function.name, json.loads(tool_call.function.arguments))

        # 传加上次AI的回答和调用外部函数的结果
        messages.append(message)
        messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": answer})
        response = self.client.chat.completions.create(model=self.model, messages=messages, tools=tools)
        print(f"answer: {response.choices[0].message.content}")

    def call_function(self, name, args):
        """使用if来判断具体要调用哪个函数"""
        if name == "get_weather":
            return self.get_weather(**args)

    def get_weather(self, location, date):
        print(f"get_weather: {location}, {date}")
        return "天气非常好"
