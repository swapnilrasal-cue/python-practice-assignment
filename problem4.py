items = []
num = [x for x in input('\nEnter the Binary Numbers Separated By comma :').split(',')]
print('-' * 70)
print("\nNumbers are : " ,num ,'\n')
print('-' * 70)
for binaryNumber in num:
    # print(binaryNumbers)
    x = int(binaryNumber, 2)
    # print(x)
    if not x%5:
        items.append(binaryNumber)
print("\nNumbers Divisible by 5 :",','.join(items),'\n')
print('-' * 70)