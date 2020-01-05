from django.urls import path
from .views import *




urlpatterns=[

    path('mytasks/',TaskView.as_view(),name='mytasks'),
    path('addtask/',TaskCreateView.as_view(),name='addtask'),
    path('mytasks/<int:pk>/delete',TaskDeleteView.as_view(),name='delete_task'),
    path('mytasks/<int:pk>/update',TaskUpdateView.as_view(),name='update_task'),
    # path('mytasks/<int:pk>',TaskDetailView.as_view(),name='detail_task'),


]