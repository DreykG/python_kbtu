def transfer(degree):
    return (float(5/9)*(int(degree) - 32))

f = int(input("How much degree by Faranheit?"))
print(round(transfer(f),1), "by Celcius")