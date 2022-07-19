from multiprocessing import connection
import csv
import pickle
import pymysql

def courier_id(couriers_list):
    for i in range(len(couriers_list)):
        print(f"{i} {couriers_list[i]}")

def print_couriers():
    #for i in range(0, len(couriers_list)):
    
        #print(couriers_list[i])
    
#def add_couriers():
    number = int(input("length of list:"))
    for i in range (number):
        new_courier = input("Please enter the new courier you want to add to the courier list:")
    #couriers_list.append(new_courier)

def remove_courier(couriers_list):
    to_remove = input("Please enter the courier you want to remove from courier list: ")
    if to_remove in couriers_list: 
        print("This courier has been removed")    
        couriers_list.remove(to_remove)       
    else: 
        print("This courier is not in the list")  

def update_couriers(couriers_list):
    for i in range(len(couriers_list)):
        print(f"{i} {couriers_list[i]}")
    update = input("Please enter the number of the courier  you want to update")
    update_two = input("Please enter the name you would like to update courier to")
    couriers_list[int(update)] = update_two 
        
#def load_couriers_list():
     #with open('couriers.txt', 'r') as file:
        #new_file = file.read().splitlines()
     #return new_file

#couriers_list = load_couriers_list() 

#def save_couriers(list):
 #   with open('couriers.txt', 'w') as file:
  #      for item in list:
   #         file.write(f"{item}\n")

 #def load_data_test():
   # with open("couriers.txt", "r") as data:
   #  new_file = data.read().splitlines()
   # return new_file

#def save_data_test():
  #  with open("couriers.txt", "w") as data:
    #    for items in couriers_list:
    #        data.write(f"{items}\n")

def couriers_menu():
 print("[0] Main menu")
 print("[1] Print Couriers")
 print("[2] Create/Add Couriers")
 print("[3] Update Couriers")
 print("[4] Delete a Courier")

#def load_csv_data():
    
 #   list = []
  #  with open("couriers.csv", 'r') as file:
   #     csv_file = csv.DictReader(file)
    #for row in csv_file:
   #     list.append(row)
   # return list
#print(load_csv_data())

def show_couriers_menu():
    couriers_menu()
    option = int(input("Enter your option: "))
    while option != 0: 
        if option == 1:
           get_from_database()
    #carry out option 1
        elif option == 2:
            new_courier()
      #carry out option 2
        elif option == 3:
            update_couriers(connect_to_database)
    #carry out option 3
        elif option == 4: 
            remove_courier(connect_to_database)
    # carry out option 4
        else:
            print("Invalid Option")
        couriers_menu() 
        option = int(input("Enter your option: "))

#couriers_list = load_csv_data

#courier_items = []

#open product.csv and read as string
#def load_couriers():
#    with open("couriers.csv", 'r') as file:
#     reader = csv.DictReader(file)
#    for row in reader:
#     couriers_list.append(row)
#load_couriers()

#def couriers_items():
#     courier_name = input("Please select the courier: ")
#     phone = input("Please select the phone number: ")
#     info_dict = {"courier name": courier_name, "phone": phone}
#     couriers_items.append(info_dict)

#with open("couriers.csv", "w+", newline = "") as file:
#         fieldnames = ["courier name", "phone"]
#         writer = csv.DictWriter(file, delimiter = ",", fieldnames = fieldnames)
#         writer.writeheader()
#         writer.writerows(couriers_items)

def connect_to_database():
    return pymysql.connect(host="localhost", user="root", password="password", database="test1")
    
def get_from_database():
  
    connection = connect_to_database()
    cursor = connection.cursor();
    cursor.execute(\
    """select * from couriers
    """)
    data_lists = cursor.fetchall()
    cursor.close()
    connection.close()  
    print (data_lists)
    
get_from_database()

def new_courier():
    courier_name = input("Enter Name: ")
    courier_number = input("Enter Number: ")
 
    add_to_database (courier_name, courier_number)

def add_to_database (courier_name, courier_number):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute (\
           f""" INSERT INTO couriers (courier_name, courier_number)
           VALUES (%s, %s)
           """,[courier_name, courier_number]) 
    connection.commit()
    cursor.close()
    connection.close()

