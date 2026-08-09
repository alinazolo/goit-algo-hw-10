import time

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
  """
  Greedy coin search algorithm.
  Starts with the largest denomination and takes
  the maximum possible number of such coins.
  """
  result = {}

  for coin in COINS:
        count = amount // coin

        if count > 0:
            result[coin] = count
            amount %= coin

  return result


def find_min_coins(amount):
    """
    Find the minimum number of coins needed
    using dynamic programming.
    """

    # min_coins[i] - minimum number of coins,
    # needed to form the sum i
    min_coins = [float("inf")] * (amount + 1)

    # last_coin[i] - last coin used
    # to obtain the sum i
    last_coin = [0] * (amount + 1)

    min_coins[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in COINS:
            if coin <= current_amount:
                previous_amount = current_amount - coin

                if min_coins[previous_amount] + 1 < min_coins[current_amount]:
                    min_coins[current_amount] = min_coins[previous_amount] + 1
                    last_coin[current_amount] = coin

    # Restoration of the coin set
    result = {}
    current_amount = amount

    while current_amount > 0:
        coin = last_coin[current_amount]

        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin

    return result


def measure_time(function, amount):
    start = time.perf_counter()

    result = function(amount)

    end = time.perf_counter()

    return result, end - start


if __name__ == "__main__":
    amount = 113

    greedy_result, greedy_time = measure_time(find_coins_greedy, amount)

    dynamic_result, dynamic_time = measure_time(find_min_coins, amount)

    print(f"Amount: {amount}")

    print("\nGreedy Algorithm:")
    print(greedy_result)
    print(f"Execution Time: {greedy_time:.8f} seconds")

    print("\nDynamic Programming:")
    print(dynamic_result)
    print(f"Execution Time: {dynamic_time:.8f} seconds")

    # Verification on a large amount
    large_amount = 100_000

    print(f"\nComparison for amount {large_amount}:")

    _, greedy_large_time = measure_time(find_coins_greedy, large_amount)

    _, dynamic_large_time = measure_time(find_min_coins, large_amount)

    print(f"Greedy: {greedy_large_time:.8f} seconds")

    print(f"Dynamic programming: {dynamic_large_time:.8f} seconds")
