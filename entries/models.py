from django.db import models

class Entry(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='タイトル',
        help_text='タイトルを入力してください',
    )
    body = models.CharField(
        max_length=10000,
        verbose_name='本文',
        help_text='本文を入力してください',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "entries"

class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = "comments"
