# with open('a.txt','r') as f:
#     line = f.readlines()
#     with open('b.txt','r') as f2:
#         line2 = f2.readlines()
#     overlaping_numbers = []
#     for i in line:
#         if i in line2:
#             overlaping_numbers.append(i)
    
#     print("OVERLAPING NUMBERS ARE : ",overlaping_numbers)

def filetolistofints(filename):
	list_to_return = []
	with open(filename) as f:
		line = f.readline()
		while line:
			list_to_return.append(int(line))
			line = f.readline()
	return list_to_return

primeslist = filetolistofints('a.txt')
happieslist = filetolistofints('b.txt')

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)