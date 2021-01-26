#here we are printin' divisible BY  5 NOT BY 10..start the coding..
print(" \n ----------------NUMBERS DIVISIBLE BY 5-------------- ")
for n in range(1,201):
  if n % 5 == 0 and n % 10 != 0:
      print(n) 
print("\n -----------END OF THE PROGRAM-------------")