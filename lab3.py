def transfer(gram):
    return (float(gram) * 28.3495231)

gram = float(input("Input count of gramms\n"))
print("Count of ounces =",transfer(gram))