# Project Structure
- `task1_greed_dynamic_algorithm.py` — this task implements two algorithms to determine the set of coins required to form a given sum.

Two approaches are implemented:

1. Greedy algorithm (`find_coins_greedy`)
2. Dynamic programming algorithm (`find_min_coins`)

- `task2_monte_carlo.py` — the purpose of this task is to calculate the definite integral of the function:

\[
f(x) = x^2
\]

on the interval:

\[
[0, 2]
\]

using the **Monte Carlo method**.

The result obtained using the Monte Carlo method is compared with:

1. The result calculated using the `quad` function from the `scipy.integrate` module.
2. The analytical value of the integral.


## Task 1 — Greedy and Dynamic Algorithms

### Comparison of the efficiency of the algorithms

For the sum `113`, the following results were obtained:

```text
Greedy Algorithm:
{50: 2, 10: 1, 2: 1, 1: 1}
Execution Time: 0.00000221 seconds

Dynamic Programming:
{50: 2, 10: 1, 2: 1, 1: 1}
Execution Time: 0.00003883 seconds
```

Both algorithms found the same optimal set of coins:

```text
50 × 2 + 10 × 1 + 2 × 1 + 1 × 1 = 113
```

To test the performance of the algorithms on a large amount, the value `100000` was used.

The results obtained:

```text
Comparison for amount 100000:

Greedy: 0.00000104 seconds
Dynamic programming: 0.03538325 seconds
```

The difference in speed became much more noticeable. The greedy algorithm ran approximately 34,000 times faster than the dynamic programming algorithm.

The reason lies in the different time complexity of the algorithms.

### Conclusion

The results of the experiment showed that for the set of coins:

```python
[50, 25, 10, 5, 2, 1]
```

the greedy algorithm is much more efficient in terms of execution time.

For the amount `113`, both algorithms found the same optimal solution of 5 coins, but the greedy algorithm ran faster.

When the amount is increased to `100000`, the difference in speed becomes much more noticeable.

Thus, for the set of coins `[50, 25, 10, 5, 2, 1]` given in the problem, it is more appropriate to use the greedy algorithm due to its high speed and low memory requirements. Dynamic programming is advisable to use when it is necessary to find the optimal result for an arbitrary set of denominations with certainty.

## Task 2. Monte Carlo Integration

### Results
The program produced the following results:

```text
Monte Carlo result: 2.6621601675110775
Quad result: 2.6666666666666665
Analytical result: 2.6666666666666665
Quad error estimate: 2.9605947323337504e-14
Difference between Monte Carlo and quad: 0.004506499155588983
```

---

## Comparison of Results

The `quad` result and the analytical result are identical:

```text
Quad:       2.6666666666666665
Analytical: 2.6666666666666665
```

The Monte Carlo result:

```text
2.6621601675110775
```

is also very close to the exact value.

A small difference is expected because the Monte Carlo method is based on randomly generated values. Therefore, the result may be slightly different each time the program is executed.

Increasing the number of random points generally improves the accuracy of the Monte Carlo approximation.

---

## Conclusion

The definite integral of the function:

\[
f(x) = x^2
\]

on the interval `[0, 2]` was successfully calculated using the Monte Carlo method.

The Monte Carlo method produced:

```text
2.6621601675110775
```

while the `quad` function and analytical calculation produced:

```text
2.6666666666666665
```

The difference between the Monte Carlo approximation and the exact result is approximately `0.0045065`, with a relative error of about `0.17%`.

The obtained results confirm that the Monte Carlo algorithm correctly approximates the value of the definite integral.

The small difference between the Monte Carlo result and the exact value is caused by the random nature of the method. With a sufficiently large number of random points, the Monte Carlo estimate approaches the exact value.

Therefore, the implemented Monte Carlo method can be considered correct for the calculation of this definite integral.
