from django.urls import path, include
from akroapp import views
from rest_framework.routers import DefaultRouter

'''exercise_list = ExerciseViewSet.as_view({'get': 'list', 'post': 'create'})
exercise_detail = ExerciseViewSet.as_view({ 'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
'''

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'exercises', views.ExerciseViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'users', views.UserViewSet)
urlpatterns = [
    path('',include(router.urls))
]

#urlpatterns = format_suffix_patterns(urlpatterns)
