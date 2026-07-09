#Restaurant

#Food Menu
def food_menu():
    print("-------MENU-------")
    for item in menu:
        print(f"{item} = {menu[item]}")

#Food Order
def order_food():
    item=input("Enter the Item Name :")
    if item in menu:
        qty=int(input("Enter the Quantity :"))
        order_list.append([item,qty])
        print(f"\n{order_list}\nYour order is placed..Thank you")
    else:
        print("\nItem not available")

#View Bill
def view_bill():
    if (len(order_list)==0):
        print("Item's Not Added")

    total_bill=0
    print("-------BILL-------")
    print("Item\tQty\tPrice\tAmount")
    for i in order_list:
        item=i[0]
        qty=i[1]
        amount=menu[item]*qty
        total_bill+=amount
        print(f"{item}\t{qty}\t{menu[item]}\t{amount}")
    print("\n-------TOTAL BILL-------")
    print(f"TOTAL BILL  =  {total_bill}")

#Exit 
def exit_program():
    print("Thank You")

#Dictionaries - menu item
menu={
        "Pizza":250,
        "Burger":150,
        "Coffee":80,
        "Pasta":200
    }
order_list=[]
while(True):
    print("\n-------Restaurant-------")
    option=int(input("Select the Option \nView menu - 1\nOrder Food - 2\nView Bill - 3\nExit - 4\nEnter your option: "));
    print()

    #Function calling
    if(option==1):
        food_menu()
    elif(option==2):
        order_food()
    elif(option==3):
        view_bill()
    elif(option==4):
        exit_program()
        break
    else:
        print("Inavlid")