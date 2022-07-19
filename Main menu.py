import products
import couriers
import orders 

def main_menu():
    print("Welcome to Sufyan's cafe")
    print("******Main Menu*******")
    print("[0] Exit main menu and exit app")
    print("[1] product menu")
    print("[2] courier menu")
    print("[3] order menu")

main_menu()
option = int(input("Enter your option: "))
while option != 0:
    # carry out option 0
    if option == 1:
        products.show_products_menu()
        # carry out option 1
        print("Product menu has been executed")
    elif option == 2:
        couriers.show_couriers_menu()
        # carry out option 2
        print("Courier menu has been executed")
    elif option == 3:
        orders.show_orders_menu()
        # carry out option 3
        print("Order menu has been executed")
    else:
        print("Invalid Option")
    main_menu()
    option = int(input("enter your option: "))

print("Thank you for visiting Sufyan's Cafe. Goodbye hope to see you again")

products.save_data_test(products.products_list) 
couriers.save_data_test(couriers.couriers_list)
orders.save_data_test(orders.orders_list)