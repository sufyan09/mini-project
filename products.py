from multiprocessing import connection
import csv
import pickle
import pymysql

def print_products():
   # for i in range(0, len(products_list)):
    
   #  print(products_list[i])
    
#def add_product():
    number = int(input("length of list:"))
    for i in range(number):
        new_product = input("Please enter the new product you want to add to the product list:")
    #products_list.append(new_product)          

def remove_product(p_list):
    to_remove = input("Please enter the product you want to remove from product list: ")
    if to_remove in p_list: 
        print("This product has been removed")    
        p_list.remove(to_remove)       
    else: 
        print("This product is not in the list")  

def update_product(p_list):
    for i in range(len(p_list)):
        print(f"{i} {p_list[i]}")
    update = input("Please enter the number of the product  you want to update")
    update_two = input("Please enter the name you would like to update product to")
    p_list[int(update)] = update_two      

#def load_products_list():
    #with open('products.txt', 'r') as file:
        #new_file = file.read().splitlines()
        #return new_file
#products_list = load_products_list()

#def save_product(list):
    #with open('products.txt', 'w') as file:
        #for item in list:
            #file.write(f"{item}\n")

#def load_data_test():
    #with open("products.txt", "r") as data:
        #new_file = data.read().splitlines()
        #return new_file

#def save_data_test(p_list):
    #with open("products.txt", "w") as data:
        #for items in p_list:
            #data.write(f"{items}\n")

def product_menu():
 print("[0] Main menu")
 print("[1] Print Products")
 print("[2] Create/Add Products")
 print("[3] Update Products")
 print("[4] Delete a Product")

#def load_csv_data():
    
#    list = []
#    with open("products.csv", 'r') as file:
#        csv_file = csv.DictReader(file)
#        for row in csv_file:
#           list.append(row)
#        return list

#print(load_csv_data())

def show_products_menu():
    product_menu()
    option = int(input("Enter your option: "))
    while option != 0: 
        if option == 1:
            get_from_database()
            print("Please see the selection of products")
    #carry out option 1
        elif option == 2:
            new_product() 
      #carry out option 2
        elif option == 3:
            update_product(connect_to_database)
    #carry out option 3
        elif option == 4: 
            remove_product(connect_to_database)
    # carry out option 4
        else:
            print("Invalid Option")
        product_menu() 
        option = int(input("Enter your option: "))

#products_list = load_csv_data() 

#product_items = []

# open product.csv and read as string
#def load_products():
#    with open("products.csv", 'r') as file:
#        reader = csv.DictReader(file)
#        for row in reader:
#            product_items.append(row)
#load_products()

#def print_products():
#    product_name = input("Please select the products: ")
#    price = float(input("Please select the price: "))
#    info_dict = {"product name": product_name, "price": price}
#    product_items.append(info_dict)

#    with open("products.csv", "w+", newline = "") as file:
#        fieldnames = ["product name", "price"]
#        writer = csv.DictWriter(file, delimiter = ",", fieldnames = fieldnames)
#        writer.writeheader()
#        writer.writerows(product_items)


def connect_to_database():
    return pymysql.connect(host="localhost", user="root", password="password", database="test1")

def get_from_database():
  
    connection = connect_to_database()
    cursor = connection.cursor();
    cursor.execute(\
    """select * from products
    """)
    data_lists = cursor.fetchall()
    cursor.close()
    connection.close()  
    print (data_lists)
    
get_from_database()

def new_product():
    product_name = input("Enter Name: ")
    price = input("Enter price: ")

    add_to_database (product_name, price)

def add_to_database (product_name, price):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute (\
           f""" INSERT INTO products (product_name, price)
           VALUES (%s, %s)
           """,[product_name, price])
    connection.commit() 
    cursor.close()
    connection.close()  