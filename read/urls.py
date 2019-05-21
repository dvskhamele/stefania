from django.urls import include, path
from . import views

urlpatterns = [
# tested
    path('data/', views.First.as_view()),
    # path('savesellerfilters/', views.ListSaveSeller.as_view(), name = 'listshops'),
    # path('savesellerrud/<pk>/', views.SavesellerRUD.as_view(), name = 'RUD')
]
