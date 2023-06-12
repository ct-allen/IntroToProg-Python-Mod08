# ------------------------------------------------------------------------ #
# Title: Assignment 08 - Final
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# CAllen,6.4.2023,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        CAllen,6.4.2023,Modified code to complete assignment 8
    """
    pass  # remove after code is added
    # --Fields--
    #product_name_str = ''
    #product_price_flt = ''

    # --Constructor--
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception('Names Cannot Be Numbers')



    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        try:  # setting the product price to a float and error handling if user entered a non-numeric value
            fltval = float(value) # could probably do without this line but it's a double
            # safety net for float value error handling
            if isinstance(fltval, float) == True:
                self.__product_price = value
            else:
                raise Exception('Price Must Be A Numeric Value')
        except:
            raise Exception('Price Must Be A Numeric Value')

    def to_string(self):
        """Function to put product and price into CSV format
        """
        object_data_csv = self.product_name + "," + str(self.product_price)
        return object_data_csv

    def __str__(self):
        """Modifying original python function to call custom to_string function"""
        return self.to_string()


# Data End-------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        CAllen,6.4.2023,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name, lstOfProductObjects):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param lstOfProductObjects: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        try:
            lstOfProductObjects.clear()  # clear current data
            file = open(file_name, "r")
            for line in file:
                product, price = line.split(",")
                row = {"Product": product.strip(), "Price": price.strip()}
                lstOfProductObjects.append(row)
            file.close()
            print('Data loaded from products.txt file')
            return lstOfProductObjects
        except:
            print('No .txt file found, continue making list.')

    @staticmethod
    def write_data_to_file(file_name, lstOfProductObjects):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param lstOfProductObjects: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        objFile = open(file_name, "w")
        for row_dic in lstOfProductObjects:
            objFile.write(row_dic['Product'] + "," + str(row_dic['Price']) + "\n")
        objFile.close()

        return lstOfProductObjects

    @staticmethod
    def add_data_to_list(prod, price, lstOfProductObjects):
            """ Adds data to a list of dictionary rows

            :param prod: (string) with name of product:
            :param price: (string) with name of price:
            :param lstOfProductObjects: (list) you want to add more data to:
            :return: (list) of dictionary rows
            """
            row = {"Product": str(prod).strip(), "Price": price}
            lstOfProductObjects.append(row)

            return lstOfProductObjects

# Processing End  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """  A class for performing Input and Output

    methods:
        print_menu_items():

        print_current_list_items(lstOfProductObjects):

        input_product_data():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
        CAllen,6.9.2023, Created methods: input_menu_choice, print_current_list_items, input_product_data
    """
    # Add code to show menu to user (Done for you as an example)
    @staticmethod
    def print_menu_items():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item
        3) Save Data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks in the terminal window

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice_str = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice_str

    @staticmethod
    def print_current_list_items(lstOfProductObjects):
            """ Shows the current Tasks in the list of dictionaries rows

            :param lstOfProductObjects: (list) of rows you want to display
            :return: nothing
            """
            print("*** The current products & prices are: ***")
            for row_dic in lstOfProductObjects:
                print(row_dic["Product"].strip(),"|", row_dic["Price"])
            print("******************************************")
            print()  # Add an extra line for

    @staticmethod
    def input_product_data():
        """  Gets product and price values to be added to the list

        :return: (string, string) with product and price
        """
        prod = input('Enter a Product: ')
        price = input('Enter a Price: ')
        prod1 = Product(prod, price)
        prod_new = prod1.product_name
        price_new = prod1.product_price

        return (prod_new, price_new)

# Presentation (Input/Output) End  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(file_name=strFileName, lstOfProductObjects=lstOfProductObjects)

# Show user a menu of options
while (True):
    IO.print_menu_items()

# Get user's menu option choice
    choice_str = IO.input_menu_choice()

    # Show user current data in the list of product objects
    if choice_str.strip() == '1':
        IO.print_current_list_items(lstOfProductObjects=lstOfProductObjects)
        continue

    # Let user add data to the list of product objects
    elif choice_str == '2':
        prod, price = IO.input_product_data()
        print(prod, price, 'has been added to list')
        FileProcessor.add_data_to_list(prod=prod, price=price, lstOfProductObjects=lstOfProductObjects)
        continue

    # let user save current data to file and exit program
    elif choice_str == '3':  # Save Data to File
        table_lst = FileProcessor.write_data_to_file(file_name=strFileName, lstOfProductObjects=lstOfProductObjects)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop

    else:
        print('That is not a menu option')
        print('Please enter a choice 1-4')
        continue

# Main Body of Script End  ---------------------------------------------------- #

