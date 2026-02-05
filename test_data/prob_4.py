import numpy as np
def like(observations, prob) : 
    em_l = [] #em_l = [0.8,0.8, 0.2, 0.8
    for ele in observations : 
        if ele == True :
            em_l.append(prob)
        else : 
            em_l.append(1-prob)
    multipy = 1
    for i in em_l : 
        multipy = multipy * i
    return multipy

observations = [True, True, False, True] #asume True is favoured condition
print("like (prob = 0.8) : ", like(observations, 0.8))
print("like (prob = 0.2) : ", like(observations, 0.2))


#0 = False
#1 = True

#Q - What would be the cost of a car, which has 4 air bags, and is rated at least 4 star safety, it should be a two wheeler and ..... 