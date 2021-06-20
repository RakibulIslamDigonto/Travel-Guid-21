from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve as mediaserve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Login_app2.urls')),
    path('', include('Blog_app.urls', namespace='Blog_app')),
    path('summernote/', include('django_summernote.urls'))
]

urlpatterns.append(url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
                       mediaserve, {'document_root': settings.MEDIA_ROOT}))

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
