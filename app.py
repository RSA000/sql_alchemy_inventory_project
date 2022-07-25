from models import (Base, session, Inventory, engine)
import csv
from datetime import datetime
from os import system as sys
from time import sleep

def price_clean(price):
    return int(float(price[1:]) * 100)


def date_clean(date):
    date_clean = date.replace('/', '-')
    date_datetime  = datetime.strptime(date_clean, '%m-%d-%Y').date()
    return date_datetime


def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.reader(csvfile)
        next(data, None)
        for row in data:
            item_in_db = session.query(Inventory).filter(Inventory.product_name==row[0]).one_or_none()
            if item_in_db == None:
                product_name = row[0]
                product_price = price_clean(row[1])
                product_quantity = row[2]
                date_updated = date_clean(row[3])
                item = Inventory(product_name=product_name, product_price=product_price,
                                 product_quantity=product_quantity, date_updated=date_updated)
                session.add(item)
            else:
                new_item = Inventory(product_name = row[0], product_price=price_clean(row[1]),
                                product_quantity=row[2], date_updated=date_clean(row[3]))

                product_duplicate = session.query(Inventory).filter(Inventory.product_name==new_item.product_name).one()
                if new_item > product_duplicate:
                    product_duplicate.product_quantity = new_item.product_quantity
                    product_duplicate.date_updated = new_item.date_updated
                    product_duplicate.product_price = new_item.product_price
                else:
                    continue
        session.commit()


def menu():
    while True:
        sys('clear')
        choice = input(""" 
        \rINVENTORY MENU\n
        \rView Inventory: V
        \rAdd Product: A
        \rBackup DB: B\n
        \rEnter Choice: """).lower()
        if choice in ['v', 'a', 'b']:
            return choice
        input('''\nInvalid Choice:\nPlease enter \'V\' to view inventory,\n \'A\' to add a product or\n \'B\' to backupt the database:
        \r Press Enter to continue ''')
        sys('clear')


def display_inventory():
    ids = [id[0] for id in session.query(Inventory.product_id).all()]
    while True:
        sys('clear')
        print('\nINVENTORY DISPLAY\n', ids)
        choice = input('Please select a valid ID from the list above: ')
        try:
            if int(choice) in ids:
                sys('clear')
                print(session.query(Inventory).filter(Inventory.product_id == choice).one())
                input('\n Press Enter to continue ')
                break
            else:
                sys('clear')
                input('\n Invalid Input. Please select a valid number from the ID list \n Press Enter ')
                continue
        except ValueError:
            sys('clear')
            input('\n Invalid Input. Please select a valid number from the ID list. Press Enter to continue')
            


def add_product():
    product_name = input('Please input your product name: ')
    sys('clear')
    price_error = True
    while price_error:
        try:
            product_price = '$' + input('Please input your product price (format: 0.00): ')
            product_price = price_clean(product_price)
            price_error = False
            sys('clear')
        except (TypeError, ValueError):
            input('Invalid Price input. Price needs to be ex (0.00 or 20) ')
    quantity_error = True
    while quantity_error:
        try:
            product_quantity = int(input('Please input your quantity of the product: '))
            quantity_error = False
            sys('clear')
        except ValueError:
            input('Invalid quantity. Please input a valid quantity ex (10) Press Enter to continue ')
    date_error = True
    while date_error:
        date_updated = input('Please input the date updated format(month/day/year): ')
        try:
            date_updated = date_clean(date_updated)
            date_error = False
            sys('clear')
        except (ValueError, TypeError):
            input('''Invalid date input. Please enter date like ex(1/12/2010)\n
            press Enter to continue ''')
            sys('clear')
    new_item = Inventory(product_name=product_name, product_price=product_price, 
                        product_quantity=product_quantity, date_updated=date_updated)
    name_check = session.query(Inventory).filter(Inventory.product_name==new_item.product_name).one_or_none()
    if name_check != None:
        product_duplicate = session.query(Inventory).filter(Inventory.product_name==new_item.product_name).one()
        if new_item > product_duplicate:
            product_duplicate.product_quantity = new_item.product_quantity
            product_duplicate.date_updated = new_item.date_updated
            product_duplicate.product_price = new_item.product_price
            print('product already in database. updated!')
            sleep(2)
            return product_duplicate
        else:
            print('''Product Not Added
            \r You entered in a product that already exists with an updated
            \rtime that was before the most recent entry''')
            sleep(3)
    else:
        return new_item

def backup_database():
    records = [item.return_list()[1:] for item in session.query(Inventory)]
    records.insert(0, ['product_name','product_price','product_quantity','date_updated'])
    with open('backup.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(records)


def app():
    while True:
        choice = menu()
        if choice == 'v':
            display_inventory()
        elif choice == 'a':
            new_item = add_product()
            if new_item == None:
                continue
            session.add(new_item)
            session.commit()
            print('Product Added!')
            sleep(1)
            sys('clear')
        elif choice == 'b':
            backup_database()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    add_csv()
    app()
    