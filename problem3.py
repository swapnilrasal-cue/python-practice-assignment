def SortWords(myList):
    sortedWords = sorted(myList)
    print("-" * 50)
    print("Words After Sorting :")
    print(sortedWords)
    print("-" * 50)

str = str(input("Enter comma separated Words to Sort : "))
print("-" * 50)
print("Words Before Sorting :")
list = str.split (",")
print(list)
print("-" * 50)
SortWords(list)