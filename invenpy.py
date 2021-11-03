
#*######################################################
### * imports * ### 

import sys 
from subprocess import call 
import math 
import json 
from datetime import datetime 

#*######################################################
### * Variables * ### 

data_file = 'log_invenpy.json'
version = '1.0'
date_format = '%m/%d/%y'

#*######################################################
### * Product Object * ### 

class Product:
    def __init__(self,name,cost,sell,target_stock,current_stock): 
        # General information information 
        self.prod_id = 0
        self.name = name
        self.cost = cost
        self.sell = sell
        self.target_stock = target_stock
        self.current_stock = current_stock
        
    def data(self):
        data_dict = {
            "id":self.prod_id,
            "name":self.name,
            "cost":self.cost,
            "sell":self.sell,
            "target_stock":self.target_stock,
            "current_stock":self.current_stock
        }
        return data_dict


#*######################################################
### * UI functions * ### 


def new_screen():
    # Clears screen and adds cute lil header
    call('clear')
    print('    /// Invenpy ///')
    print(f'/ Version: {version} / ')
    print('\n')


def start_menu(): # Nav menu on startup 
    new_screen()
    print('1. New inventory report')
    print('2. Product statistics')
    print('3. Product information')
    print('4. View logs')
    print('5. Edit inventory')
    print('6. Settings')
    select = input('[#] ')
    
    if select == '1':
        pass 
    elif select == '2':
        pass 
    elif select == '3':
        pass 
    elif select == '4':
        pass 
    elif select == '5':
        edit_inventory()
    elif select == '6':
        pass
    else:
        pass


#*######################################################
### * Modifying Inventory * ### 


def edit_inventory():
    new_screen()
    print('1. Add new product to inventory.')
    print('2. Delete product.')
    print('3. Modify product information.')
    select = input('[#] ')
    
    if select == '1':
        new_product()
    elif select == '2':
        pass 
    elif select == '3':
        pass 


def new_product():
    new_screen()
    print('Create new product? [Y/N]')
    print('You will be asked to provide information about the product to be tracked.')
    confirm = input('[Y/N] ')
    if confirm.lower() == 'y':
        new_screen()
        name = input('[!] Product name: ')
        cost = input('[!] Product unit cost: $')
        sell = input('[!] Product sale price: $')
        target = input('[!] Minimum desired units on hand: ')
        current = input('[!] Current units on hand: ')
        cont = input('[!] Continue with above entries? [Y/N] ')
        if cont.lower() == 'y':
            new_screen()
            new = Product(name,cost,sell,target,current)
            new_data = new.data()
            data = load_json()
            data["products"].append(new_data)
            save_json(data)
            input('[!] New product added! Press enter to continue. ')
        start_menu()
    

def record_inventory():
    pass


#*######################################################
### * JSON and data management * ### 

def get_today():
    return datetime.now()


def format_json(): # Reset data file with empty format.
    #! Resets all json data, use with caution.
    format = {
        "products":[],
        "logs":[],
        "settings":[]
        }
    
    save_json(format)


def load_json(): # Open file and return loaded json object
    file = open(data_file,'r') 
    data = json.load(file)
    file.close() 
    return data 


def save_json(data): # Update json file with new data 
    new_data = json.dumps(data, indent=4)
    file = open(data_file,'w') 
    file.write(new_data)
    file.close()


#*######################################################
#*######################################################
#*######################################################

#*######################################################

start_menu()

#*######################################################