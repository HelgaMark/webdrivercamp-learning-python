#!/usr/bin/python3

if __name__=="__main__":
  #ADD YOUR IMPORT HERE
  import calculation
  
  a = 4 #use this variable as a first argument to call a function 
  b = 2 #use this variable as a second argument to call a function
  
  #ADD YOUR CODE HERE
  
  result_add = calculation.add(a,b)
  result_sub = calculation.sub(a,b)
  result_mul = calculation.mul(a,b)
  result_div = calculation.div(a,b)

  print(f"{a} + {b} = {result_add}")
  print(f"{a} - {b} = {result_sub}")
  print(f"{a} * {b} = {result_mul}")
  print(f"{a} / {b} = {result_div}")
