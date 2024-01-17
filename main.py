
# Online Python - IDE, Editor, Compiler, Interpreter

nterms = int(input("How many terms of a number do you want to print? "))
# Program to display the Fibonacci sequence up to n-th term

# first two terms
a, b = 0, 1
sum = 0

# check if the number of terms is valid
if nterms <= 0:
   print (int(input("Please enter a positive integer")))
   
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(a)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while sum < nterms:
       print(a)
       nth = a + b
       # update values
       a = b
       b = nth
       sum += 1
     
