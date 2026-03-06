statement 1 : the cat sat on car -> noun, verb, objects
where did cat sit or the cat sat on ?


the cat that chased a mouse which did steal the cheese was trying to sit on the car - ? who sat -> rat as well as cat -> car was getting sat on by cat or rat

-> Self - Attention : 
st 1 : "The cat sat on a car"
Q = "the cat sat on a car" -> P("the") = 5 times ; P("cat") = 5 times ; P("sat") = 5 times ; P("on") = times ; P("car") = 5 times
K = "the"
Value = [0.01, 0.02, 0.06, 0.04, 0.15]
target = cat
predicted = car
check -> F
error = -log(p) -> p = conditional probability = P("cat"/"the") ; P("sat"/"the") ; P("on"/"the") ; P("a"/"the") ; P("car"/"the")
updated value = [0.001, 0.09, 0.005, 0.007, 0.02] = [0.1, 9, 0.5, 0.7, 2]


Q = "the cat sat on a car"
K = "the"
Value = [0.001, 0.09, 0.005, 0.007, 0.02]
target = cat
predicted = cat
check -> T
