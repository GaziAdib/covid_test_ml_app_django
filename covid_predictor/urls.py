from django.contrib import admin
from django.urls import path
from predict import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('records/', views.db_record, name='records'),
    path('delete/<int:pk>', views.delete, name='delete')
]
