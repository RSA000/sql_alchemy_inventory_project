#### SQL Alchemy Inventory Project

A Console application that stores inventory data. The application can take a CSV file and load it into an SQLite database. The user should be able to interact with the data and also backup/export the existin state of the database into a CSV file.

Tasks: 

* Tidy Repo: 
    * Repository does not contain virtual environment, __pycache or DS.Store

* Database Setup
    * SQLite Database has name inventory.db
    
    * Product model named properly ('products')

* The Product Model:
    * Products have 5 columns (product_id, product_name, product_quantity, product_price, date_updated)

* CSV to Database
    * product_quantity is stored as an integer
   
    * product_price is stored as an integer
   
    * date_updated is stored as a DateTime object

* Adding existing data to the database
    * produce_quantity is an integer
    
    * produce_price is an Integer
    
    * date_updated is a Datetime object
    
    * EXTRA: if a duplicate product name is found, only the most recently updated is added.

* Menu Prompts
    * All menu prompts added (v to view, a to add, b to backup)
   
    * EXTRA: If any other character is pressed users is presented with a readable error message and can try again

* Menu option V
    * Products id's are listed and user can choose one to see a readable description
    
    * EXTRA: If an invalid input is entered, user is given a readable error message and can try again

* Menu option A:
    * User is prompted to insert product name, quantity and price
    
    * EXTRA: If there is already an entry with the same name, the item is updated

* Menu option b: 
    * A CSV called backup.csv is created and contains all the current contents of the products table
    
    * EXTRA: backups.csv file contains a header

* ##### More Extras
    * When creating the csv backup. prices are converted back into '$0.00' format so it matches the original csv
    
    * dates are also reverted back to original format when backing up csv
    
    * A quit function is added when user wants to exit the application 
    
    * When Adding a product, the inputted name is converted to title case
    
    * If date_updated is before the date of the already existing entry, an error message will be presented to user describing the error and will not change the current entry.

