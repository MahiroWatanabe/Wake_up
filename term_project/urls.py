from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("wake_up.urls")),
    path('blog/', include("blog.urls")),
    path('accounts/', include("accounts.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
]
