from .models import Post,PostPicture
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    pictures = serializers.SerializerMethodField() 

    def get_pictures(self, obj):
        picture = obj.postpicture.all()
        # post에있는 사진들을 모두 가져와라 
        # queryset 형태로 pictuer에 넣어둠 -> 시리얼라이저 매개변수로 인스턴스에 쿼리셋을 넣어줌
        # many =ture -> 사진이 많음
        # context -> urldl 절대경로로 안 나옴
        return PostPictureSerializer(instance=picture, many=True, context=self.context).data 
    
    class Meta:
        model = Post
        fields = ['title','content','createdAt','category','pictures']
        
    def create(self, validated_data):
        instance = Post.objects.create(**validated_data)
        postpicture_set = self.context['request'].FILES
        for pic_data in postpicture_set.getlist('picture'):
            PostPicture.objects.create(post=instance, picture=pic_data)
        return instance

class PostPictureSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(use_url=True)
    class Meta:
        model = PostPicture
        fields = ['picture']