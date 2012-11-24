myList = [1, 2, 3]
def changeListReference(something):
	"changes the reference of something"
	something.append([1, 2, 3])
	print("Inside:", something)
	return

def changeListValue(something):
	"changes the value of something within the function"
	something = [4, 5, 6]
	print("Inside:", something)
	return

#changeListReference(myList)
#print("Outside:", myList)
#changeListValue(myList)
#print("Outside:", myList)

def f(a, myList=[]):
	print(myList)
	myList.append(a)
	return myList

def f_bad(a, myList=[]):
	myList.append(a)

def f_diff(a, myList=[]):
	myList += [a]
	return myList

def g(a, myList=None):
	if myList is None:
		myList = []
	myList.append(a)
	return myList

def g_bad(a, myList=None):
	if myList is None:
		myList = []
	myList.append(a)

