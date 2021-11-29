"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse
import dask
from django.shortcuts import render

df = dask.datasets.timeseries(start='2020-01-01', end='2020-01-30', freq="3600s").compute()

def sub_table(request):
    # sub = df.loc[df['name'] == name]
    # sub = sub.sort_values('x')[:10]
    return render(request,{'sub':'name'})

def hello(request):
    return HttpResponse('Hello World')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',sub_table),
]
