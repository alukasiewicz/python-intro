"""
Przykład 2: Wizualizacja danych statystycznych w Seaborn

Seaborn automatycznie stylizuje wykresy i uproszcza pracę z danymi z Pandas.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Przykładowy zbiór danych: wbudowany 'tips'
tips = sns.load_dataset("tips")

# Wykres rozrzutu z automatycznym kolorowaniem wg płci
plt.figure(figsize=(7, 4))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
plt.title("Napiwki vs suma rachunku (Seaborn)")
plt.tight_layout()
plt.show()

# Wykres pudełkowy (boxplot)
plt.figure(figsize=(6, 4))
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("Rozkład rachunków wg dnia i płci (Seaborn)")
plt.tight_layout()
plt.show()
