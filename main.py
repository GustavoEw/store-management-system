from database.connection import connect_to_google_sheets

credentials_json = 'path/to/your/credentials.json' 
 # Update with the path to your credentials JSON file
sheet_name = 'Banco Loja'  
# Update with the name of your Google Sheet
db=connect_to_google_sheets(credentials_json, sheet_name)

print(db.title)  # Print the title of the Google Sheet to verify the connection