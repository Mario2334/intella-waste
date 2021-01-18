from datetime import date, datetime

from rest_framework.response import Response

from user.serializers import UserSerializer
from .models import Event
from rest_framework.decorators import action
from rest_framework import viewsets,views
from rest_framework.permissions import IsAuthenticated
from .serializers import EventSerializer
from django.db.models import Q

from .utils import TestCalendar


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(Q(creator=self.request.user) | Q(guests__in=[self.request.user,]))

    def create(self, request, *args, **kwargs):
        request.data["creator"] = request.user.id
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        try:
            event= Event.objects.get(id=kwargs["pk"])

        except Event.DoesNotExist as e:
            return Response(status=404)

        if(event.guests.count()<11 and event.creator.id != request.user.id):
            event.add_guest(request.user)
            return Response(status=200)
        else:
            return Response(status=406)


class CalendarViewSet(views.APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(Q(creator=self.request.user) | Q(guests__in=[self.request.user, ]))

    def get(self,request,year,month):

        # # use today's date for the calendar
        # d = get_date(('day', None))

        cal = TestCalendar(self.get_queryset(),year,month)
        html = cal.formatmonth(withyear=True)
        return Response(html,content_type="text/html")

# def get_date(req_day):
#     if req_day:
#         year, month = (int(x) for x in req_day.split('-'))
#         return date(year, month, day=1)
#     return datetime.today()