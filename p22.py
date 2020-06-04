counter_dict = {}

def wordCount():
    with open('abc.txt') as f:
	    line = f.readline()
	    while line:
		    line = line.strip()
		    if line in counter_dict:
			    counter_dict[line] += 1
		    else:
			    counter_dict[line] = 1
		    line = f.readline()
    print(counter_dict)
    
if __name__ == "__main__":
    wordCount()