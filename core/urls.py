#   Copyright (c) Code Written and Tested by Ahmed Emad in 28/02/2020, 16:53

from django.urls import path

from core.views import RedirectView, ShortenView, home, Redirect, Shorten

app_name = 'core'

urlpatterns = [
    path('', home),
    path('shorten', Shorten, name='shorten'),
    path('<str:url>', Redirect, name='redirect')
]
