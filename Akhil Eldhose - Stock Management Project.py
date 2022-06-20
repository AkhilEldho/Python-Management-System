#Project - Stock Management
#Akhil Eldhose 

#intilazing the lists
barcode = [2684, 5647, 3940, 123]
title = ["Justice League", "Avengers", "Batman", "Flash"]
category = ["Action", "Action", "Detective", "Adventure"]
price = [14.97, 13.99, 13.99, 14.52]
quantity = [12, 20, 30, 24]

#adding the product function
def addProduct():
    #input a code and check to if the book already in-stock
    print("+-------------------------------------+")
    code = int(input("| Enter the code of the new comic:"))        

    #checking if item is in inventory
    if(checkProduct(code) == True):
        print("+-------------------------------------+")
        print("| Code already in exists")
        addProduct()        
        
    #continue if product not in inventory
    elif(checkProduct(code) == False):
        barcode.append(code)    
        #adding title to the list
        print("+-------------------------------------+")
        name = input("| Enter Title     : ")
        title.append(name)
            
        #adding category
        print("+-------------------------------------+")
        sort = input("| Enter Category  : ")
        category.append(sort)
            
        #adding price
        print("+-------------------------------------+")
        money = float(input("| Enter Price     : "))
        price.append(money)
            
        #adding quantity
        print("+-------------------------------------+")
        amount = int(input("| Enter Quantity  : "))
        #keeps asking user to enter amount in range
        while (amount < 10 or amount > 50):
            print("| Quantity only between 10 to 50 can be taken")
            amount = int(input("| Enter new Quantity: "))
        quantity.append(amount)
        
        #checking to see if user wants to add more books
        print("+-------------------------------------+")
        more = input("| Would you like to add more books?\n| Y/N: ")
        if (more == 'y' or more == 'Y'):
            print("+-------------------------------------+")
            addProduct()
            
        print("| Comic Saved")
        searchProduct(code)
    
#checking to see if book is in the inventory
def checkProduct(itemCode):
    if (itemCode in barcode):
        return True
    else:
        return False

#searching for the product
def searchProduct(itemCode):
    if (checkProduct(itemCode) == True):
        #printing the details of the book
        #location is done through the index of barcode
        print("+-------------------------------------+")
        print("| Comic Details                       |")
        print("+-------------------------------------+")
        print("| Code       :", barcode[barcode.index(itemCode)])
        print("| Title      :", title[barcode.index(itemCode)])
        print("| Category   :", category[barcode.index(itemCode)])
        print("| Price      : $"+str(price[barcode.index(itemCode)]))
        print("| Quantity   :", quantity[barcode.index(itemCode)])
        print("+-------------------------------------+")
    
    #if book not in ask user if they want to add it
    elif (checkProduct(itemCode) == False):
        print("+-------------------------------------+")
        add = input("| Comic not found\n| Would you like to add it? Y/N: ")
        if (add == 'y' or add == 'Y'):
            addProduct()
        elif (add == 'n' or add == 'N'):
            code = int(input("| Enter the correct code: "))
            searchProduct(code)
            
        #repeat the function if not entering proper selection
        else:
            print("+-------------------------------------+")
            print("| Invalid Selection")
            searchProduct(itemCode)
    
