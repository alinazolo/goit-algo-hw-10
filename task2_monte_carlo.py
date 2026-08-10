import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def f(x):
    return x**2


def monte_carlo_integral(func, a, b, n=100000):
    """
    Обчислення визначеного інтеграла методом Монте-Карло.
    """

    # Генеруємо випадкові точки x на відрізку [a, b]
    random_x = np.random.uniform(a, b, n)

    # Обчислюємо значення функції у випадкових точках
    function_values = func(random_x)

    # Середнє значення функції множимо на довжину відрізка
    integral = (b - a) * np.mean(function_values)

    return integral


# Межі інтегрування
a = 0
b = 2

# Кількість випадкових точок
n = 100000

# Метод Монте-Карло
monte_carlo_result = monte_carlo_integral(f, a, b, n)

# Перевірка за допомогою scipy.integrate.quad
quad_result, error = quad(f, a, b)

# Аналітичний результат
analytical_result = (b**3) / 3 - (a**3) / 3

print(f"Monte Carlo result: {monte_carlo_result}")
print(f"Quad result: {quad_result}")
print(f"Analytical result: {analytical_result}")
print(f"Quad error estimate: {error}")

print(
    f"Difference between Monte Carlo and quad: {abs(monte_carlo_result - quad_result)}"
)


# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, "r", linewidth=2)

ix = np.linspace(a, b, 100)
iy = f(ix)

ax.fill_between(ix, iy, color="gray", alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])

ax.set_xlabel("x")
ax.set_ylabel("f(x)")

ax.axvline(x=a, color="gray", linestyle="--")

ax.axvline(x=b, color="gray", linestyle="--")

ax.set_title(f"Графік інтегрування f(x) = x^2 від {a} до {b}")

plt.grid()
plt.show()
