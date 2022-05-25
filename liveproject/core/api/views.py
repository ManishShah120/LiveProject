from core.models import CustomUser, Vacation
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serielizers import CustomUserSerializer


class CustomUserListCreateView(ListCreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class CustomUserUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


customuserlistcreate = CustomUserListCreateView.as_view()
customuserupdate = CustomUserUpdateView.as_view()
