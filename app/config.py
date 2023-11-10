import json
import os
from typing import Callable

from pyrogram.filters import Filter
from pyrogram.types import Message


class _Config:
    def __init__(self):
        self.CMD_DICT: dict[str, dict[str, Callable, str]] = {}

        self.CMD_TRIGGER: str = os.environ.get("CMD_TRIGGER", ".")

        self.CONVO_DICT: dict[int, dict[str | int, Message | Filter | None]] = {}

        self.DEV_MODE: int = int(os.environ.get("DEV_MODE", 0))

        self.DB_URL: str = os.environ.get("DB_URL")

        self.FBAN_LOG_CHANNEL: int = int(
            os.environ.get("FBAN_LOG_CHANNEL", os.environ.get("LOG_CHAT"))
        )

        self.LOG_CHAT: int = int(os.environ.get("LOG_CHAT"))

        self.SUDO: bool = False

        self.SUDO_TRIGGER: str = os.environ.get("SUDO_TRIGGER", "!")

        self.OWNER_ID = int(os.environ.get("OWNER_ID"))

        self.SUDO_CMD_LIST: list[str] = []

        self.SUDO_USERS: list[int] = []

        self.UPSTREAM_REPO: str = os.environ.get(
            "UPSTREAM_REPO", "https://github.com/thedragonsinn/plain-ub"
        )

    def __str__(self):
        config_dict = self.__dict__.copy()
        config_dict["DB_URL"] = "SECURED"
        return json.dumps(config_dict, indent=4, ensure_ascii=False, default=str)


Config = _Config()
