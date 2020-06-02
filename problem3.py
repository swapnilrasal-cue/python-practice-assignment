def SortWords(myList):
    # sortedWords = sorted(myList)
    print("-" * 50)
    print("Words After Sorting :")
    print(sorted(myList))
    print("-" * 50)

user_input = str(input("Enter comma separated Words to Sort : "))
print("-" * 50)
print("Words Before Sorting :")
user_list = user_input.split (",")
print(user_list)
print("-" * 50)
SortWords(user_list)