numblist = [int(i) for i in input('Write a list of numbers: ').split()]
print(numblist)

justOneNumb = set(numblist)

# ex 1 ----------------------
most_repeats = None
bigger = 0

for i in justOneNumb:
    cont = numblist.count(i)
    if cont > bigger:
        bigger = cont
        most_repeats = i
#-----------------------------

print(f'the number that repeats the most times is {most_repeats} with {bigger} times') 

# ex 2 ----------------------
appearsOneTime = []

for i in justOneNumb:
    if numblist.count(i) == 1:
        appearsOneTime.append(i)
#-----------------------------
    

print(f'the numbers that appears just one time are {' '.join(map(str, appearsOneTime))}.') 

#ex 2 -------------------------
prime_factor = 0
list_prime = []

for i in justOneNumb:
    for j in range(1, i + 1):
        if i % j == 0:
            prime_factor += 1
    if prime_factor == 2:
        list_prime.append(i)
        prime_factor = 0
    else:
        prime_factor = 0
#-----------------------------

print(list_prime)
print(f'The sum of prime numbers is: {sum(list_prime)}')

