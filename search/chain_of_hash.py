from __future__ import annotations

import hashlib
from typing import Any, Type


class Node:
    """ハッシュを構成するノード"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """初期化"""
        self.key = key  # キー
        self.value = value  # 値
        self.next = next  # 後続ノードへの参照で、チェインにおける後続ポインタ


class ChainedHash:
    """チェイン法を実現するクラス"""

    def __init__(self, capacity: int) -> None:
        """初期化処理

        初期化処理後に生成されるtableの全要素はNoneであり、全バケットは空。
        """
        self.capacity = capacity  # ハッシュ表の容量
        self.table = [None] * self.capacity  # ハッシュ表を格納するList型の配列

    def hash_value(self, key: Any) -> int:
        """ハッシュ値をもとめる

        - keyがint型の場合: keyをハッシュのcapacityで割った余剰をハッシュ値とする
        - keyがint型ではない場合: バイト文字列のハッシュ値を16進数の文字列として取り出し、
          int型に変換したものをcapacityで割った余剰をハッシュ値とする
        """
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def search(self, key: Any) -> Any:
        """keyを持つ要素の探索

        １．ハッシュ関数によってキーをハッシュ値に変換
        ２．ハッシュ値をインデックスとするバケットに着目する
        ３．バケットが参照する線形リストを先頭から順に探索し、キーと同じ値が見つかれば探索成功。見つからなければ失敗。
        """
        hash = self.hash_value(key)

        p = self.table[hash]  # 着目ノード

        while p is not None:
            if p.key == key:
                return p.value  # 探索成功
            p = p.next  # 後続のノードに着目

        return None  # 探索失敗

    def add(self, key: Any, value: Any) -> bool:
        """要素の追加

        １．ハッシュ関数によってキーをハッシュ値に変換
        ２．ハッシュ値をインデックスとするバケットに着目する
        ３．バケットが参照する線形リストを先頭から順に探索し、キーと同じ値があれば
           登録済みのため挿入失敗。最後まで要素がなければノードを追加
        """
        hash = self.hash_value(key)
        p = self.table[hash]  # 着目ノード
        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp  # ノードの追加
        return True

    def remove(self, key: Any) -> bool:
        """要素の削除

        １．ハッシュ関数によってキーをハッシュ値に変換
        ２．ハッシュ値をインデックスとするバケットに着目する
        ３．バケットが参照する線形リストを先頭から順に探索し、
            キーと同じ値があれば削除し、ない場合は削除失敗。
        """
        hash = self.hash_value(key)
        p = self.table[hash]  # 着目ノード
        pp = None  # 前回の着目ノード

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next  # 前回の着目ノードを更新
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        """ハッシュ表の結果出力"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end="")
            while p is not None:
                print(f" → {p.key} ({p.value})", end="")
                p = p.next
            print()


# 実行
# 容量13のハッシュ表を生成
hash = ChainedHash(13)
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
    print(f"そのキーを持つ値は{result}です")
else:
    print("該当する値が見つかりませんでした。")


print("削除するキーを1 ~ 13で入力してください。")
key = int(input("key:"))
if not hash.remove(key):
    print("削除失敗!")


hash.dump()
