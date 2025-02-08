import pandas as pd
import matplotlib.pyplot as plt

# データを読み込む
data = pd.DataFrame({
    "Year": [2020, 2021, 2022],
    "Sales": [100, 150, 200]
})

# データを表示
print(data)

# グラフを描画
plt.plot(data["Year"], data["Sales"])
plt.title("Yearly Sales")
plt.show()