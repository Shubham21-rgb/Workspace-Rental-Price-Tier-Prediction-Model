def calculate_outliers(data):
    q1_x,q3_x=data.quantile(0.25) , data.quantile(0.75)

    iqr_x=q3_x - q1_x

    lower_x,upper_x= q1_x - 1.5 * iqr_x, q3_x + 1.5 * iqr_x

    return lower_x,upper_x

def get_outlier_points(lp,up,data):
    lower_points= (data < lp).sum()
    upper_points= (data > up).sum()
    return lower_points,upper_points




for i in numerical_columns.columns:
    print("==========================")
    lower_x,upper_x=calculate_outliers(train[i])
    lp,up=get_outlier_points(lower_x,upper_x,train[i])

    print(f"Feature Name : {i}")
    print(f"Lower Threshold Points : {lp}")
    print(f"Upper Threshold Points : {up}")
