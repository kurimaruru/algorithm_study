import copy
from typing import List

number_arr = [100, 89, 47, 13, 2, 5, 98, 32, 45, 67, 48]


def linear_search_for_sentinel_loop(number_arr: List[int]):
    """番兵法"""
    key = int(input("探したい数字を入力してください: "))

    arr_for_sentinel = copy.deepcopy(number_arr)
    arr_for_sentinel.append(key)

    counter = 0
    while True:
        if arr_for_sentinel[counter] == key:
            break

        counter += 1

    return (
        print(f"{key}は見つかりませんでした。")
        if counter == len(number_arr)
        else print(f"{counter+1}回目のループで{key}は見つかりました。")
    )


linear_search_for_sentinel_loop(number_arr=number_arr)
