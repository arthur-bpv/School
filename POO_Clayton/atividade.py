numb = int(input('Digite: '))
binary = ''
adc = 0
quotient = numb

while quotient > 0:
    adc = quotient % 2
    quotient = quotient // 2
    binary += str(adc)

binary = binary[::-1]
print(binary)
