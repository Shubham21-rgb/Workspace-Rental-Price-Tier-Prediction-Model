import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(18,14))

corr_matrix = numerical_columns.corr()

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    vmin=-1,
    vmax=1,
    linewidths=0.5,
    annot_kws={"size": 7},
    cbar_kws={"shrink" : 0.8}
    
)

plt.xticks(rotation=45, ha="right" , fontsize=9)
plt.yticks(rotation=0, fontsize=9)

plt.title("Correlation with price_teir", fontsize=16,pad=20,weight="bold")

plt.tight_layout()

plt.show()

#corr(x,x) = 1 



