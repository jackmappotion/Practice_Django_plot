"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from plot_matplotlib.views import visualize_data as matplotlib_visualize_data
from plot_seaborn.views import visualize_data as seaborn_visualize_data
from plot_plotly.views import visualize_data as plotly_visualize_data

urlpatterns = [
    path("admin/", admin.site.urls),
    path("matplotlib_visualize/", matplotlib_visualize_data, name="matplotlib_visualize_data"),
    path("seaborn_visualize/", seaborn_visualize_data, name="seaborn_visualize_data"),
    path("plotly_visualize/", plotly_visualize_data, name="plotly_visualize_data"),
]
