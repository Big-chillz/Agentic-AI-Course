y=mx+c
m = slope
c = intercept

25,50000
30,70000
x = age
y = salary
x1 = 25
y1 = 50k
x2 = 30
y2 = 70k
x3 = 55
y3 = ?

a = age
b = exp
c = salary

a,b = lablled input data
c = labelled op data

m = 5
c = 0
yp = m(x) + c
yp1 = 5(25)+0= 125k (predicted)

loss = predicted(yp) - actual(y) = 125 - 50 = 75 

loss = 0 -> prediction and actual will be 


loss > 0 -> predicted > actual -> decrease m -> m = 4
yp1 = 4(25) + 0 = 100

loss = predicted(yp) - actual(y) = 100 - 50 = 50
loss > 0 -> predicted > actual -> decrease m -> m = 0.5

yp1 = 0.5(25) + 0 = 12.25
loss = predicted(yp) - actual = 12.25 - 50 = -37.75
loss < 0 -> predicted < actual -> increase m -> m = 1

yp1 = 1(25)+0 = 25
loss = predicted (yp) - actual (y) = 25 - 50 = -25
loss < 0 -> predicted < actual -> increase m -> m = 10

yp1 = 10(25) + 0 = 250
loss = predicted - actual = 250 - 50 = 200
loss > 0 -> predicted > actual -> decrease m -> 2

yp1 = 2(25) + 0 = 50
loss = predicted - actual = 50-50 = 0
loss = 0 -> pred = actual -> no need to change m value
gradient descent - to minimize loss





a = 1,2,3,4,10 (input 1)
b = 2,3,5,7,29 (input 2)

o = 3,5,8,11,? (output)

x = 5 
o = 10