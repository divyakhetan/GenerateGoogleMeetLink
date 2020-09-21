from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

scopes = ["https://www.googleapis.com/auth/calendar"]

flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
flow.run_console()

print(flow.credentials)
pickle.dump(flow.credentials, open("token.pkl", "wb"))



credentials = pickle.load(open("token.pkl", "rb"))
print(credentials)
