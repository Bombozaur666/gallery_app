from django.urls import path

from .views import SubjectHome, SubjectDetail, SubjectSpecific
urlpatterns = [
    path('',  SubjectHome.as_view(), name='subject-home'),
    path('<int:subject_id>',  SubjectDetail.as_view(), name='subject-detail'),
    path('<str:row_prefix>/<int:row_id>',  SubjectSpecific.as_view(), name='subject-specific'),
]
