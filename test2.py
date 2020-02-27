from __future__ import print_function
import datetime
from datetime import timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from model import db as db
from cryptography.fernet import Fernet
def function_candidate(data):
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    token_file="token_adi1.pickle"
    creds=""
    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    # service_for_file=build('drive','v3',credentials=creds)
    event1 = {
        'summary': 'Interview Slot Confirmation',
        'location': 'DarwinBox Hyderabad',
        'description':"Hello",
        'start': {
        'dateTime':'2020-04-01T12:00:00',
        'timeZone': 'Asia/Kolkata',
        },
        'end': {
        'dateTime':'2020-04-01T14:00:00',
        'timeZone': 'Asia/Kolkata',
        },

        'attendees': [
            {'email':'adithyakng5243@gmail.com'},
            {'email':"naveen.c@darwinbox.in"},
            {'email':"qwertykeypad9079@gmail.com"}
            ],
        "guestsCanSeeOtherGuests": false,
        'conferenceData':data,
        }
    event = service.events().insert(calendarId='primary', body=event1,sendUpdates="all",supportsAttachments=True,conferenceDataVersion=1).execute()
    print(event['conferenceData']['entryPoints'])  
    print(event)
    # return (eventabcd['conferenceData'])


def function_interviewers():
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    token_file="token_adi1.pickle"
    creds=""
    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    # service_for_file=build('drive','v3',credentials=creds)
    event1 = {
        'summary': 'Interview Slot Confirmation',
        'location': 'DarwinBox Hyderabad',
        'description':"Hello",
        'start': {
        'dateTime':'2020-04-01T12:00:00',
        'timeZone': 'Asia/Kolkata',
        },
        'end': {
        'dateTime':'2020-04-01T14:00:00',
        'timeZone': 'Asia/Kolkata',
        },

        'attendees': [
            {'email':'adithyakng@gmail.com'}
            ]
        }
    event= service.events().insert(calendarId='primary', body=event1,sendUpdates="all",supportsAttachments=True,conferenceDataVersion=0).execute()
    del event['conferenceData']['entryPoints'][1]
    print(event['conferenceData']['entryPoints']) 
    return (event['conferenceData'])

get_conferenceData=function_interviewers()
function_candidate(get_conferenceData)
