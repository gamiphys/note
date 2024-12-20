import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# CSVファイルの読み込み
def load_csv(file_path, x_column, I_column):
    data = pd.read_csv(file_path)
    x = data[x_column].values * 1e-3  # 指定されたx列を取得
    I = data[I_column].values  # 指定されたI列を取得
    return x, I

# 理想曲線の計算
def ideal_intensity(x, I0, a, d, lambda_, L):
    k_a = np.pi * a * x / (lambda_ * L)
    k_d = np.pi * d * x / (lambda_ * L)
    intensity = I0 * (np.cos(k_d) ** 2) * (np.sin(k_a) / k_a) ** 2
    intensity[np.isnan(intensity)] = I0  # k=0のときNaNをI0に置換
    return intensity

# 平行移動してピークを中心に調整
def shift_to_center(x, I):
    peak_index = np.argmax(I)  # 最大値のインデックスを取得
    peak_position = x[peak_index]  # 最大値の位置を取得
    x_centered = x - peak_position  # 平行移動
    return x_centered

# 比較する関数
def compare_graph(csv_path, x_column, I_column, I0, a, d, lambda_, L, ideal_offset):
    # CSVデータの読み込み
    x_data, I_data = load_csv(csv_path, x_column, I_column)

    # データを平行移動してピークを中心に調整
    x_data_centered = shift_to_center(x_data, I_data)

    # 理想曲線の計算
    x_ideal = np.linspace(min(x_data_centered), max(x_data_centered), 1000)
    x_ideal_shifted = x_ideal - ideal_offset  # 理想曲線のオフセットを適用
    I_ideal = ideal_intensity(x_ideal_shifted, I0, a, d, lambda_, L)

    # グラフのプロット
    plt.figure(figsize=(10, 6))
    plt.plot(x_data_centered, I_data, 'o', label="Experimental Data", markersize=5)
    plt.plot(x_ideal, I_ideal, '-', label="Ideal Curve (Shifted)")
    plt.xlabel("x[m] (shifted to center)")
    plt.ylabel("Intensity I(x)")
    plt.title("Comparison of Experimental Data and Ideal Curve (Ideal Curve Shifted)")
    plt.legend()
    plt.grid()
    plt.show()

# 使用例
# パラメータを設定
I0 = 16          # 最大強度
a = 80e-6        # スリット幅 (80 µm)
d = 800e-6       # スリット間隔 (800 µm)
lambda_ = 6.7e-7 # 波長 (670 nm)
L = 0.45         # スリットからの距離 (45 cm)
ideal_offset = -0.00030  # 理想曲線を左に移動する距離 (0.0006 m)

# CSVファイルのパスを指定
csv_file_path = r"C:\Users\gamiy\assignment\物理学実験\物理学実験2\1\huku.csv"  # 適切なパスに置き換える
# 以下の列名をCSVファイル内の列名に置き換える
x_column = "長さ(複)"  # x列の名前（例: "Position"）
I_column = "強度(複)"  # I列の名前（例: "Intensity"）

# グラフを比較
compare_graph(csv_file_path, x_column, I_column, I0, a, d, lambda_, L, ideal_offset)
