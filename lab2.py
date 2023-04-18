while True:
    try:
        product_name = input("Enter product name: ")
        product_price_net = float(input("Enter product price net: "))
        client_email = input("Enter client email: ")
        client_phone = input("Enter client phone: ")
        
        tax_rate = 0.23
        product_price_gross = product_price_net * (1 + tax_rate)
        
        print("Welcome in Emin’s store.")
        print("Your basket:")
        print("name; net price; gross price; email, phone")
        print(f"{product_name}; {product_price_net:.2f}; {product_price_gross:.2f}; {client_email}, {client_phone}")
        break
    
    except ValueError:
        print("Process interrupted. Bad data type.. Write again")