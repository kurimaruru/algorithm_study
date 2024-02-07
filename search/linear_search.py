from typing import List

number_arr = [100, 89, 47, 13, 2, 5, 98, 32, 45, 67, 48]


def linear_search_by_while(number_arr: List[int]):
    """線形探索をwhile文で実行"""
    key = int(input("探したい数字を入力してください: "))
    counter = 0

    while True:
        if counter == len(number_arr):
            print(f"{key}は見つかりませんでした。")
            return

        if number_arr[counter] == key:
            print(f"{counter+1}回目のループで{key}は見つかりました。")
            return

        counter += 1


def linear_search_by_for(number_arr: List[int]):
    """線形探索をfor文で実行"""
    key = int(input("探したい数字を入力してください: "))

    for i in range(len(number_arr)):
        if number_arr[i] == key:
            print(f"{i+1}回目のループで{key}は見つかりました。")
            return

    print(f"{key}は見つかりませんでした。")


linear_search_by_while(number_arr=number_arr)
linear_search_by_for(number_arr=number_arr)
