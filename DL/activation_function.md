input -> output : 
1 -> 2
2 -> 1
3 -> 2


new weight = old weight - learning rate*dw
dw = error * input
new bias = old bias - learning rate * db
db = error
prediction = weight * input + bias
error = prediction - target

epoch 1 : 
weights =  0
bias = 0
phase 1 : 
prediction = 0
check -> F
error = -2
dw = -2
new weight = 0.2
db = -2
new bias = 0.2

phase 2 : 
in = 2
op = 1
weight = 0.2
bisa = 0.2
prediction = 0.6
error = -0.4
dw = -0.8
new weight = 0.28
db = -0.4
new bias = 0.24

phase 3 : 
input = 3
op = 2
weight = 0.28
bias = 0.24

prediction = 1.08
error = -0.92
dw = -2.76
new weight = 0.556
db = -0.92
bias = 0.332

in -> predicted op
1 -> 0.556*1 + 0.332 = 0.888
2 -> 0.556*2 + 0.332 = 1.444
3 -> 0.556*3 + 0.332 = 2.000
4 -> 0.556*4 + 0.332 = ~2.5

Epoch 2 : (without activation function)
completed all the 3 phases 
1 -> pred > 0.888
2 -> pred < 1.444
3 -> pred > 2.000
4 -> pred < ~2.5

Epoch 2 : (with activation function)
activation function = ReLU(x)
{
    ReLU(x) = max(0,x)
    ReLU(5) = max(0,5) = 5
    ReLU (-33) = max(0,-33) = 0
}

success in 2 cases > success in 2 cases and failure in 2 cases
phase 1 : 
weight = 0.556
bias = 0.332
input : 1
target : 2
prediction = 0.888
activation function = ReLU(prediction)
ReLU(0.888) = max(0,0.888) = 0.888
Check -> F
error = precition - target = 









# new : 
input -> output : 
1 -> 0
2 -> 1
3 -> 0

pred(1) = 0.42
pred(2) = 0.79
pred(3) = 0.56
