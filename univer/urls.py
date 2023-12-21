from django.contrib import admin
from django.urls import path, include
from project.views import index, ProductSearchView, ProductDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('search', ProductSearchView.as_view(), name="post-search")
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)