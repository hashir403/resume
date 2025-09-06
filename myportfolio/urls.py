
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('project', views.project_list, name='project'),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
]
if settings.DEBUG:  # sirf development ke liye
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)