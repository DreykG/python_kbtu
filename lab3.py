def volume(r):
    v=round(float((4*r**3)/3),1)
    print("Volume with 'п' = " + str(v) + "п")

r = float(input("Input radius:\n"))
volume(r)