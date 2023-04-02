"""tudo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from tasks import views
from crm import views as crm_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/add/',views.TodoCreateView.as_view(),name="todo-add"),
    path('todos/all/',views.TodoListView.as_view(),name="todo-list"),
    path('todos/<int:pk>',views.TodoDetailView.as_view(),name="todo-detail"),
    path('todos/<int:pk>/remove/',views.TodoDeleteView.as_view(),name="todo-delete"),
    path('todos/<int:pk>/change/',views.TodoUpdateView.as_view(),name="todo-change"),
    path('todos/all/completed/',views.TodoCompletedView.as_view(),name="todo-completed"),


    path('employee/add/',crm_views.EmployeeCreateView.as_view(),name="emp-add"),
    path('employee/all/',crm_views.EmployeeListView.as_view(),name="emp-list"),
    path('employee/<int:pk>/detail/',crm_views.EmployeeDeatilView.as_view(),name="emp-detail"),
    path('employee/<int:pk>/remove/',crm_views.EmployeeDeleteView.as_view(),name="emp-delete"),
    path('employee/<int:pk>/edit/',crm_views.EmployeeEditView.as_view(),name="emp-edit"),
    path('register/',crm_views.SignUpView.as_view(),name="regsiter"),
    path('login/',crm_views.SignInView.as_view(),name="signin"),
    path('logout/',crm_views.signout_view,name="signout"),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
