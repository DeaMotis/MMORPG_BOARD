from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)



