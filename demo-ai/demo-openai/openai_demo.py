import unittest
import os
from openai import OpenAI


class ListDemo(unittest.TestCase):

    def setUp(self) -> None:
        # 设置环境变量: export OPENAI_API_KEY=""
        # self.client = OpenAI()
        # 这边使用阿里百炼大模型, 符合openai的规范, 可以直接使用openai的sdk
        # See https://help.aliyun.com/zh/model-studio/getting-started/
        self.client = OpenAI(api_key=os.getenv("ALI_API_KEY"), base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

    def test_completion(self):
        completion = self.client.chat.completions.create(
            model="qwen-plus",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "写一首诗"},
            ],
        )
        print(completion.choices[0].message)
