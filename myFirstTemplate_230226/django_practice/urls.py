"""django_practice URL Configuration

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
from django.urls    import path
# from app1.views     import homepage
# from app2.views     import pageApp2, ntab1, about, listing, bootstrap

import app1.views as views1
import app2.views as views2
"""
from django.contrib import admin
from django.urls    import path
from app1.views     import homepage
"""

urlpatterns = [
    path('admin/'        , admin.site.urls),
    path(''              , views1.homepage),
    path('App2'          , views2.pageApp2),
    path('App2/ntab1'    , views2.ntab1),
    path('about'         , views2.about),
    path('App2/list'     , views2.listing),
    path('App2/bootstrap', views2.bootstrap),
    path('list/<int:yr>/<int:mon>/<int:day>/', views2.LISTING),
]
