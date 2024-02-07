# 線形探索

直線状に並んだ配列から目的とするキーを持つ要素に出会うまで先頭から順に走査する探索方法

[線形探索のアニメーション参考](https://qiita.com/midiambear/items/f1491f1eb108af40b7ab#:~:text=%E3%83%AA%E3%82%B9%E3%83%88%E3%81%AE%E6%8E%A2%E7%B4%A2-,%E7%B7%9A%E5%BD%A2%E6%8E%A2%E7%B4%A2,-%E7%B7%9A%E5%BD%A2%E6%8E%A2%E7%B4%A2%E3%81%AF)

## 特徴

要素数が n であれば、これらの条件を判断する回数はいずれも平均 **n / 2 回**である。

## 実行コマンド

```bash
$ poetry run python3 search/linear_search.py
```

# 番兵法

配列の末尾に番兵（探索するキーと同じ値）を追加し、探索した結果が元の配列から見つかったものなのか、末尾に追加した番兵なのかを判定する探索方法

![Alt text](image.png)

## 特徴

番兵法は繰り返しの終了判定を削減する役割を持っている。

例えば、線形探索ではループの中で毎回配列の終端かを判定していたが、番兵法ではその必要がない。

```python
    while True:
        # 線形探索では毎回終端を判定していた
        if counter == len(number_arr):
            print(f"{key}は見つかりませんでした。")
            return

        if number_arr[counter] == key:
            print(f"{counter+1}回目のループで{key}は見つかりました。")
            return

        counter += 1
```

## 実行コマンド

```bash
$ poetry run python3 search/linear_search_for_sentinel_loop.py
```

# 2 分探索

要素がキーの昇順または降順にソートされている配列から効率よく探索を行うアルゴリズムである。

[2 分探索のアニメーション](https://qiita.com/midiambear/items/f1491f1eb108af40b7ab#%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2:~:text=%E8%A1%A8%E3%81%97%E3%81%BE%E3%81%99%E3%80%82-,%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2,-%E6%95%B4%E5%88%97%E3%81%95%E3%82%8C)

## 特徴

中央値の左 or 右の中央値がキーと一致するかを探索範囲がなくなるまで続ける。

繰り返しのたびに探索範囲がほぼ半分になるため、必要となる比較回数は平均**log n**である。
