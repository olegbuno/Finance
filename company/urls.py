from django.urls import path
from .views import CldrView, DocuView, PdView, PinsView, RunView, ZmView, ZuoView, CompanyView

app_name = "company"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('company/', CompanyView.as_view()),
    path('company/cldr', CldrView.as_view()),
    path('company/docu', DocuView.as_view()),
    path('company/pd', PdView.as_view()),
    path('company/pins', PinsView.as_view()),
    path('company/run', RunView.as_view()),
    path('company/zm', ZmView.as_view()),
    path('company/zuo', ZuoView.as_view()),
]