from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
# from drf_yasg.views get_scheme_view
# from drf_yasg import openapi
#
# schema_view = get_schema_view(
#     openapi.Info(
#         title ="Book list Api",
#         default_version='v1',
#         description='Library demo project',
#         terms_of_service='demo.com',
#         contact=openapi.Contact(email=''),
#         license=openapi.License
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny, ],
# )



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',  include('books.urls'))
]
