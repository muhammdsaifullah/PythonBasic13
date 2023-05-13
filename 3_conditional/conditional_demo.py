marks = float(input("marks= "))

if marks >= 1 and marks <=39:
    print("grade f")
elif marks>=40 and marks<=49:
    print("grade D")
elif marks >= 50 and marks <= 59:
    print("grade C")
elif marks >= 60 and marks <= 69:
    print("grade B")
elif marks >= 70 and marks <= 79:
    print("grade A-")
elif marks >= 80 and marks <= 89:
    print("grade A")
elif marks>=90 and marks<=100:
    print("grade A+")
else:
    print("Invalid Marks")
