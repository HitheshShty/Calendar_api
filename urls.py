from django.urls import path
from .views import CreateEventView
from .views import UpdateEventView
from .views import DeleteEventView

urlpatterns = [
    path('create-event/', CreateEventView.as_view(), name='create-event'),  #url to direct for creating an event
    path('update-event/<str:event_id>', UpdateEventView.as_view(),name='update-event'),#update the event using event_id
    path('delete-event/<str:event_id>',  DeleteEventView.as_view(),name = 'delete-event')#delete the event using event_id
]