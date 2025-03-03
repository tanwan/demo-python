import unittest
import chromadb
from pathlib import Path
from chromadb.utils.embedding_functions.onnx_mini_lm_l6_v2 import ONNXMiniLM_L6_V2

file_dir = Path(__file__).parent / ".file"
tmp_dir = Path(file_dir / "tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)


class ChromaDemo(unittest.TestCase):
    def setUp(self) -> None:
        # Client:非持久化的
        # PersistentClient: 持久化的
        # HttpClient: server/client模式, server启动: chroma run --path /db_path
        self.chroma_client = chromadb.PersistentClient(path=str(tmp_dir))
        # 嵌入算法
        ef = ONNXMiniLM_L6_V2(preferred_providers=["CPUExecutionProvider"])
        # create_collection只创建collection, embedding_function用来指定嵌入算法
        # see https://docs.trychroma.com/docs/embeddings/embedding-functions
        self.collection = self.chroma_client.get_or_create_collection(name="test", embedding_function=ef)

    def test_upsert(self):
        """
        upsert: 更新或者添加数据
        add: 只能添加数据
        Chroma会使用默认的嵌入模型将文本处理为向量, 也可以自定义嵌入的模型, 必须提供唯一id
        """
        # 使用add的话,只能添加数据
        self.collection.upsert(
            documents=["This is a document about pineapple", "This is a document about oranges", "This is a document about apples"],
            # metadatas是可选的
            metadatas=[{"source": "test1"}, {"source": "test2"}, {"source": "test3"}],
            ids=["id1", "id2", "id3"],
        )
        # 默认取出前10条
        print(self.collection.peek())

    def test_query(self):
        """query"""
        self.test_upsert()
        # 返回2条结果
        results = self.collection.query(query_texts=["apple"], n_results=2)
        print(results)
