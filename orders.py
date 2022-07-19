from multiprocessing import connection
import csv
import pickle
import pymysql

#orders  []

#orders.append({
  #  "customer_name": "Sam",
  #  "customer_adress": "90 George Road, BIRMINGHAM, B16 9UH",
 #   "customer_phone": "07544678051",
 #   "courier": 1,
    #"status": order_status_options[0]
#})

def order_id(order_list):
    for i in range(len(order_list)):
        print(f"{i} {order_list[i]}")
    print(f"{i} {order_list[i]}")

def print_orders():
   # for i in range(0, len(orders)):

     #   print(orders[i])

#def add_order():
    order_name = input("Please enter your name: ")
    address = input("Please enter your address: ")
    email_address = input("Please enter your email: ")
    phone = input("Please enter your phone number: ")
    courier = input("Please enter the courier: ")
    product_id = input("please select the product id: ")
    #new_order = {"Name": name, "Phone": phone, "Email_address": email_address, "Address": address, "Courier": courier,}
    #orders.append(new_order)
    #add_order(orders)
   # print(orders)
    
    number = int(input("length of list:"))
    for i in range(number):
        new_order = input(
            "Please enter the new order you want to add to the order list:")
   # orders.append(new_order)

def remove_order(order_list):
    to_remove = input("Please enter the order you want to remove from order list: ")
    if to_remove in order_list:
        print("This order has been removed")
        #orders.remove(to_remove)
    else:
        print("This order is not in the list")

#def update_order(order_list):#
    #for i in range(len(order_list)):
    #    print(f"{i} {order_list[i]}")
   # update = input("Please enter the id of the order you want to update")
   # update_two = input("Please enter what you would like to update the order with")
    #order_list[int(update)] = update_two


#def load_csv_data():
 #   list = []
 #   with open("orders.csv", 'r') as file:
#        csv_file = csv.DictReader(file)
#        for row in csv_file:
  #          list.append(row)
    #    return list

#def load_order_list():
 #   with open('orders.txt', 'r') as file:
  #      new_file = file.read().splitlines()
   #     return new_file

#order_list = load_order_list()

#def save_order(list):
 #   with open('orders.txt', 'w') as file:
  #      for item in list:
   #         file.write(f"{item}\n")

#def load_data_test():
 #   with open("orders.txt", "r") as data:
  #      new_file = data.read().splitlines()
   #     return new_file

#def save_data_test(order_list):
 #   with open("orders.txt", "w") as data:
  #      for items in order_list:
   #         data.write(f"{items}\n")

#def load_update_order_status():
 #   with open('order status.txt', 'r') as file:
  #      new_file = file.read().splitlines()
   #     return new_file
#orderStatus = load_update_order_status()

#def save_order_status(list):
 #   with open('order status.txt', 'w') as file:
  #      for item in list:
   #         file.write(f"{item}\n")

#save_order_status(orderStatus)

def orders_menu():
    print("[0] Main menu")
    print("[1] Print orders")
    print("[2] Create/Add orders")
    print("[3] Update order")
    print("[4] Delete a order")

#print(load_csv_data())

def show_orders_menu():
    orders_menu()
    option = int(input("Enter your option: "))
    while option != 0:
        if option == 1:
            get_from_database()
            print("Please see the selection of orders")
    # carry out option 1
        elif option == 2:
           new_order() 
    # carry out option 2
        elif option == 3:
            update_order ()
    # carry out option 3
        elif option == 4:
            remove_order() 
    # carry out option 4   
        else:
            print("Invalid Option")
        orders_menu()
        option = int(input("Enter your option: "))

#orders_list = load_csv_data()

# open orders.csv and read as string
#with open("orders.csv", 'r') as file:
 #   reader = csv.reader(file, delimiter=',')
  #  for row in reader:
   #     print(row)

# open orders.csv and read as dict
#with open("orders.csv", 'r') as file:
   # csv_file = csv.DictReader(file)
   # for row in csv_file:
    #    print(row)
        
#def order_items():
   # order_name = input("Please select the order name: ")
  #  address = input("Please select your address: ")
   # email_address = input("Please select your email address: ")
  #  phone = input("Please select your phone number: ")
  #  courier = input("Please select your courier: ")
  #  product_id = input("Please select the product id: ")
  #  order_status_options = input("Please select the order status: ")
  #  info_dict = {"order name": order_name, "address": address, "email address": email_address, "phone": phone, "courier": courier, "product id": product_id, "order status options": order_status_options}
  #  order_items.append(info_dict)
    
   # with open("orders.csv", "w+", newline = "") as file:
      #  fieldnames = ["order name", "address", "email address", "phone" "courier", "product_id", "order status options"]
     #   writer = csv.DictWriter(file, delimiter = ",", fieldnames = fieldnames)
     #   writer.writeheader()
     #   writer.writerows(order_items)

def connect_to_database():
    return pymysql.connect(host="localhost", user="root", password="password", database="test1")
    
def get_from_database():
  
    connection = connect_to_database()
    cursor = connection.cursor();
    cursor.execute(\
    """select * from orders
    """)
    data_lists = cursor.fetchall()
    cursor.close()
    connection.close()  
    print (data_lists)

get_from_database()

def new_order():
    order_name = input("Enter Name: ")
    order_address = input("Enter Address: ")
    order_email_address = input("Enter Email Address: ")
    order_phone_number = input("Enter Phone Number: ")
    courier = input("Enter Courier: ")
    product_id = input("Enter Product ID: ")
    order_status_options = input("Enter Order Status: ")

    add_to_database (order_name, order_address, order_email_address, order_phone_number, courier, product_id, order_status_options)

def add_to_database (order_name, order_address, order_email_address, order_phone_number, courier, product_id, order_status_options):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute (\
           f""" INSERT INTO orders (order_name, order_address, order_email_address, order_phone_number, courier, product_id, order_status_options)
           VALUES (%s, %s, %s, %s, %s, %s, %s)
          """,[order_name, order_address, order_email_address, order_phone_number, courier, product_id, order_status_options])
    connection.commit()
    cursor.close()
    connection.close()

def update_order ():  
    order_name = input ("Please enter order name: ")
    order_status_options = input ("Please enter the order_status: ")
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute (\
           f""" UPDATE orders set order_status_options = %s where order_name = %s
           """,[order_status_options, order_name])
    connection.commit()
    cursor.close()
    connection.close() 