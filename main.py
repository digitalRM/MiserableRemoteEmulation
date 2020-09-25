    # loops


number = 0   
   

for i in range(3):
    number += 1
    print(number)

number = 0

while number <5:
    number += 1
    print(f"number is {number}")

    if number % 2 == 0:
        print(f"{number} is even") 
    elif number % 2 != 0:
        print (f"{number} is odd")
    else:
        print("Number is 0 or not 1-5.")