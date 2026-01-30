import pandas as pd

df = pd.read_csv("D:\\Agentic_Course\\test_data\\data.csv")
print(df)


def fun(a,b): #definition of a function
    print("calling from the function")
    print(a+b)

#fun(5,7) # calling a function


#print("\n using info function \n")
#print(df.info())


#print("\n using describe function \n")
#print(df.describe())

print("\n missing values per column \n")
print(df.isnull())

print("\n total per column \n")
print(df.isnull().sum())

print("\n filling the null values \n")
df["age"]=df["age"].fillna(df["age"].mean())
df["spend"]=df["spend"].fillna(0)
print(df)