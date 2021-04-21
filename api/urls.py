from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('global_event/', login_required(GlobalEventList.as_view())),
    path('global_event/<int:pk>', GlobalEventDetail.as_view()),

    path('trp/', TRPBadgeList.as_view()),
    path('trp/<int:pk>', TRPBadgeDetail.as_view()),

    path('national/', NationalPartList.as_view()),
    path('national/<int:pk>', NationalPartDetail.as_view()),

    path('not_national/', NotNationalPartList.as_view()),
    path('not_national/<int:pk>', NotNationalPartDetail.as_view()),

    path('online_event/', OnlineList.as_view()),
    path('online_event/<int:pk>', OnlineDetail.as_view()),

    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social'))

]

urlpatterns = format_suffix_patterns(urlpatterns)
