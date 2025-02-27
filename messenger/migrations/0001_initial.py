# Generated by Django 5.1.4 on 2024-12-12 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('avatar', models.ImageField(null=True, upload_to='avatars/chat/')),
                ('max_participants', models.PositiveIntegerField(default=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('chatroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='messenger.chatroom')),
            ],
            bases=('messenger.chatroom',),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('chatroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='messenger.chatroom')),
            ],
            bases=('messenger.chatroom',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visibleName', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('avatar', models.ImageField(null=True, upload_to='avatars/user/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chatroom', models.ManyToManyField(null=True, related_name='chatrooms_with_users', to='messenger.chatroom')),
                ('chat', models.ManyToManyField(null=True, related_name='chats_with_users', to='messenger.chat')),
                ('favorite', models.ManyToManyField(null=True, related_name='favorite_for_user', to='messenger.favorite')),
            ],
        ),
        migrations.AddField(
            model_name='chatroom',
            name='participants',
            field=models.ManyToManyField(null=True, related_name='chatrooms', to='messenger.user'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messenger.user')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messenger.chat')),
            ],
        ),
    ]
