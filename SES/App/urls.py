from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index),
    path('upload/rubric/', views.upload_rubric, name='upload_rubric'),
    path('upload/essay/', views.upload_essay, name='upload_essay'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)