from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    # path('read/1/', views.read)
    path('read/<id>/', views.read),

    # 12강
    # delete path 추가
    path('delete/', views.delete)
]