#updating product
def updateProduct(itemCode):
    #Checking if product is in list or not
    if (checkProduct(itemCode) == False):
        cont = input("| Would you like to add product. Y/N: ")
        if (cont == 'y' or cont == 'Y'):
            addProduct()
        else:
            code = int(input("| Please enter proper code: "))
            updateProduct(code)
    #if true continue to update
    elif (checkProduct(itemCode) == True):
        searchProduct(itemCode)
        print("+-------------------------------------+")
        update = input("| Continue to update? Y/N: ")
        #if yes update each 
        if (update == 'y' or update == 'Y'):
            #title update
            #repeat until they input y or n
            while (True):
                print("+-------------------------------------+")
                titleUpdate = input("| Would you like to update Title, Y/N: ")
                if (titleUpdate == 'y' or titleUpdate == 'Y'):
                    name = input("| Enter new title: ")
                    title[barcode.index(itemCode)] = name
                    break
                elif (titleUpdate == 'n' or titleUpdate == 'N'):
                    break
                    
            #category update
            while (True):
                print("+-------------------------------------+")
                categoryUpdate = input("| Would you like to update Category, Y/N: ")
                if (categoryUpdate == 'y' or categoryUpdate == 'Y'):
                    sort = input("| Enter new category: ")
                    category[barcode.index(itemCode)] = sort
                    break
                elif (categoryUpdate == 'n' or categoryUpdate == 'N'):
                    break

            #price update
            while (True):
                print("+-------------------------------------+")
                priceUpdate = input("| Would you like to update Price, Y/N: ")
                if (priceUpdate == 'y' or priceUpdate == 'Y'):
                    money = float(input("| Enter new price: $"))
                    price[barcode.index(itemCode)] = money
                    break
                elif (priceUpdate == 'n' or priceUpdate == 'N'):
                    break

            #quantity update
            while (True):
                print("+-------------------------------------+")
                quantityUpdate = input("| Would you like to update/add quantity, Y/N: ")
                if (quantityUpdate == 'y' or quantityUpdate == 'Y'):
                    
                    #Asking if you would add to quantity
                    add = input("| Would you like to Add to Quantity, Y/N: ")
                    if (add == 'y' or add == 'Y'):
                        amount = int(input("| Add to Quantity: "))
                        while (amount < 10 or amount > 50):
                            print("| Quantity must be between 10 and 50")
                            amount = int(input("| Please enter new quantity: "))
                        #adding new quantity to existing value
                        quantity[barcode.index(itemCode)] += amount
                        break
                    
                    #Update Product
                    update = input("| Would you like to Update Quantity, Y/N: ")
                    if (update == 'y' or update == 'Y'):
                        amount = int(input("| Add to Quantity: "))
                        while (amount < 10 or amount > 50):
                            print("| Quantity must be between 10 and 50")
                            amount = int(input("| Please enter new quantity: "))
                        #assigning quantity
                        quantity[barcode.index(itemCode)] = amount
                        break
                elif (quantityUpdate == 'n' or quantityUpdate == 'N'):
                    break
                
            #printing out book details after update
            searchProduct(itemCode)
            print("| Updated")

        #if no exit to main menu
        elif(update == 'n' or update == 'N'):
            print("+-------------------------------------+")
            print("| Not updating")
        #if they enter anything else repeat the function
        else:
            print("+-------------------------------------+")
            print("| Invalid selection")
            updateProduct(itemCode)            
    
