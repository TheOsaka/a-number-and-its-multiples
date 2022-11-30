i=1
number=int(input("Enter a number between one and ten: "))
while i<=10:
    if 1<=number<=10:
        print(f"{number} x {i}= {number * i}")
        i=i+1
    else:
        print("Check the number you wrote")
        break