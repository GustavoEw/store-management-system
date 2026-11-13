from database.connection import connect_to_google_sheets
from services.product import Product
from datetime import datetime

credentials_json = "credetials/credentials.json" 
 # Update with the path to your credentials JSON file
sheet_name = "Dados Loja" 
# Update with the name of your Google Sheet
db=connect_to_google_sheets(credentials_json, sheet_name)

worksheet=db.worksheet("Produtos")
      # Print the title of the sheet to verify the connection
print(f"Connected to Google Sheet: {worksheet.title}"); 
product = Product()
def create_product():
    # Creating a product via the terminal, to test the object
    id = input("Enter product ID: ")
    name = input("Enter product name: ")
    unit = input("Enter product unit, 1 for unite, 2 for kg: ")
    category = input("Enter with product category example: Spices, Sugar, etc: ")
    quantity=None
    price = float(input("Enter product price: "))
    if(unit == "1"):
        quantity = int(input("Enter product quantity: "))
    elif(unit == "2"):
        quantity = float(input("Enter product quantity: "))
    barcode = input("Enter product barcode: ")
    expiration_date = datetime.strptime(input("Enter product expiration date (DD/MM/YYYY): "), "%d/%m/%Y").date()
    cost = float(input("Enter product cost: "))
    observations = input("Enter product observations: ")
    return id, name, unit, category, barcode, expiration_date, price, cost, quantity, observations

product.set_product(*create_product())
data = product.get_product()
values = list(data.values())
worksheet.append_row(values)