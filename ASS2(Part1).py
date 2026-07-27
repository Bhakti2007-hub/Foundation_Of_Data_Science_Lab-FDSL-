import pandas as pd
import numpy as np

# Import data in dataframe (dataframe = rows+column)
#import CSV file
df=pd.read_csv("C:/Users/BHAKTI/OneDrive/Desktop/SCOE/MLL/WineQT.csv")

#print 1st five record 
print(df.head())
print("---------------------------------------------------------------------------------------------------------")

#print 2nd Five record
print(df.tail())
print("---------------------------------------------------------------------------------------------------------")


#print all info 
print(df.info())
print("---------------------------------------------------------------------------------------------------------")


#describe the data
print(df.describe())
print("---------------------------------------------------------------------------------------------------------")


#print type of dataset
print("Type: ",type(df))
print("---------------------------------------------------------------------------------------------------------")


#print the columns 
print("Columns: ",list(df.columns))
print("---------------------------------------------------------------------------------------------------------")


#print data using Index
print("Index ",df.index.tolist())
print("---------------------------------------------------------------------------------------------------------")


#print shape of dataset
print("Shape: ",df.shape)
print("---------------------------------------------------------------------------------------------------------")

#print location wise data
print("Print Data With Labels")
print(df.loc[0:2,["fixed acidity"	,"volatile acidity",	"citric acid",	"residual sugar"]])
print("---------------------------------------------------------------------------------------------------------")

#print index wise location 
print("Print data with index")
print(df.iloc[0:3,0:3])
print("---------------------------------------------------------------------------------------------------------")

#Apply filter giving specific command
print("Print Data where Fixed acidity is 7.8")
print(df[df["fixed acidity"]==7.8])
print("---------------------------------------------------------------------------------------------------------")
