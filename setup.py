from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import json
from pprint import pprint
from datetime import datetime, timedelta
from passwords import account_sid, auth_token, send_from, send_to
from twilio.rest import Client                                                        


scopes = ["https://www.googleapis.com/auth/calendar"]

flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
flow.run_console()

print(flow.credentials)
pickle.dump(flow.credentials, open("token.pkl", "wb"))



credentials = pickle.load(open("token.pkl", "rb"))
print(credentials)

