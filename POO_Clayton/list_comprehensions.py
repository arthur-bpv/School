import math

numb = [1, 2, 3, 4, 5]

# #element
# for i in numb:
#     print("---\n",i)
#
# #position
# for i in range(5):
#     print('---\n', numb[i])

# ex1 ----------------------------------

#add the square of each number in the numb list
numb2 = []

# for i in numb:
#     numb2.append(i**2)

# equal v (list comprehension)

numb2 = [i**2 for i in numb]

print('---\n', numb2)

# ex2 ---------------------------------

numb3 = [math.sqrt(i) for i in numb]
# or i ** (1/2)

print('---\n', numb3)

# ex3 ---------------------------------

numb4 = [i for i in numb if i % 2 == 0]

print('---\n', numb4)

# ex4 ---------------------------------

numb = list(range(20))

print([i for i in numb if i % 3 == 0 and i % 5 ==0])
# print if it is divisible by 3 and 5

# ------------------------------------------------------------------------

phrase = 'Hello World'
#
# for l in phrase:
#     print(l)
#
print([l for l in phrase])

# vowels

print([l for l in phrase if l in 'aeiou'])

# ------------------------------------------------------------------------

phrase = "hello big world big world big bigand word word"
cont = 1
for i in phrase:
    if i == " ":
        cont += 1

print(f'The sentence has {cont} words.')

print('The sentence has', [x for x in phrase if x == ' '].count(' ') + 1, 'words.')

phrase = "Good afternoon"
words = phrase.split(' ')
print(len(words))

phrase = '10 20 30'

print(phrase.split())
numbers = [int(i) for i in phrase.split()]

print(numbers)
#
print(max([int(i) for i in input('How old are you and 2 other persons? ').split()]))

print([n**2 for n in[int(i) for i in input('Write five numbers: ').split()]])
