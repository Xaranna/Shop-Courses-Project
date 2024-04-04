from api.models import CourseResource, CategoryResource
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name='v1')
api.register(CourseResource())
api.register(CategoryResource())

# api/v1/courses/        GET, POST
# api/v1/courses/1/      GET, DELETE
# api/v1/categories/     GET
# api/v1/categories/1/   GET

# FOR POST, DELETE add header
# Key: Authorization
# Value: ApiKey admin:admin12345

urlpatterns = [
    path('', include(api.urls), name='index')
]
