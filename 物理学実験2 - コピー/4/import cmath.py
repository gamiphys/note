# -*- coding: utf-8 -*-

import sys
import io

# 標準出力のエンコーディングを設定
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import cmath
import math

def find_integer_combinations(a):
    combinations = []
    limit = int(math.sqrt(a)) + 1
    for h in range(-limit, limit):
        for k in range(-limit, limit):
            for l in range(-limit, limit):
                if h**2 + k**2 + l**2 == a:
                    combinations.append((h, k, l))
    return combinations

def calculate_F(h, k, l):
    i = complex(0, 1)
    term1 = 54
    term2 = 18 * cmath.exp(2 * cmath.pi * i * (0.5 * h + 0.5 * k + 0.5 * l))
    term3 = 10 * cmath.exp(2 * cmath.pi * i * (0.5 * k + 0.5 * l))
    term4 = 10 * cmath.exp(2 * cmath.pi * i * (0.5 * h + 0.5 * l))
    term5 = 10 * cmath.exp(2 * cmath.pi * i * (0.5 * h + 0.5 * k))
    return term1 + term2 + term3 + term4 + term5

def main():
    a = int(input("整数 a を入力してください: "))
    combinations = find_integer_combinations(a)
    
    if not combinations:
        print(f"{a} を満たす整数の組 (h, k, l) は見つかりませんでした。")
    else:
        for h, k, l in combinations:
            F_value = calculate_F(h, k, l)
            print(f"(h, k, l) = ({h}, {k}, {l}) のとき、F(h, k, l) = {F_value}")

if __name__ == "__main__":
    main()
