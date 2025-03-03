# pip install langchain-deepseek
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
import unittest


class DeepSeekDemo(unittest.TestCase):
    def setUp(self) -> None:
        # 设置环境变量: export DEEPSEEK_API_KEY=""
        self.model = ChatDeepSeek(
            model="deepseek-chat",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )

    def test_invoke(self):
        """使用invoke直接调用, 如果需要多个invoke的话,推荐使用chain调用"""
        # 简单调用
        print(self.model.invoke("写一首诗"))
        # 使用role调用
        messages = [
            # 也可以直接使用tuple, 相当于("system", "你是一个AI助手")
            SystemMessage("你是一个AI助手"),
            HumanMessage("写一首诗"),
        ]
        print(self.model.invoke(messages))

    def test_prompt_template(self):
        """使用提示模板"""
        # 相当于ChatPromptTemplate.from_messages([("system", "你是一个翻译助手, 请将以下句子翻译成{language}"), ("user", "{text}")])
        prompt_template = ChatPromptTemplate.from_messages(
            [SystemMessagePromptTemplate.from_template("你是一个翻译助手, 请将以下句子翻译成{language}"), HumanMessagePromptTemplate.from_template("{text}")]
        )

        # prompt_template.invoke后, 会将模板组装成message
        print(self.model.invoke(prompt_template.invoke({"language": "中文", "text": "hello world"})))

    def test_chain(self):
        """使用chain调用"""
        prompt_template = ChatPromptTemplate.from_messages([("system", "你是一个翻译助手, 请将以下句子翻译成{language}"), ("user", "{text}")])
        # StrOutputParser直接获取出content
        parser = StrOutputParser()
        chain = prompt_template | self.model | parser

        print(chain.invoke({"language": "中文", "text": "hello world"}))

    def test_stream(self):
        """返回流"""
        # 同步使用stream, 异步使用astream
        for chunk in self.model.stream("写一首诗"):
            print(chunk.content, end="|")
