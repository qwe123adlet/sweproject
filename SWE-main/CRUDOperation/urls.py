"""CRUDOperation URL Configuration

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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # new
    path('accounts/', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('something/',views.showemp, name = "showemp"),
    path('something/Insert',views.insertemp,name="insertemp"),
    path('something/InsertPatient', views.insertpatient, name="insertpatient"),
    path('something/editpatient/<int:id>', views.editpatient, name="editpatient"),
    path('UpdatePatient/<int:id>',views.updatepatient, name="updatepatient"),
    path('something/edit/<int:id>', views.editemp,name="editemp"),
    path('Update/<int:id>',views.updateemp, name="updateemp"),
    path('something/DeletePatient/<int:id>', views.delpatient, name="delpatient"),
    path('something/Delete/<int:id>', views.delemp, name="delemp"),
    path('showspecialization/',views.showspecialization,name="showspecialization"),
    path('showspecialization/doctortableSpec/<int:id>', views.doctortableSpec, name = "doctortableSpec"),
    path('searchbar/', views.searchbar, name="searchbar"),
    path('doctortable/<int:id>', views.doctortable, name = "doctortable"),
    path('showspecialization/appointment', views.makeappointment, name = "makeappointment"),
]
