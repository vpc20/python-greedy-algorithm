# from functools import lru_cache

# coins should be sorted in descending order


# def coin_change_greedy_recur(coin_list, change):
#     if change in coin_list:
#         return 1
#     coin_sublist = [coin for coin in coin_list if coin <= change]
#     if len(coin_sublist) == 0:
#         return 0
#     count = coin_change_greedy_recur(coin_sublist, change - coin_sublist[0])
#     return 1 + count if count != 0 else 0


# def coin_change_greedy_recur(coin_list, change):
#     if change <= 0:
#         return 0
#     for coin in coin_list:
#         if change >= coin:
#             return 1 + coin_change_greedy_recur(coin_list, change - coin)


# def coin_change_greedy_recur(coin_list, change):
#     if change == 0:
#         return 0
#     if change < 0:
#         return -1
#     for coin in coin_list:
#         if change >= coin:
#             coin_count = coin_change_greedy_recur(coin_list, change - coin)
#             return 1 + coin_count if coin_count >= 0 else -1
#     else:
#         return -1

# coins should be sorted in descending order
def coin_change_greedy_recur(coins, change):
    if change == 0:
        return 0

    while coins and change < coins[0]:
        coins.pop(0)
    if not coins:
        return -1

    chg = coin_change_greedy_recur(coins, change - coins[0])
    return -1 if chg == -1 else 1 + chg


# does not handle cases where giving change is not possible
# def coin_change_recur(coin_list, change):
#     @lru_cache(maxsize=1000)
#     def _coin_change_recur(change):
#         min_count = change
#         if change == 0:
#             return 0
#         for coin in coin_list:
#             if change >= coin:
#                 coin_count = 1 + _coin_change_recur(change - coin)
#                 min_count = min(min_count, coin_count)
#         return min_count
#
#     return _coin_change_recur(change)


if __name__ == '__main__':
    # print(coin_change_greedy_recur([1], 1))
    # print(coin_change_greedy_recur([1], 2))
    # print(coin_change_greedy_recur([1], 3))

    print(coin_change_greedy_recur([50, 25, 10, 5, 1], 1))
    print(coin_change_greedy_recur([50, 25, 10, 5, 1], 2))
    print(coin_change_greedy_recur([50, 25, 10, 5, 1], 3))
    print(coin_change_greedy_recur([50, 25, 10, 5, 1], 4))
    print(coin_change_greedy_recur([50, 25, 10, 5, 1], 5))

    print(coin_change_greedy_recur([50, 25, 10, 5, 1], 21))

    print(coin_change_greedy_recur([25, 10, 5], 63))

    # print(coin_change_greedy_recur([50, 25, 10, 5, 1], 11))

    # print(coin_change_greedy_recur([50, 25, 10, 5, 1], 63))
    # print(coin_change_greedy_recur([10, 5], 11))
    # print(coin_change_greedy_recur([1], 2))
    # print(coin_change_greedy_recur([5], 3))
