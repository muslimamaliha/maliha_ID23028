from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('student_app.urls')),
    path('', RedirectView.as_view(url='/students/')),  # redirect root to /students/
]
