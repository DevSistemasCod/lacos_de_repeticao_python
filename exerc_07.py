dividendo = int(input("Informe o primeiro número: "))

divisor = 2
resto = 0

while dividendo > 1:
    resto = dividendo % divisor
    
    if resto == 0:
        print(divisor)
        dividendo =  dividendo / divisor
    else:
        divisor = divisor + 1
