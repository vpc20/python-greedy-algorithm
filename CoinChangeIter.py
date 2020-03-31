# def coin_change_greedy_iter(coins, change):
#     min_coin = 0
#     for coin in coins:
#         if change >= coin:
#             count, change = divmod(change, coin)
#             min_coin += count
#     return -1 if change != 0 else min_coin


# return min no. of coins and the coin count for each denomination
def coin_change_greedy_iter(coins, change):
    min_coin = 0
    coin_count = []
    for coin in coins:
        if change >= coin:
            count, change = divmod(change, coin)
            min_coin += count
            coin_count.append((coin, count))
    return (-1, []) if change != 0 else (min_coin, coin_count)


if __name__ == '__main__':
    print(coin_change_greedy_iter([50, 25, 10, 5, 1], 63))
    print(coin_change_greedy_iter([10, 5], 11))
    print(coin_change_greedy_iter([50, 25, 10, 5, 1], 2))
