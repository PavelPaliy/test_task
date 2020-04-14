from django . urls import path
from .views import index, contacts, about


urlpatterns = [
    path ('', index),
    path ('about/', about),
    path ('contacts/', contacts),
]