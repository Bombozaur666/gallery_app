from django.core.exceptions import ValidationError
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import subjects
from .serializers import SubjectSerializer
# Create your views here.


class SubjectHome(GenericAPIView):
    def get(self, *args, **kwargs):
        queryset = subjects.objects.filter(site=self.kwargs['site_id'])
        serializer = SubjectSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        schema = self.request.data['schema']
        batch = []
        for name in schema:
            batch.append(subjects(name=name, site_id=self.kwargs['site_id']))
            try:
                batch[-1].full_clean()
            except ValidationError:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        subjects.objects.bulk_create(batch, len(batch))
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubjectDetail(GenericAPIView):
    def get(self, *args, **kwargs):
        _subject = get_object_or_404(subjects, pk=self.kwargs['subject_id'], site=self.kwargs['site_id'])
        serializer = SubjectSerializer(_subject, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        _subject = get_object_or_404(subjects, pk=self.kwargs['subject_id'], site=self.kwargs['site_id'])
        _subject.name = self.request.data['schema']
        _subject.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, *args, **kwargs):
        subjects.objects.get(pk=self.kwargs['subject_id'], site=self.kwargs['site_id']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubjectSpecific(GenericAPIView):
    def get(self, *args, **kwargs):
        _subject = get_list_or_404(subjects, row_id=self.kwargs['row_id'], row_prefix=self.kwargs['row_prefix'])
        serializer = SubjectSerializer(_subject, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        _subject = subjects(name=self.request.data['schema'], row_id=self.kwargs['row_id'], row_prefix=self.kwargs['row_prefix'], site_id=self.kwargs['site_id'])
        try:
            _subject.full_clean()
        except ValidationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        _subject.save()
        return Response(status=status.HTTP_204_NO_CONTENT)








