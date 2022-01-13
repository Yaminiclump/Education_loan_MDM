from django.urls import path

from . import views

urlpatterns = [
    path("get_country_by_id", views.get_country_by_id, name="get_country_by_id"),
    path("get_country_list", views.get_country_list, name="get_country_list"),
    path("search_country", views.search_country, name="search_country"),

    path("get_state", views.get_state, name="get_state"),
    path("search_state", views.search_state, name="search_state"),

    path("get_city", views.get_city, name="get_state"),
    path("search_city", views.search_city, name="search_city"),

    path("get_pincode", views.get_pincode, name="get_pincode"),
    

    path("get_institute", views.get_institute, name="get_institute"),
    path("search_institute", views.search_institute, name="search_institute"),

]
