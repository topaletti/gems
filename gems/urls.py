"""gems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

import app.views
import app.mail

urlpatterns = [
    path('', app.views.index, name="app/index"),
    path('companies/', app.views.DatabaseView.as_view(), name="app/database"),
    path('challenges/', RedirectView.as_view(url='2022-04/'), name="app/challenges"),
    path('challenges/<slug:slug>/', app.views.ChallengeView.as_view(), name="app/challenge"),
    path('admin/', admin.site.urls),
    #path('sendtestmail/', app.mail.send_test_mail),
]
