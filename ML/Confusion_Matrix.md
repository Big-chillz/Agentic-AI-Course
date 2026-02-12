Category,Legs

Cat1,yes
Fish1,No
Cat2,Yes - Test
Dog1,Yes
Tiger1,Yes
Fish2,No - Test
Snake1,No - Test
Dog2,Yes
Snake2,No 
Fish3,No

train_test_split -> test_size = 0.3

Actual Values : 
Cat2,yes
Fish2,No
Snake1,No

Test or Predicted Values :
Cat2,Yes
Fish2,Yes
Snake1, No

- When you fill the matrix fill it by or with respect model performance, but when you are looking or comparing look with actual perspective

- What is model doing 

P - Actual : 1 (Cat2)
P - Predicted - 2 (Fish2 and Snake1)
N - Actual - 2 (Fish2 and Snake1)
N - predicted - 1 (Snake1)

TP : first check P - actual = 1 -> Cat2 - check what modelis telling = T(yes) = 1
FP : first check N - actual = 2 -> Fish2 and Snake 1 - check what model is telling : Fish2 a yes(whereas model is telling a NO), Snake1 is a NO)model is also telling a no) = 1
FN : first check P - actual = 1 -> Cat2 - check what is model telling -> Yes (so no false yes) = 0
TN : first check N - actual = 2 -> Fish2 and Snake1 - check what is model telling : Fish2 a yes (whereas model is telling no) , snake1 is a no and actual is also no - 1



actual :
a,p
b,n
c,p
d,n
e,p
f,p
g,n

predicted : 
a,p
b,n
c,n
d,p
e,p
f,n
g,p

TP : actual p - (a,c,e,f) : predicted p - (a,d,e,g) : {a,e} - 2
FP : actual N - (b,d,g) : predicted p - (a,d,e,g) : {d,g} - 2
FN : actual P - (a,c,e,f) : predicted n - (b,c,f) : {c,f} - 2
TN : actual N - (b,d,g) : predicted n - (b,c,f) : {b} - 1

recall = TP / (TP + FN)
Precision = TP / (TP + FP)

F1 score = 2 x (Precision x Recall) / (Precision + Recall)