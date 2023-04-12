from django.urls import path
from .views import Home, GalleryDetails, GalleryMoveUp, GalleryMoveDown, UpdateManyPhotos, PhotoManagement, UpdatePhoto, PhotoMoveUp, PhotoMoveDown

urlpatterns = [
    path('',  Home.as_view(), name='gallery-home'),
    path('<int:gallery_id>/', GalleryDetails.as_view(), name='gallery-photos'),
    path('<int:gallery_id>/move_up/', GalleryMoveUp.as_view(), name='gallery-move-up'),
    path('<int:gallery_id>/move_down/', GalleryMoveDown.as_view(), name='gallery-move-down'),
    path('<int:gallery_id>/photos/update/', UpdateManyPhotos.as_view(), name='gallery-update-many-photos'),
    path('<int:gallery_id>/photo/<int:photo_id>/', PhotoManagement.as_view(), name='gallery-photo'),
    path('<int:gallery_id>/photo/<int:photo_id>/update', UpdatePhoto.as_view(), name='gallery-update-photo'),
    path('<int:gallery_id>/photo/<int:photo_id>/move_up', PhotoMoveUp.as_view(), name='gallery-photo-move-up'),
    path('<int:gallery_id>/photo/<int:photo_id>/move_down', PhotoMoveDown.as_view(), name='gallery-photo-move-down'),
]
