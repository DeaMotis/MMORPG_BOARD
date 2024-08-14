from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    USER_CATEGORY = (('Tank', 'Танк'),
                     ('Healer', 'Хил'),
                     ('Damage_Dealer', 'ДД'),
                     ('Merchant', 'Торговец'),
                     ('Guild_Master', 'Гильдмастер'),
                     ('Quest_Giver', 'Квестгивер'),
                     ('Blacksmith', 'Кузнец'),
                     ('Leatherworker', 'Кожевник'),
                     ('Potions_Master', 'Зельевар'),
                     ('Spell_Master', 'Мастер заклинаний'))
    category = models.CharField(max_length=32, choices=USER_CATEGORY, verbose_name='Категория')
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def get_absolute_url(self):
        return reverse('post', kwargs={'id': self.id, 'name': self.name})

    def __str__(self):
        return self.title
class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)
