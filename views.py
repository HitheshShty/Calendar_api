from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .serializers import EventSerializer,UpdateSerializer
import pytz
from datetime import datetime

SCOPES = ["https://www.googleapis.com/auth/calendar"] # selected that facilitates create,update and deletion of the event

SERVICE_ACCOUNT_FILE = 'E:\calendar_rest_api\service_accountfile.json' # path for the json data

class CreateEventView(APIView):
    def __init__(self):
        super().__init__()
        self.credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    def post(self, request):# defined to handle the HTTP POST request
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(): # validating the data
            event_data = serializer.validated_data

            start_datetime_utc = datetime.combine(event_data['start_date'], event_data['start_time'])
            end_datetime_utc = datetime.combine(event_data['end_date'], event_data['end_time'])

            attendees = [email.strip() for email in event_data.get('attendees').split(',')]
            attendees = [{'email': email} for email in attendees] #email to be entered in comma seprated way

            event_body = {
                'summary': event_data['summary'],
                'location': event_data['location'],
                'description': event_data['description'],
                'colorId': event_data['colorId'],
                'start': {'dateTime': start_datetime_utc.isoformat(), 'timeZone': 'UTC'},
                'end': {'dateTime': end_datetime_utc.isoformat(), 'timeZone': 'UTC'},
                'recurrence': event_data['recurrence'],
                'attendees':  event_data['attendees'],
            }


            service = build("calendar", "v3", credentials=self.credentials)
            try:
                event = service.events().insert(calendarId="primary", body=event_body).execute()
                print(event)
                eventId = event['id']
                print(eventId)
                return Response({"message": "Event created successfully", "event_link": event.get('htmlLink')}, status=status.HTTP_201_CREATED)
            except HttpError as error:
                return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UpdateEventView(APIView):
    def __init__(self):
        super().__init__()
        self.credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    def put(self, request, event_id):
        serializer = UpdateSerializer(data=request.data)
        if serializer.is_valid():
            event_data = serializer.validated_data
            
            existing_event = self.fetch_event(event_id)
            if not existing_event:
                return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
            
            updated_event = self.update_event(existing_event, event_data)
            
            service = build("calendar", "v3", credentials=self.credentials)
            try:
                service.events().update(calendarId="primary", eventId=event_id, body=updated_event).execute()
                return Response({"message": "Event updated successfully"}, status=status.HTTP_200_OK)
            except HttpError as error:
                return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def fetch_event(self, event_id):
        service = build("calendar", "v3", credentials=self.credentials)
        try:
            event = service.events().get(calendarId="primary", eventId=event_id).execute()
            return event
        except HttpError as error:
            if error.resp.status == 404:
                return None  
            else:
                raise 

    def update_event(self, existing_event, new_event_data):
        for key, value in new_event_data.items():
            if value is not None:
                existing_event[key] = value
        return existing_event



class DeleteEventView(APIView):

    def __init__(self):
        super().__init__()
        self.credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)



    def delete(self,request, event_id):
        service = build("calendar", "v3", credentials=self.credentials)
        try:
            service.events().delete(calendarId="primary", eventId=event_id).execute()
            return Response({"message": "Event deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except HttpError as error:
            return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)









        
        




