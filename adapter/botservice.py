from typing import Generator


class BotAdapter:
    """定义所有 Chatbot 的通用接口"""
    preset_name: str = "default"

    def __int__(self): ...

    async def ask(self, msg: str) -> Generator[str]: ...
    """向 AI 发送消息"""

    async def rollback(self): ...
    """回滚对话"""

    async def reset(self): ...
    """重置会话"""
