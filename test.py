import pandas as pd
import matplotlib.pyplot as plt

# サンプルデータを作成
data = {
    "Month": ["January", "February", "March", "April", "May", "June"],
    "Sales": [100, 120, 150, 170, 200, 220],
    "Profit": [20, 25, 35, 40, 50, 60]
}

# データを表示
print(data)

# グラフを描画
plt.plot(data["Year"], data["Sales"])
plt.title("Yearly Sales")
plt.show()