from __future__ import annotations

import hashlib
from enum import Enum
from typing import Any, Type


class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2


class Bucket:
    """ハッシュを構成するバケット"""

    def __init__(
        self, key: Any = None, value: Any = None, status: Status = Status.EMPTY
    ):
        self.key = key
        self.value = value
        self.status = status

    def set(self, key: Any, value: Any, status: Status = Status.EMPTY):
        self.key = key
        self.value = value
        self.status = status

    def set_status(self, status: Status):
        self.status = status


class OpenHash:
    """オープンアドレス法を実現するハッシュクラス"""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def rehash_value(self, key: Any) -> int:
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        """バケットの探索"""
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            # バケットが空であれば探索終了
            if p.status == Status.EMPTY:
                break
            # バケットに値が格納されていて、キーが一致すれば探索成功
            elif p.status == Status.OCCUPIED and p.key == key:
                return p
            # バケットに値が格納されていて、キーが一致しなければ再ハッシュ
            hash = self.rehash_value(key)
            p = self.table[hash]

    def search(self, key: Any) -> Any:
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None

    def add(self, key: Any, value: Any) -> bool:
        # すでにキーが存在する場合は追加しない
        if self.search(key) is not None:
            return False
        # ハッシュ値を求め、バケットに格納
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.status == Status.EMPTY or p.status == Status.DELETED:
                self.table[hash].set(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(key)
            p = self.table[hash]
        return False

    def remove(self, key: Any) -> int:
        p = self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True


hash = OpenHash(13)
test_data = [
    {"key": 0, "value": "cat"},
    {"key": 1, "value": "dog"},
    {"key": 2, "value": "fish"},
    {"key": 4, "value": "lion"},
    {"key": 5, "value": "koara"},
    {"key": 6, "value": "kaba"},
    {"key": 7, "value": "wani"},
    {"key": 10, "value": "usagi"},
    {"key": 11, "value": "bear"},
    {"key": 14, "value": "dog2"},
    {"key": 27, "value": "dog3"},
]
print("テストデータの追加")
for data in test_data:
    hash.add(data["key"], data["value"])

print("探索するキーを1 ~ 13で入力してください。")
key = int(input("key:"))
result = hash.search(key)
if result is not None:
    print(f"キー{key}の値は{result}です。")
else:
    print("そのキーは存在しません。")

print("キ削除するキーを1 ~ 13で入力してください。")
key = int(input("key:"))
if hash.remove(key):
    print(f"キー{key}の値を削除しました。")
