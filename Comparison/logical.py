"""

condition1: Purchase more than 1000 taka

condition 2 : Customer age must be less than 50 years

condition 3: Customer Gender should be male
condition 4: payment with cash will get 10% discount payment with card will get 20% discount


"""

purchase =int( input("purchase= "))

age =int(input("age= "))

gender = input("gender= ")
payment = input("payment= ")

if purchase >1000 and age <50 :
    print("eligible for discount")
    if payment == "cash":
        print("10% discount")
        print(purchase-purchase*10/100)
    elif payment == "card":
        print("20% discount")
        print(purchase-purchase*20/100)
    if gender=="male":
         print("will get a free chocolate")
    elif gender== "female":
         print("get a pen")

else:
    print("Not eligible")