# Generated by Django 4.2.1 on 2024-07-30 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Tank', 'Танк'), ('Healer', 'Хил'), ('Damage_Dealer', 'ДД'), ('Merchant', 'Торговец'), ('Guild_Master', 'Гильдмастер'), ('Quest_Giver', 'Квестгивер'), ('Blacksmith', 'Кузнец'), ('Leatherworker', 'Кожевник'), ('Potions_Master', 'Зельевар'), ('Spell_Master', 'Мастер заклинаний')], max_length=32, verbose_name='Категория')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('text', models.TextField()),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('status', models.BooleanField(default=False)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.post')),
            ],
        ),
    ]
