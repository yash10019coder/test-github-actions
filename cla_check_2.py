from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import os.path
import sys
import json

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1naQC7iEfnro5iOjTFEn7iPCxNMPaPa4YnIddjT5CTM8'
SAMPLE_RANGE_NAME = 'Usernames'
TOKEN = os.environ['SHEETS_TOKEN']


def getValues():
  result = None
  creds = None
  try:
      creds = Credentials.from_authorized_user_info(
          json.loads(TOKEN), SCOPES)
      service = build('sheets', 'v4', credentials=creds)
      # Call the Sheets API
      sheet = service.spreadsheets()
      result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                  range=SAMPLE_RANGE_NAME).execute()
      result = result.get('values', [])
  except:
      print("API error:", sys.exc_info()[0])
  finally:
      return result


def main():
  prAuthor = [sys.argv[1]]
  print('Checking if ', prAuthor, ' has signed the CLA')
  values = getValues()
  if not values:
    print('No data found.')
  if(prAuthor in values):
		print(prAuthor, ' has signed the CLA')
		exit(0)
  else:
		print(prAuthor, ' has not signed the CLA')
		exit(1)


if __name__ == '__main__':
    main()
