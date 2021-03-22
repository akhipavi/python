numer = input("enter the number:")
value = 10
while(value<11):
    for value in range(1,11):

        multiply = value*int(numer)
        line = str(value) + "X" + str(numer) + "=" + str(multiply)
        print(line)
