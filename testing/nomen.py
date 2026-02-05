import pandas as pd
import numpy as np
import json
"""  
# read data from a csv file
df = pd.read_csv("D:\\Agentic_Course\\testing\\data.csv")
print(df)

# write data to a csv file
df["high_value"] = df["spend"] > 2000
df.to_csv("D:\\Agentic_Course\\testing\\data_out.csv", index=False)
"""

# r - read mode , w - write mode , a - append mode, r+ == w+ , a+
content = {
    "file" : "path to file"
}

# writing in json file
#ith open("D:\\Agentic_Course\\testing\\test.json", "a") as f:
#   json.dump(content, f)


# reading from json file
with open("D:\\Agentic_Course\\testing\\test.json", "r") as f:
    data = json.load(f)
    print(data)




try : 
    with open("D:\\Agentic_Course\\testing\\test.json", "r") as f:
        history = json.load(f)
        print(history)
except FileNotFoundError :
    history = []
