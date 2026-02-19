"""
As a user

1. View the Menu
2. Add to Cart
3. Order Summary
4. Cash
# 5. Coupons 
6. Delivery Type ( Serve and Collect)
    6.1 -> Serve -> Enter the table tag number
    6.2 -> Collect -> Printing Your Receipt
"""


items = [
    {
        "item_no": 1,
        "item_name" : "Ice Tea",
        "item_price" : 99
    },
    {
        "item_no": 2,
        "item_name" : "Fanta Float",
        "item_price" : 89
    },
    {
        "item_no": 3,
        "item_name" : "Coke Float",
        "item_price" : 79
    },
    {
        "item_no": 4,
        "item_name" : "Cofee",
        "item_price" : 199
    }
]


class McDonalds:

    def show_menu(self):
        print("List of Items")
        print(f"| Number | Name | Price |")
        for item in items:
            print(f"| {item.get("item_no")} | {item.get("item_name")} | ₹{item.get("item_price")} |")

cart = [] 
discount = [
    {
        "discount_coupon" : "NEWYEAR10",
        "discount" : 10
    }
]
order_number = 1000
while True:
    print("""
Welcome to McDonald's 
Please select your options:
        1. View Menu
        2. Add to Cart
        3. Order Summary
        4. Proceed Pay
""")
    user_input = int(input("Enter your Input: "))
    mcd1 = McDonalds()
    if user_input == 1:
        mcd1.show_menu()
    elif user_input == 2:
        user_food_option = int(input("Enter the item you want eat:"))
        cart.append(user_food_option)
    elif user_input == 3:
        total_amount = 0
        for item in items:
            if item["item_no"] in cart:
                print(f"{item['item_name']} | {item['item_price']}")
                total_amount += item['item_price']
        print("Total Amount You Should Pay:", total_amount)
    elif user_input == 4:
        user_have_coupon = input("Do you have a coupon Y/N:")
        if user_have_coupon.lower() == "n":
            print("Amount Payable :", total_amount)
            print("1. Cash")
            payment_option = int(input("Enter Your Payment Options:"))
            if payment_option == 1:
                print("Cash Received")
                total_amount = 0
                cart = []
                print("Order Number:", order_number)
                order_number += 1
            else:
                print("Invalid Option")
        elif user_have_coupon.lower() == "y":
            user_coupon = input("Enter your discount coupon")
            discount_percent = 0
            for i in discount:
                if i['discount_coupon'] == user_coupon:
                    discount_percent = i['discount']
                    break;
            
            print("Amount Payable :", total_amount)
            print("Discounted Price:", total_amount - (total_amount / 100)* discount_percent)
            print("1. Cash")
            payment_option = int(input("Enter Your Payment Options:"))
            if payment_option == 1:
                print("Cash Received")
                total_amount = 0
                cart = []
                print("Order Number:", order_number)
                order_number += 1
            else:
                print("Invalid Option")
    else:
        print("Invalid Input")