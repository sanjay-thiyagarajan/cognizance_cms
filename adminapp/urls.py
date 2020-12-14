from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('dashboard/',views.dashboard),
    path('members/',views.members, name='members'),
    path('announcements/', views.announcements, name='announcements'),
    path('add-members/',views.add_members, name='add-members'),
    path('groups/',views.groups, name='groups'),
    path('add-group/',views.add_group,name='add-group'),
    path('reviewing/<str:application_id>/', views.reviewing, name='reviewing'),
    path('applications/', views.applications, name='applications'),
    path('tasks/',views.tasks, name='tasks')
]