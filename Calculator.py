#variables

a=float(input("enter your 1st number:"))
print("for addition type: +")
print("for subrtaction type: -")
print("for multiplication type: *")
print("for division type: /")
c=str(input("choose your operator:"))
b=float(input("enter your 2nd number:"))

#calculator function

def mycalc():
  if c=="+":
    print("your number is:",a+b)
  elif c=="-":
    print("your number is:",a-b)
  elif c=="/":
    print("your number is:",a*b)
  elif c=="/":
    print("your number is:",a/b)
  elif c=="%":
    print("your number is:",a%b)
  else:
    print("invalid operator")

mycalc()
