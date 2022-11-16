from .models import Post
from .serializer import PostSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

#Post의 목록 , detail 보여주기, 수정하기 , 삭제하기 모두 기능
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [SearchFilter]
    search_fields = ['title']

