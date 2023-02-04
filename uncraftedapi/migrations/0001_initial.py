# Generated by Django 4.1.5 on 2023-02-04 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('message_content', models.CharField(max_length=1000)),
                ('is_new', models.BooleanField()),
                ('connected_to_trade', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
                ('image_url', models.URLField()),
                ('trade_preferences', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('is_draft', models.BooleanField(default=False)),
                ('is_pending', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_pending', models.BooleanField(default=True)),
                ('item_offered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post2', to='uncraftedapi.post')),
                ('item_wanted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post1', to='uncraftedapi.post')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('favorite_craft', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('about', models.CharField(max_length=1000)),
                ('profile_image_url', models.URLField()),
                ('instagram', models.URLField()),
                ('etsy', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TradeMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uncraftedapi.message')),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uncraftedapi.trade')),
            ],
        ),
        migrations.AddField(
            model_name='trade',
            name='trade_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tradeuser', to='uncraftedapi.user'),
        ),
        migrations.AddField(
            model_name='post',
            name='owner_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='uncraftedapi.user'),
        ),
        migrations.AddField(
            model_name='post',
            name='posted_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='uncraftedapi.user'),
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messageuser2', to='uncraftedapi.user'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messageuser1', to='uncraftedapi.user'),
        ),
    ]
