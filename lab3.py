def count(legs,heads):
    rab = (legs - 2*heads)/2
    chick = heads - rab
    print("Number of rabbit =", rab)
    print("Number of chickens =", chick)
    
legs = int(input("input legs:\n"))
heads = int(input("input heads:\n"))
count(legs,heads)



# legs = 94
# head = 35

# 4*r + 2*c = 94
# r+c=35
# c = 35-r
# 4r +70-2r=94
# 2r=24
# r=12
# c=23
# 4*12 + 2*23 = 48+46