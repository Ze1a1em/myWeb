from django.urls import path, re_path

from . import views

app_name = 'groups'

urlpatterns = [
    path("", views.ListGroups.as_view(), name="all"),
    path("new/", views.CreateGroup.as_view(), name="create"),
    re_path("posts/in/(?P<pk>[-\w]+)/$",views.SingleGroup.as_view(),name="single"),
    re_path(r"join/(?P<pk>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
    re_path(r"leave/(?P<pk>[-\w]+)/$",views.LeaveGroup.as_view(),name="leave"),
]
