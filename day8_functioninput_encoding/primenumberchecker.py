def prime_number(number):
    is_prime = True
    for i in range(2,number):
        # print(i)
        if number % i == 0:
            is_prime = False
    

    if is_prime == True: #tapi ini gausah dikasih ==True juga bisa, karena syarat if kerja kan asalkan True
        print("this is a prime number")
    else:
        print("This is NOT a prime number")

n = int(input("Whats your number:"))

prime_number(number = n)
