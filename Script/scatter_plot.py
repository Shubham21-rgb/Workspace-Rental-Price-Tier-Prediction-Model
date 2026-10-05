#max_seats was having the high correlation.
sns.scatterplot(
    data=train,
    x="max_seats",
    y="price_tier",
    alpha=0.4,
    color="teal",
    edgecolor="w",
    linewidth=0.5
)
