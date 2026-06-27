from django.shortcuts import render
from rest_framework import viewsets
from dis_task.models import Task
from dis_task.serializers import TaskSerializer
from dis_task.permissions import IsAdminOrOwner
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class  = TaskSerializer
    permission_classes = [IsAdminOrOwner]
    search_fields = ['title', 'description']

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['status']
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'created_at']

    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name='Admin').exists():
            return Task.objects.all()
        
        return Task.objects.filter(owner = user)
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)