from django.test import TestCase

# Create your tests here.

import django_filters
from rest_framework import filters
from rest_framework import viewsets

class EventFilter(filters.FilterSet):
    timestamp_gte = django_filters.DateTimeFilter(name="timestamp", lookup_expr='gte')
    class Meta:
        model = Event
        fields = ['event_type', 'event_model', 'timestamp', 'timestamp_gte']

class EventsView(viewsets.ReadOnlyModelViewSet):
    ...
    filter_class = EventFilter



