while True:

    import time
    print("calculator menu")
    time.sleep(1)
    print("the operation for addition in +")
    time.sleep(1)
    print("the operation for sustraction is -")
    time.sleep(1)
    print("the operation for multiplication is *")
    time.sleep(1)
    print("the operation for devision is /")
    time.sleep(1)
    print("the operation for reste devision is %")

    n1 =int(input("enter the first number: "))

    operation =input("enter the opertion (+|-|*|/|%): ")

    n2 =int(input("enter the second number: "))

    if operation == "+" :
       print("the result is ",n1 + n2)
    elif operation =="-" :
       print("the result is ",n1 - n2)
    elif operation == "/" :
       if n2 == 0:
          print("imposible to devise 0")
       else:
          print("the result is",n1/n2)
    elif operation == "*" :
       print("the result is ",n1 * n2)  

    if operation == "%" :
       print("the result is ",n1 % n2)

    reponse =(input("do yoy wanna continue (y/n): "))
    if reponse == "n":
       break




