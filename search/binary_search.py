from typing import List

sorted_number_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(sorted_number_arr: List[int]):
    """2分探索"""
    key = int(input("探したい数字を入力してください: "))

    first_index = 0
    last_index = len(sorted_number_arr) - 1

    counter = 0
    while True:
        center_index = (first_index + last_index) // 2
        if sorted_number_arr[center_index] == key:
            print(f"{counter+1}回目のループで{key}は見つかりました。")
            return
        # キーが中央値より大きい場合は、中央より後ろで絞り込む
        elif sorted_number_arr[center_index] < key:
            first_index = center_index + 1
        # キーが中央値より小さい場合は、中央より前で絞り込む
        else:
            last_index = center_index - 1

        if first_index > last_index:
            print(f"{key}は見つかりませんでした。")
            break

        counter += 1


binary_search(sorted_number_arr=sorted_number_arr)
