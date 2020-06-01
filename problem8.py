n = int(input("\nEnter the Number upto you want to iterate :"))
divisibleBy7 = [i for i in range(0, n) if (i % 7 == 0)]
print('-' * 70)
print('\nThe Numbers Divisible By 7 Are : -\n')
print(divisibleBy7, '\n')
print('-' * 70)