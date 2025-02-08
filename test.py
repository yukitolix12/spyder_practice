import pandas as pd
import matplotlib.pyplot as plt

# サンプルデータを作成
data = {
    "Month": ["January", "February", "March", "April", "May", "June"],
    "Sales": [100, 120, 150, 170, 200, 220],
    "Profit": [20, 25, 35, 40, 50, 60]
}

# データフレームに変換
df = pd.DataFrame(data)

# グラフのサイズを設定
plt.figure(figsize=(10, 6))

# 折れ線グラフ（売上）
plt.plot(df["Month"], df["Sales"], marker="o", label="Sales", color="blue")

# 棒グラフ（利益）
plt.bar(df["Month"], df["Profit"], alpha=0.6, label="Profit", color="orange")

# タイトルとラベルを設定
plt.title("Sales and Profit Analysis", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Amount", fontsize=12)