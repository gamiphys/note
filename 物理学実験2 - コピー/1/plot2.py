import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# CSVファイルの読み込み（(単)のみ抽出）
def load_csv_single(file_path):
    data = pd.read_csv(file_path)
    x_single = data["長さ(単)"].dropna().values  * 1e-3# "長さ(単)"列を取得し、欠損値を除去
    I_single = data["強度(単)"].dropna().values  # "強度(単)"列を取得し、欠損値を除去
    return x_single, I_single

# 理想曲線の計算（単スリット）
def ideal_intensity(x, I0, a, lambda_, L):
    k_a = np.pi * a * x / (lambda_ * L)
    intensity = np.zeros_like(k_a)
    nonzero_indices = k_a != 0
    intensity[nonzero_indices] = I0 * (np.sin(k_a[nonzero_indices]) / k_a[nonzero_indices]) ** 2
    intensity[~nonzero_indices] = I0
    return intensity

# 平行移動してピークを中心に調整
def shift_to_center(x, I):
    peak_index = np.argmax(I)
    peak_position = x[peak_index]
    x_centered = x - peak_position
    return x_centered

# 比較する関数
def compare_graph_single(csv_path, I0, a, lambda_, L):
    # CSVデータの読み込み
    x_data, I_data = load_csv_single(csv_path)

    # データを平行移動してピークを中心に調整
    x_data_centered = shift_to_center(x_data, I_data)

    # 理想曲線の計算
    x_ideal = np.linspace(min(x_data_centered), max(x_data_centered), 1000)
    I_ideal = ideal_intensity(x_ideal, I0, a, lambda_, L)

    # グラフのプロット
    plt.figure(figsize=(10, 6))
    plt.plot(x_data_centered, I_data, 'o', label="Experimental Data (Single)", markersize=5)
    plt.plot(x_ideal, I_ideal, '-', label="Ideal Curve")
    plt.xlabel("x[m] (shifted to center)")
    plt.ylabel("Intensity I(x)")
    plt.title("Comparison of Experimental Data and Ideal Curve (Single Slit)")
    plt.legend()
    plt.grid()
    plt.show()

# 使用例
I0 = 26  # 最大強度
a = 100e-6   # スリット幅（1.33 µm）
lambda_ = 7.5e-7  # 波長（例: 0.77 µm）
L = 0.3   # スリットからの距離（30.0 cm）

csv_file_path = r"C:\Users\gamiy\assignment\物理学実験\物理学実験2\1\huku.csv"  # 適切なパスに置き換える

# グラフを比較
compare_graph_single(csv_file_path, I0, a, lambda_, L)
