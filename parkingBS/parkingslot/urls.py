from django.urls import path
from . import views

urlpatterns = [
    path('slot-details/<int:pk>/', views.slot_details, name='slot-details'),
    path('create-slot/', views.create_slot, name='create-slot'),
    path('update-slot/<int:pk>/', views.update_slot, name='update-slot'),
    path('all-slots/', views.all_slots, name='all-slots'),
    path('slot-queue/', views.slot_queue, name='slot-queue'),
    path('accept-slot/<int:pk>/', views.accept_slot, name='accept-ticket'),
    path('close-slot/<int:pk>/', views.close_slot, name='close-slot'),
    path('workspace/', views.workspace, name='workspace'),
    path('all-closed-slots/', views.all_closed_slots, name='all-closed-slots')
]