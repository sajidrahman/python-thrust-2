'''
Created on May 21, 2018

@author: sajid
'''
from math import *
from pip._vendor.distlib.compat import raw_input
import sys

#make a list of safe functions
safe_list = ['math','acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 
 'modf', 'pi', 'pow', 'radians', 'sin','sinh', 'sqrt', 'tan', 'tanh']
#use the list to filter the local namespace
safe_dict = dict([ (k, locals().get(k, None)) for k in safe_list ])
#add any needed builtins back in.
safe_dict['abs'] = abs

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
       safe_dict['x']=x
       x = eval(x)
       try:
           result = eval(expr,{},{"x":x,"sin":sin, "cos":cos, "tan":tan, 
                                  "log":log, "log10":log10, "sqrt":sqrt}) # eval was using the variable x which is in it local scope
           expresssion_list.append(expr)
           print ('%s for x=%g yields %g' % (expr, x, result))
       except:
            print("Illegal input detected, please try with a valid trigonometric expression.")
#        
