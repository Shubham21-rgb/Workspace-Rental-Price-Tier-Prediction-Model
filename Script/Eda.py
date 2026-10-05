# Descriptive Statistics
columns=numerical_columns.columns.tolist()
train[columns].describe().T


#Checking uniqiue values
for columns in train.columns:
    print("======================")
    print(f"Column Name of Traning Data {columns} : {train[columns].nunique()}")

#Space_id is basically a identifier
#Facilities also has a good no of unique values which means the values are diverse
#operator_ref also has a good no of unqiue values



#Checking empty values
nan_column_fields= list()
for miss in train.columns :
    print(f"Missing Value Count of : {miss} features : {train[miss].isna().sum()}")
    if train[miss].isna().sum() > 0:
        nan_column_fields.append(miss)
print(f"Columns having empty values are : {nan_column_fields}")


# Using IQR method

q1_x,q3_x=train['operator_platform_age_years'].quantile(0.25) , train['operator_platform_age_years'].quantile(0.75)

iqr_x=q3_x - q1_x

lower_x,upper_x= q1_x - 1.5 * iqr_x, q3_x + 1.5 * iqr_x

print(lower_x)
print(upper_x)

lower_points= (train['operator_platform_age_years'] < lower_x).sum()
upper_points= (train['operator_platform_age_years'] > upper_x).sum()
print(f"Low outliers : {lower_points}")
print(f"High outliers : {upper_points}")


