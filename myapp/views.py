from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from django.views.decorators.csrf import ensure_csrf_cookie


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = '__all__'


class VoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = '__all__'


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = models.UserInfo.objects.all()


class InvoiceView(viewsets.ModelViewSet):
    serializer_class = VoiceSerializer
    queryset = models.Invoice.objects.all()



class InvoiceList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        tguserid = self.request.query_params.get('tgUserId')
        print(tguserid)
        if tguserid is not None:
            queryset = models.UserInfo.objects.filter(tgUserId=tguserid)
            # print(queryset)
        print(queryset)
        return queryset


#
# class VoiceApi(APIView):
#     def get(self, *args, **kwargs):
#         all_voices = models.Voice.objects.all()
#         serilized_voices = VoiceSerializer(all_voices, many=True)
#         return Response(serilized_voices.data)
#
#

class UserList(generics.ListAPIView):
    serializer_class = VoiceSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = models.Invoice.objects.all()
        invoiceid = self.request.query_params.get('inVoiceId')
        if invoiceid is not None:
            queryset = queryset.filter(invoiceId=invoiceid)
            # print(queryset)
        print(queryset)
        return queryset

#     elif request.method == 'POST':
#         serializer = VoiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# @api_view(['GET', 'POST', 'PATCH'])
# def user_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         users = models.UserInfo.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# elif request.method == 'PATCH':
#     serializer = UserSerializerFor(request.user, data=request.data, partial=True)
#
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = TimeSerializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(customer_id=customer, **serializer.validated_data)
#         return Response(serializer.validated_data)
#     if serializer.is_valid():
#         serializer.save()
#         print(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
