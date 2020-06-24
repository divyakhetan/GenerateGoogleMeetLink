from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import json
from pprint import pprint
from datetime import datetime, timedelta
from passwords import account_sid, auth_token, send_from, send_to
from twilio.rest import Client                                                        


# scopes = ["https://www.googleapis.com/auth/calendar"]

# flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
# flow.run_console()

# print(flow.credentials)
# pickle.dump(flow.credentials, open("token.pkl", "wb"))



credentials = pickle.load(open("token.pkl", "rb"))
# print(credentials)

service = build("calendar", "v3", credentials=credentials)

result = service.calendarList().list().execute()
# pprint(result['items'][0])

calendar_id = result['items'][0]['id']
# result = service.events().list(calendarId=calendar_id).execute()
# pprint(result['items'][1])

start_time = datetime(2020, 6, 23, 20, 15, 0)
end_time = datetime(2020, 6, 23, 20, 30, 0)

event = {
  'summary': 'Session Meet Link',
  'location': 'Mumbai',
  'description': 'Class',
  'start': {
    'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': 'Asia/Kolkata',
  },
  'end': {
    'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': 'Asia/Kolkata',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=1'
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
  'conferenceData': {
      'createRequest' : {
          'requestId' : "divya"
      }
  }, 
}

service.events().insert(calendarId=calendar_id, conferenceDataVersion=1, body=event).execute()
# print 'Event created: %s' % (event.get('htmlLink'))
result = service.events().list(calendarId=calendar_id).execute()
no_of_enteries = len(result['items'])
link = result['items'][no_of_enteries - 1]['hangoutLink']
# pprint(result['items'][no_of_enteries - 1])
print(link)


account_sid = account_sid
auth_token = auth_token

client = Client(account_sid, auth_token)

client.messages.create(
    to = send_to,
    from_= send_from,
    body = link
)
