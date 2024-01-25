
def fizzbuzz(start, finish):
    '''Function takes some range from Start to Finish
Returns which numbers between the range are multiples of 3,5, or both and which numbers contain 3,5, or both or neither'''
    for i in range(start,finish + 1): #creatimg for loop to iterate through every element within some range
        if ("3" in str(i) and "5" in str(i)) or ( i % 3 == 0 and i % 5 == 0): #If the number 3 AND 5 shows up within the number OR the number is a multiple of 3 AND 5, print fizzbuzz
            print("fizzbuzz")
        elif "5" in str(i) and (i % 3 == 0):  #Making sure that each element is checked for both 5 in string and whether it is a multiple of 3
            print("fizzbuzz")
        elif "3" in str(i) and (i % 5 == 0): #Vice versa from line above^
            print("fizzbuzz")
        elif ("5" in str(i)) or (i % 3 != 0 and i % 5 == 0): # if string has a 5 but is also a multiple of 5 print buzz
            print("buzz")
        elif ("3" in str(i)) or (i % 3 == 0 and i % 5 != 0): #if string has 3 but also multiple of 3 print fizz
            print("fizz")
        elif i % 3 != 0 and i % 5 != 0:
            print(i)

fizzbuzz(1,15)