import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.optim as optim

df = pd.read_csv("D:\\Agentic_Course\\DL\\data.csv")
df = df.dropna()  # Drop rows with missing values

X = torch.tensor(df[["age","signup_days"]].values, dtype=torch.float32)

Y = torch.tensor(df["spend"].values, dtype=torch.float32).view(-1,1)

class SimpleNn(nn.Module) : 
    def __init__(self):
        super(SimpleNn,self).__init__()
        self.layer1 = nn.Linear(2,4) # input layer = 2, hidden layer = 4
        self.output = nn.Linear(4,1) # hidden layer = 4, output layer = 1

    def forward(self,x) :
        x = torch.relu(self.layer1(x))
        x = self.output(x)
        return x
    def predict(self,x) :
        with torch.no_grad():
            x = torch.relu(self.layer1(x))
            x = self.output(x)
        return x

model = SimpleNn()    
loss_fn = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)


losses = []

for epoch in range(0,500):
    optimizer.zero_grad()

    predictions = model(X)
    loss = loss_fn(predictions, Y)
    loss.backward()
    optimizer.step()
    losses.append(loss.item())

    if epoch % 50 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item()}")

plt.plot(losses)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training Loss Over Time")
plt.show()  