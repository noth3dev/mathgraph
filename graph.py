import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def plot_functions_and_find_intersections(func1, func2, x_range=(-10, 10)):
    x = sp.symbols('x')
    f1 = sp.sympify(func1)
    f2 = sp.sympify(func2)
    
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals1 = [float(f1.subs(x, val)) for val in x_vals]
    y_vals2 = [float(f2.subs(x, val)) for val in x_vals]
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals1, label=f'y = {func1}')
    plt.plot(x_vals, y_vals2, label=f'y = {func2}')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('함수의 그래프')
    plt.grid(True)

    intersections = sp.solve(f1 - f2, x)
    real_intersections = [sp.N(point) for point in intersections if point.is_real]

    for point in real_intersections:
        y_value = float(f1.subs(x, point))
        plt.plot(float(point), y_value, 'ro')  # 교점 표시
        plt.annotate(f'({point.evalf():.2f}, {y_value:.2f})', (float(point), y_value), textcoords="offset points", xytext=(0,10), ha='center')

    plt.show()

    if real_intersections:
        print("교점:")
        for point in real_intersections:
            y_value = float(f1.subs(x, point))
            print(f'({point.evalf():.2f}, {y_value:.2f})')
    else:
        print("실수 교점이 없습니다.")

# 사용 예시:
func1 = input("첫 번째 함수를 입력하세요 (x에 대한 식): ")
func2 = input("두 번째 함수를 입력하세요 (x에 대한 식): ")

plot_functions_and_find_intersections(func1, func2)
