""" App URL Configuration """
from django.urls import path

from northstar.views import *


urlpatterns = [
    path('users', UserListView.as_view()),
    path('users/<str:uid>', UserDetailView.as_view()),
    path('users/<str:uid>/search', PlacesListView.as_view()),
    path('org/event', EventListView.as_view()),
    path('org/event/<int:id>', EventDetailView.as_view()),
    path('org', OrganisationsListView.as_view()),
    path('org/<int:id>', OrganisationDetailView.as_view()),
    path('categories', CategoriesListView.as_view()),
    path('users/<str:uid>/recommend', RecommendationsListView.as_view()),
    path('org/<int:id>/event', EventByOrgListView.as_view()),
    path('stats/category', CategoryStats.as_view()),
    path('stats/place', PlacesStats.as_view()),
]
