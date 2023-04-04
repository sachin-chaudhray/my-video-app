from django.urls import path
from .views import upload_video,video_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', upload_video, name='upload_video'),
    path('view/', video_list, name='video_list' )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
