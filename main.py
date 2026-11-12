from database.connection import connect_to_google_sheets
from services.product import Product

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
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    return id, name, price, quantity

product.set_product(*create_product())
data = product.get_product()
print(data["name"])  # Print the product name to verify the data
print(data["id"]) 
     # Print the entire product data to verify the object