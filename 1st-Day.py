print("enter 1: for add and 2: for sub and 3: for multiply and 4: for divide")
ch = int(input("please enter choice  number: "))
if ch == 1:
  add1 = int(input("please enter if you first number:"))
  add2 = int(input("please enter if you second number:"))
  a = add1 + add2
  print(a)
elif ch==2:
  sub1 = int(input("please enter if you first number:"))
  sub2 = int(input("please enter if you second number"))
  b = sub1 - sub2
  print(b)
elif ch==3:
  mul1 = int(input("please enter if you first number:"))
  mul2= int(input("please enter if you second number:"))
  c = mul1 * mul2
  print(c)
elif ch==4:
  div1 = int(input("please enter if you first number:"))
  div2 = int(input("please enter if you second number:"))
  b = div1 // div2
  print(b)
else:
  print("out of range")