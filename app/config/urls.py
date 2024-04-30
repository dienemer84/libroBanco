from django.contrib import admin
from django.urls import path, include
from core.homepage.views import IndexView
from core.login.views import *


from django.conf import settings
from django.conf.urls.static import static

from app.core.login.views import LoginFormView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('erp/', include('core.erp.urls')),
    path('admin/', admin.site.urls),
    path('login/', LoginFormView.as_view()),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)