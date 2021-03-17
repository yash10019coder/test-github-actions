from __future__ import print_function
import os.path
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1naQC7iEfnro5iOjTFEn7iPCxNMPaPa4YnIddjT5CTM8'
SAMPLE_RANGE_NAME = 'Usernames'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    tmp = {"scopes": ["https://www.googleapis.com/auth/spreadsheets.readonly"], "token_uri": "https://oauth2.googleapis.com/token", "expiry": "2021-03-17T16:37:31.818747Z", "token": "ya29.a0AfH6SMArk7xbOZ8nVbb6AKCqHNOZ02aWhkL-OC16lnaRM_Lcp6GYLk2mQi4ChbnA8PlR4A4HEZKuj468VBvqvGCOlF4P722q9HFIlaV-ZBDlLVPSYECIPVP25X35psVgQqKwBetJPOZ7m2bOo7eGd-ydIrOl", "client_id": "589502381328-ejaahnr6l7seamn7mf3qindk3v8b2qej.apps.googleusercontent.com", "client_secret": "tfq98wceMO7kH846HJOYaIAA", "refresh_token": "1//0gC-jLMYI6h5cCgYIARAAGBASNwF-L9IrP1wU348_rdGmcQJfbU-UDcAako6niWQbSkYO57FdqNWHJ6pbXyJw1zYYg8tqJq6xSAQ"}

    creds = None
    creds = Credentials.from_authorized_user_info(tmp, SCOPES)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    print(result)
    print(values)

if __name__ == '__main__':
    main()