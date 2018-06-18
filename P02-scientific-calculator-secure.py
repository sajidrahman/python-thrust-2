'''
Created on May 21, 2018

@author: sajid
'''
from math import *
from pip._vendor.distlib.compat import raw_input
import sys


   # make all math functions available
# 
# print("1. sin(x)*sin(x) + cos(x)*cos(x)")
# print("2. 2*sin(x)+1")
# print("3. 1 - 2*sin(x)*sin(x)")
# print("4. 2*tan(x)/(1 - tan(x)*tan(x))")
# print("Press the number corresponding to a formula to execute it."+
# "Or add a formula by pressing 'n' ")
# formula = "sin(x)*sin(x) + cos(x)*cos(x)"
# x = eval("3.14")
# result = eval(formula)
# print ('%s for x=%g yields %g' % (formula, x, result))
print ("*** Welcome to the Python Calculator ***")
expresssion_list = []
while True:
   expr = raw_input("Enter a trigonometric expression or 'quit': ")
   
   if str(expr) == "quit":
       if not len(expresssion_list)==0:
           y = raw_input("Save expressions in a text file? Press ‘s’ to save or any other key to discard and exit")
           if str(y) == 's':
               with open("trig_expressions.txt", "a+") as file:
                   for expr in expresssion_list:
                       file.write("{}\n".format(expr))
               print("Expressions saved successfully.") 

       sys.exit("You've ended the Python Calculator")
   else:
       x = raw_input("Enter argument: ") # vulnerable input  __import__("subprocess").getoutput("ls")
       if isinstance(x, float):
           print("Not a decimal type value, please try again!")
           continue
       x = eval(x)
       result = eval(expr) # eval was using the variable x which is in it local 
       #scope to map it with the argument 'x' in trigonometric functions
       expresssion_list.append(expr)
#        print(result)
       print ('%s for x=%g yields %g' % (expr, x, result))
