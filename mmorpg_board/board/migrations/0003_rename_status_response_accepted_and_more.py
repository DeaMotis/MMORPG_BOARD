# Generated by Django 4.2.1 on 2024-08-17 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_post_image_alter_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='status',
            new_name='accepted',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='post',
            new_name='ad',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='dateCreation',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='response',
            name='text',
        ),
        migrations.AddField(
            model_name='response',
            name='message',
            field=models.TextField(default='Нет сообщения'),
        ),
    ]