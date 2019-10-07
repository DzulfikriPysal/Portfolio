from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('default.urls')),
    path('user/', include('user.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