#buy product    
def buyProduct(itemCode, order):    
    #checking if product is in list
    if (checkProduct(itemCode) == True and quantity[barcode.index(itemCode)] != 0):
        #Making sure order isn't above 50 or quantity
        while (order > quantity[barcode.index(itemCode)]):
            print("|", barcode[barcode.index(itemCode)], "only has", quantity[barcode.index(itemCode)],"books in stock")
            order = int(input("| Please enter new amount: "))
        
        searchProduct(itemCode)
        choice = input("| Continue to buy? Y/N: ")
        
        if (choice == 'y'or choice == 'Y'):
            #if order is less 10 no discount
            if (order < 10):
                #calculating cost plus gst
                cost = order * price[barcode.index(itemCode)]
                total = cost + cost * 0.15
                print("+-------------------------------------+")
                print("| Total price will be $"+str(round(total,2)))
                
                #Subtracting order from purchase
                quantity[barcode.index(itemCode)]-= order
            
            #if order is less 10 no discount
            elif (10 <= order < 20):
                cost = order * price[barcode.index(itemCode)] - (order * price[barcode.index(itemCode)]*0.10)
                total = cost + (cost * 0.15)                
                print("+-------------------------------------+")
                print("| Total price will be $"+str(round(total,2)))
            
                #Subtracting order from purchase
                quantity[barcode.index(itemCode)]-= order
            
            #if order is from 20 - 30
            elif (20 <= order <=30):
                cost = order * price[barcode.index(itemCode)] - (order * price[barcode.index(itemCode)]*0.20)
                total = cost + (cost * 0.15)                
                print("+-------------------------------------+")
                print("| Total price will be $"+str(round(total,2)))
                
                #Subtracting order from purchase
                quantity[barcode.index(itemCode)]-= order
            
            #if order above 30 give 30% discount
            elif (30 < order):
                cost = order * price[barcode.index(itemCode)] - (order * price[barcode.index(itemCode)]*0.30)
                total = cost + (cost * 0.15)                
                print("+-------------------------------------+")
                print("| Total price will be $"+str(round(total,2)))

                #Subtracting order from purchase
                quantity[barcode.index(itemCode)]-= order
                if (quantity[barcode.index(itemCode)] < 0):
                    quantity[barcode.index(itemCode)] = 0
            
            else:
                print("| Comic book", barcode[barcode.index(itemCode)], "is out of stock")
                print("| Please update")
                searchProduct(itemCode)
        
        elif (choice == 'n' or choice == 'N'):
            print("+-------------------------------------+")
            cont = input("| Would you like to change quantity? Y/N: ")
            if (cont == 'y' or cont == 'Y'):
                amount = int(input("| Enter new amount: "))
                buyProduct(itemCode, amount)
            elif (cont == 'n' or cont == 'N'):
                print("| Order cancelled")
            else:
                print("| Invalid Selection")
            
        #if choice is anything else repeat the code
        else:
            print("+-------------------------------------+")
            print("| Invalid selection")
            buyProduct(itemCode, order)
    
    #if the product code is true but if it is 0 
    elif (checkProduct(itemCode) == True and quantity[barcode.index(itemCode)] == 0):
        print("| Comic book", barcode[barcode.index(itemCode)], "is out of stock")
        print("| Please add stock")
        searchProduct(itemCode)
    
    #if code doesn't exist ask them to add or to enter a new code        
    else:
        print("| Code does not exist")
        choice = input("| Would you like to add the code? Y/N ")
    
        if (choice == 'y' or choice == 'Y'):
            addProduct()
        elif (choice == 'n' or choice == 'N'):
            print("+-------------------------------------+")
            code = int(input("| Enter new code: "))
            amount = int(input("| Enter new quantity: "))
            buyProduct(code, amount)
        #if entered anything else repeat the function
        else:
            print("+-------------------------------------+")
            print("| Invalid Selection")
            buyProduct(itemCode, order)
                        
#Having options neatly in a function
def options():
    print("+-------------------------------------+")
    print("| 1. Add Comic Book                   |")
    print(" ------------------------------------- ")
    print("| 2. Search Comic Book                |")
    print(" ------------------------------------- ")
    print("| 3. Update Comic Book                |")
    print(" ------------------------------------- ")
    print("| 4. Buy Comic Book                   |")
    print(" ------------------------------------- ")
    print("| 5. Exit                             |")
    print("+-------------------------------------+")

#Main Program
print("+-------------------------------------+")
print("|            ComicStore               |")

#Making the loop infinte till exit becomes true
while(True):
    options()
    choice = int(input("| What would you like to do:          | "))
    print("+-------------------------------------+")
    
    #if choice is 1 go to add function
    if (choice == 1):
        addProduct()
        print("+-------------------------------------+")
        print("| Back to Main Menu                   |")
    
    #if choice is 2 go to search function
    elif (choice == 2):
        code = int(input("| Enter the code of the book: "))        
        searchProduct(code)
        print("+-------------------------------------+")
        print("| Back to Main Menu                   |")
    
    #if choice is 3 go to update function
    elif (choice == 3):
        code = int(input("| Enter the code of the book: "))        
        updateProduct(code)
        print("+-------------------------------------+")
        print("| Back to Main Menu                   |")
    
    #if choice is 4 go to buy function
    elif (choice == 4):
        code = int(input("| Enter the code of the book: "))
        order = int(input("| Enter the amount of books you want to buy: "))
        buyProduct(code, order)
        print("+-------------------------------------+")
        print("| Back to Main Menu                   |")
    
    #if choice is 5 stop code
    elif (choice == 5):
        print("+-------------------------------------+")
        print("|       Thank You for shopping        |")
        print("|                at                   |")
        print("|            ComicStore               |")
        print("+-------------------------------------+")
        break
    else:
        print("| Invalid selection")
        print("| Please select from the following")


