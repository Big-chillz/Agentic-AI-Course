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

#print("\n missing values per column \n")
#print(df.isnull())

#print("\n total per column \n")
#print(df.isnull().sum())

#print("\n filling the null values \n")
#df["age"]=df["age"].fillna(df["age"].mean())
#df["spend"]=df["spend"].fillna(0)
#print(df)

#print(df[["age", "signup_days"]].quantile([0.15,0.70]))

#df["high_sign_up_days"] = df["signup_days"] > df["signup_days"].quantile(0.50)
#print(df)

#df["low_sign_up_days"] = df["signup_days"] < df["signup_days"].quantile(0.15)
#print(df)
#
#df["lowest_spend"] = df["spend"] < df["spend"].quantile(0.85) #

#df["efficiency"]=(df["high_sign_up_days"])&(df["lowest_spend"])
#print(df)

print("\n")
print(f"Mean of attributes \n: {df.mean(numeric_only=True)}")
print("\n")
print(df.median(numeric_only=True))
print(df.mode(numeric_only=True))
print(df.std(numeric_only=True))
print(df.var(numeric_only=True))
print(df.quantile(0.25, numeric_only=True))