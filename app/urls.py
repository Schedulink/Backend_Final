from django.urls import path
from .import views

urlpatterns = [
    path('dept/',views.DeptList.as_view()),
    path('deg/',views.DegprmList.as_view()),
    path('sem/',views.SemList.as_view()),
    path('sub/',views.SubList.as_view()),
    path('fac/',views.FacList.as_view()),
    path('timetable/',views.TimetableList.as_view()),
    path('admin/',views.AdminList.as_view()),
]