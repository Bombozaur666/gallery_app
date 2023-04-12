from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .models import photo, gallery
from rest_framework.generics import GenericAPIView
from .serializer import SimpleGallerySerializer, PhotoSerializer, GallerySerializer
from django.core.exceptions import ValidationError

# Create your views here.


class Home(GenericAPIView):
    def get(self, *args, **kwargs):
        _gallery = gallery.objects.filter(site=self.kwargs['site_id'])
        serializer = SimpleGallerySerializer(_gallery, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, *args,  **kwargs):
        data = self.request.data
        _gallery = gallery(name=data['name'],
                           description=data['description'],
                           sort_value=data['sort_value'],
                           private=data['private'],
                           site_id=self.kwargs['site_id'])
        try:
            _gallery.full_clean()
        except ValidationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        _gallery.save()
        return Response(status=status.HTTP_201_CREATED)


class GalleryDetails(GenericAPIView):
    def get(self, *args,  **kwargs):
        _photos = get_list_or_404(photo,
                                  gallery_photos__pk=self.kwargs['gallery_id'],
                                  gallery_photos__site=self.kwargs['site_id'])
        serializer_photo = PhotoSerializer(_photos, many=True)
        _gallery = get_object_or_404(gallery,
                                     pk=self.kwargs['gallery_id'],
                                     site=self.kwargs['site_id'])
        serializer_gallery = GallerySerializer(_gallery, many=False)
        return Response(data={"gallery": serializer_gallery.data, "photos": serializer_photo.data},
                        status=status.HTTP_200_OK)

    def post(self, *args,  **kwargs):
        _gallery = get_object_or_404(gallery, pk=self.kwargs['gallery_id'], site=self.kwargs['site_id'])
        for _photo in self.request.data['photos']:
            _gallery.photos.add(get_object_or_404(photo, pk=_photo))
        try:
            _gallery.full_clean()
        except ValidationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        _gallery.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, *args,  **kwargs):
        _gallery = get_object_or_404(gallery, pk=self.kwargs['gallery_id'], site=self.kwargs['site_id'])
        if 'name' in self.request.data:
            _gallery = self.request.data['name']
        if 'description' in self.request.data:
            _gallery = self.request.data['description']
        try:
            _gallery.full_clean()
        except ValidationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        _gallery.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, *args,  **kwargs):
        _gallery = get_object_or_404(gallery, pk=self.kwargs['gallery_id'], site=self.kwargs['site_id'])
        if self.request.data['photo'] in _gallery.photos:
            _gallery.photos.remove(get_object_or_404(photo, pk=self.request.data['photo']))
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        _gallery.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GalleryMoveUp(GenericAPIView):
    def put(self, *args, **kwargs):
        obj = get_object_or_404(gallery, pk=self.kwargs['gallery_id'], site=self.kwargs['site_id'])
        obj.sort_value += 1
        obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GalleryMoveDown(GenericAPIView):
    def put(self, *args, **kwargs):
        obj = get_object_or_404(gallery, pk=self.kwargs['gallery_id'], site=self.kwargs['site_id'])
        obj.sort_value -= 1
        obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateManyPhotos(GenericAPIView):
    def put(self, *args, **kwargs):
        photos_ids = gallery.objects.filter(pk=self.kwargs['gallery_id'], site=self.kwargs['site_id']).values_list(
            'photos__pk', flat=True)
        for _id in self.request.data['photos']:
            if _id['id'] not in photos_ids:
                return Response(status=status.HTTP_400_BAD_REQUESTT)

        batch = []
        for photo_to_update in self.request.data['photos']:
            _photo = photo.objects.get(pk=photo_to_update['id'])
            _photo.description = photo_to_update['description']
            batch.append(_photo)
        photo.objects.bulk_update(batch, ['description'], len(batch))
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhotoManagement(GenericAPIView):
    def delete(self, *args, **kwargs):
        _gallery = gallery.objects.get(pk=self.kwargs['gallery_id'],
                                       site=self.kwargs['site_id'])
        _gallery.photos.remove(photo.objects.get(pk=self.kwargs['photo_id']))
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, *args, **kwargs):
        _photo = photo.objects.get(gallery_photos__pk=self.kwargs['gallery_id'],
                                   gallery_photos__site=self.kwargs['site_id'],
                                   pk=self.kwargs['photo_id'])
        _photo.photo = self.request.data['file']
        _photo.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdatePhoto(GenericAPIView):
    def put(self, *args, **kwargs):
        _photo = photo.objects.get(gallery_photos__pk=self.kwargs['gallery_id'],
                                   gallery_photos__site=self.kwargs['site_id'],
                                   pk=self.kwargs['photo_id'])
        _photo.description = self.request.data['description']
        _photo.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhotoMoveUp(GenericAPIView):
    def put(self, *args, **kwargs):
        _photo = photo.objects.get(gallery_photos__pk=self.kwargs['gallery_id'],
                                   gallery_photos__site=self.kwargs['site_id'],
                                   pk=self.kwargs['photo_id'])
        _photo.sort_value += 1
        _photo.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhotoMoveDown(GenericAPIView):
    def put(self, *args, **kwargs):
        _photo = photo.objects.get(gallery_photos__pk=self.kwargs['gallery_id'],
                                   gallery_photos__site=self.kwargs['site_id'],
                                   pk=self.kwargs['photo_id'])
        _photo.sort_value -= 1
        _photo.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

















