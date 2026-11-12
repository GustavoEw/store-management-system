import gspread
from gspread.exceptions import SpreadsheetNotFound, APIError

## Connect to Google Sheets using gspread
def connect_to_google_sheets(credentials_json, sheet_name):
    try:
        """
        Connect to a Google Sheet using gspread.

        Args:
            credentials_json (str): Path to the JSON file with Google API credentials.
            sheet_name (str): Name of the Google Sheet to connect to.

        Returns:
            gspread.models.Spreadsheet: The connected Google Sheet object.
        """
        # Authenticate using the provided credentials
        gc = gspread.service_account(filename=credentials_json)
        
        # Open the specified Google Sheet
        sh = gc.open(sheet_name)
        
        return sh
    except SpreadsheetNotFound:
        print(f"Error: The Google Sheet '{sheet_name}' was not found. Please check the sheet name and try again.")
        return None 
    except APIError as error:
        print(f"API Error: {error}. Please check your credentials and try again.")
        return None