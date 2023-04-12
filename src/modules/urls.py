from django.urls import path, include

import gallery.urls
import subjects.urls

urlpatterns = [
    path('gallery/', include(gallery.urls)),
    path('subject/', include(subjects.urls)),
]
