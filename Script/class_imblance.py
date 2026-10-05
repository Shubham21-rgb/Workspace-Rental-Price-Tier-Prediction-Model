train['price_tier'].value_counts() # No class Imbalance
#If class imbalance was there what metric we use ? --> F1 score,Accuracy Does not give the correctness as compared to F1
#1 --> 30k 2--> 60K . Here the Model will take biased decision 
#In such cases what we can do ?
#We will use resampling to increase the training set of 1 to 60k


train['operator_platform_age_years'].value_counts().sort_values(ascending=True)


print(train['geo_lat'].value_counts())


#The maximum value of lat is 90
print(train[train['geo_lat'].abs() > 90]['geo_lat'].count()) # Higly Suspicious
print(train[train['geo_lon'].abs() > 180]['geo_lon'].count()) 
