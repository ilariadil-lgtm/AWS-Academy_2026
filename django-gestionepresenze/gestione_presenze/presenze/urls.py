from django.urls import path
from .views import RegistrazioneView

urlpatterns = [
    path('registrazione/', RegistrazioneView.as_view(), name='registrazione'),
    # altre view per presenze/assenze
]