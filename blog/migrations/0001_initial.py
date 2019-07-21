# Generated by Django 2.2.3 on 2019-07-21 07:21

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
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('time_created', models.DateTimeField()),
                ('price', models.IntegerField(choices=[(0, 500), (1, 1000), (2, 1500), (3, 2000), (4, 2500), (5, 3000), (6, 3500), (7, 4000), (8, 4500), (9, 5000)])),
                ('selected', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('time_created', models.DateTimeField()),
                ('selected', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Question')),
            ],
        ),
    ]
