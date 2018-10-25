from django.urls import path
from . import views
'''
experiments/add
experiments/<int:pk>/edit
experiments/<int:pk>/delete
'''
urlpatterns = [
    path('experiments/', views.ListExperiments.as_view()),
    path('experiments/<int:pk>', views.UpdateExperiment.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('create_user/', views.UserCreate.as_view()),
    path('/users/(?P<pk>[0-9]+)/', views.UserDetail.as_view()),
]
