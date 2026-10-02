#Today Topic: Problem Statement , some basic functions of pandas and Sklearn.
#Orientation of Notebook

#Work Flow -->   EDA --> Preprocessing --> Feature Engineering --> Model Building(HPT, Model Comparison) --> Error Analysis


# DATA LOADING
train=pd.read_csv('/kaggle/input/competitions/workstation-rental-price-tier-prediction/kaggle_ready_dataset/train.csv')
test=pd.read_csv('/kaggle/input/competitions/workstation-rental-price-tier-prediction/kaggle_ready_dataset/test.csv')
sub=pd.read_csv('/kaggle/input/competitions/workstation-rental-price-tier-prediction/kaggle_ready_dataset/sample_submission.csv')



## To check the shape of a file means no of observation(Rows) vs features(Columns)
print("=============================================")
print("============= Files Shapes ==================")
print(train.shape)
print(test.shape)
print(sub.shape)
print("==================END========================")


train.info()
# sparse feature and another is dense feature 


numerical_columns= train.select_dtypes(include=['int64','float64']) # Hence it becomes numerical columns
categorical_columns= train.select_dtypes(include=['object']) # This is categorical columns





print("++++++++++++++++++++++++++++")
print("===== Numerical Columns ======")
print(len(numerical_columns.columns))
print("===== Categorical Columns ======")
print(len(categorical_columns.columns))
