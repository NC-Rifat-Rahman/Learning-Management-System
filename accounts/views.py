from rest_framework import generics, mixins, request, response, status
from .models import UserProfile
from .serializers import userSerializer, LoginSerializer
from django.db.models import Q
from .permissions import IsOwnerOrReadonly
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView


class userPostAPIiew(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field ='pk'
    serializer_class = userSerializer
    #queryset = UserProfile.objects.all()

    def get_queryset(self):
        qs= UserProfile.objects.all()
        query= self.request.GET.get("q")
        if query is not None:
            qs=qs.filter(Q(title__icontains=query)| Q(content__icontains=query)).distinct()
            return qs

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)


class userPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field ='pk'
    serializer_class = userSerializer
    #queryset = UserProfile.objects.all()
    permission_classes = [IsOwnerOrReadonly]

    def get_queryset(self):
        return UserProfile.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}



class LoginAPIView(GenericAPIView):

    serializer_class = LoginSerializer
    def post(self,request):
      #email = request.data.get('email', None)
      password= request.data.get('password', None)

      user = authenticate( password=password)

      if user:
        serializer = self.serializer_class(user)

        return response.Response(serializer.data,status=status.HTTP_200_OK)
      return response.Response({'message':"Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)