from django.urls import path

from history import views

app_name = 'history'

urlpatterns = [
    path('', views.HistoryView.as_view(), name='history'),
    path('stats-by/<str:date>/', views.HistoryView.as_view(), name='stats_by'),
]