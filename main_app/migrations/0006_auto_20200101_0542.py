# Generated by Django 2.2.6 on 2020-01-01 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='reviews',
            field=models.ManyToManyField(to='main_app.Review'),
        ),
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
