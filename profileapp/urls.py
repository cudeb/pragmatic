from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'
urlpatterns = [
    path('create/',ProfileCreateView.as_view(),name='create'),
    path('udpate/<int:pk>',ProfileUpdateView.as_view(),name='update'),
]