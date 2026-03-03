out_loop = 0
in_loop = 0
for i in range(0,10):# -> this is what epoch looks like or does ; just a fancy variable name for a loop
    out_loop = out_loop+1 # -> this runs 1000 times
    for j in range(0,10): #j = 0,1,2,3,4,5,6,7,8,9 = 10 times
        in_loop = in_loop+1 # -> this runs 1000*1000
        print(f"value of is i is {i} and value of j is {j}")
        print(f"out loop : {out_loop} and in loop : {in_loop}")


