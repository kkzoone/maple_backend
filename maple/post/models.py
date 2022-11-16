from django.db import models
# 게시글 모델:
# 제목
# 사진
# 글
# 작성날짜
# 카테고리 케이크/스콘/휘낭시에/쿠키
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    createdAt = models.DateField(auto_now_add=True,null=True)
    opt1 = "케이크"
    opt2 = "스콘"
    opt3 = "휘낭시에"
    opt4 = "쿠키"
    CHOICES = ((opt1, "케이크"), (opt2, "스콘"), (opt3, "휘낭시에"),
               (opt4, "쿠키"))
    category = models.CharField(
        choices=CHOICES, max_length=50, null=True, blank=True
    )
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'post'
        ordering = ['-createdAt']   

class PostPicture(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postpicture')
    picture = models.ImageField(default=None,null=True, upload_to='postpictures/')

    class Meta:
        db_table="post_picture"