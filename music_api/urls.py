from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from catalogue import views
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'albums', views.AlbumViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('hello_world/', views.hello_world, name="hello-world"),
    # path('artists/', views.ArtistView.as_view(), name ="Artist")
    path('artists/', views.ArtistView.as_view(), name='artists'),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view(), name='artists'),
    path(r'openapi-schem', get_schema_view(
        title="Music Api",
        description="Music Catalogue API",
        version="1.0.0",
        public=True,
    ), name='openapi-schema'),

    path('docs/', TemplateView.as_view(
        template_name='catalog/swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}),
         name='swagger-ui'
         )

]
