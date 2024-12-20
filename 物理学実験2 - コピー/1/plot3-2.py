import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# CSVファイルの読み込み
def load_csv(file_path, x_column, I_column):
    data = pd.read_csv(file_path)
    x = data[x_column].values * 1e-3  # 指定されたx列をmmからmに変換
    I = data[I_column].values  # 指定されたI列を取得
    return x, I

# 理想曲線の計算（二重スリット、異なるスリット幅）
def ideal_intensity_double_slit(x, A1, A2, a1, a2, lambda_, L, d):
    k_a1 = np.pi * a1 * x / (lambda_ * L)
    k_a2 = np.pi * a2 * x / (lambda_ * L)
    sinc_a1 = np.sinc(k_a1 / np.pi)  # numpyのsincはpiで正規化されている
    sinc_a2 = np.sinc(k_a2 / np.pi)

    # 位相差を x に依存させる
    delta_phi = 2 * np.pi * d * x / (lambda_ * L)
    complex_amplitude = A1 * sinc_a1 + A2 * sinc_a2 * np.exp(1j * delta_phi)
    intensity = np.abs(complex_amplitude)**2
    return intensity

# 平行移動してピークを中心に調整
def shift_to_center(x, I):
    peak_index = np.argmax(I)  # 最大値のインデックスを取得
    peak_position = x[peak_index]  # 最大値の位置を取得
    x_centered = x - peak_position  # 平行移動
    return x_centered

# 比較する関数
def compare_graph_double_slit(csv_path, x_column, I_column, A1, A2, a1, a2, lambda_, L, d, ideal_offset):
    # CSVデータの読み込み
    x_data, I_data = load_csv(csv_path, x_column, I_column)

    # データを平行移動してピークを中心に調整
    x_data_centered = shift_to_center(x_data, I_data)

    # 理想曲線の計算
    x_ideal = np.linspace(min(x_data_centered), max(x_data_centered), 1000)
    I_ideal = ideal_intensity_double_slit(x_ideal, A1, A2, a1, a2, lambda_, L, d)

    # 理想曲線のみ左に移動
    x_ideal_shifted = x_ideal - ideal_offset

    # スケールを実験データに合わせる
    I_ideal_scaled = I_ideal * (np.max(I_data) / np.max(I_ideal))

    # グラフのプロット
    plt.figure(figsize=(10, 6))
    plt.plot(x_data_centered, I_data, 'o', label="Experimental Data", markersize=5)
    plt.plot(x_ideal_shifted, I_ideal_scaled, '-', label="Ideal Curve (Double Slit, Different Widths)")
    plt.xlabel("x (shifted to center) [m]")
    plt.ylabel("Intensity I(x)")
    plt.title("Comparison of Experimental Data and Ideal Curve ")
    plt.legend()
    plt.grid()
    plt.show()

# 使用例
# パラメータを設定
A1 = 2          # スリット1の振幅
A2 = 2          # スリット2の振幅
a1 = 92e-6      # スリット1の幅 (80 µm)
a2 = 80e-6      # スリット2の幅 (80 µm)
lambda_ = 6.7e-7 # 波長 (670 nm)
L = 0.45        # スリットからの距離 (45 cm)
d = 800e-6      # スリット間隔
ideal_offset = 0.0003 # 理想曲線を左に移動する距離 (0.0006 m)

# CSVファイルのパスを指定
csv_file_path = r"C:\Users\gamiy\assignment\物理学実験\物理学実験2\1\huku.csv"  # 適切なパスに置き換える
# 以下の列名をCSVファイル内の列名に置き換える
x_column = "長さ(複)"  # x列の名前（例: "Position"）
I_column = "強度(複)"  # I列の名前（例: "Intensity"）

# グラフを比較
compare_graph_double_slit(csv_file_path, x_column, I_column, A1, A2, a1, a2, lambda_, L, d, ideal_offset)
