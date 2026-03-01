single neuron prediction : 
training data : 
input -> output :
1->2
2->4
3->6
4->8 #testing

Neuron Formula : prediciton = (weight*input)+bias
error : prediction - target
dw formula : dw = rate of change of weight = error * input
new weight = old weight - learning rate * dw
db = error 
new bias = old bias - learning rate * db 

weight = 0
bias = 0
learning rate = 0.10

def check():
prediction = target ? - T/F

# training
Phase 1 : 
input = 1
target = 2
prediction = (0*1)+0 = 0
check : F
error = prediction - target = -2
update weight 
dw = rate of change of weight = error * input
dw = -2 * 1 = -2
new weight = old weight - learning rate * dw
new weight = 0 - 0.10*-2 = 0.20 = 0.2
bias :
db = error = -2
new bias = old bias - learning rate * db 
new bias = 0 - 0.10*-2 = 0.20 = 0.2

phase 2 : 
weight = 0.2
bias = 0.2
input = 2
output = 4 <- target
prediction = (weight*input) + bias
prediction = 0.20*2 + 0.20 = 0.6
check ? - F
error = prediction - target = 0.6 - 4 = -3.4

update weight  :
dw = -3.4 * 2 = -6.8
new weight = old weight - learning rate * dw
new weight = 0.2 - 0.10 * -6.8 = 0.88

update bias :
db = error 
db = -3.4
new bias = old bias - learning rate * db
new bias = 0.2 - 0.10 * -3.4 = 0.54

phase 3 : 
weight = 0.88
bias = 0.54
input = 3
output = 6 <- target

prediction = 0.88*3 + 0.54 = 3.18
check ? ->  F
error = 3.18 - 6  = -2.82

update weight : 
dw = -2.82 * 3 = -8.46
new weight = 0.88 - 0.10*-8.46 = 1.726

update bias : 
db = -2.82
new bias = 0.54 - 0.10*-2.82 = 0.822

# testing : 
input = 4
weight = 1.726
bias = 0.822

prediction = weight*input + bias 
prediction = 1.726*4 + 0.822 = 7.726

