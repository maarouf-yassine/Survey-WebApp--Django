
from django.contrib import admin
from django.urls import path
from surveyapp import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("surveys/<str:topic>", views.Surveys, name="surveys"),
    path("signup", views.signup, name="signup"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("singlesurvey/<str:single_survey_name>", views.single_survey, name="singlesurvey"),
    path("addcat", views.addcat, name="addcat"),
    path("deletecat", views.deletecat, name="deletecat"),
    path("addsurv", views.addsurv, name="addsurv"),
    path("deletesurv", views.deletesurvey, name="deletesurv"),
    path("update", views.updatesurv, name="update")
]