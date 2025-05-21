from django.db import models


class Post(models.Model):
    title = models.CharField(max_length= 100, blank= False) # 제목이 없으면 말이 안되지요.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title

class Comment(models.Model):   
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"댓글: {self.content[:20]}"