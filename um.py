def fibonacci(x):
    number = 0
    number_plus = 1

    while number_plus <= x:
        if x == number or x == number_plus:
            print("Faz parte")
            return
        
        number, number_plus = number_plus, number + number_plus
    
    print("Não faz parte")

fibonacci(2)