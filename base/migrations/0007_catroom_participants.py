# Generated by Django 4.0.4 on 2022-06-28 05:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0006_alter_catroom_created_alter_catroom_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='catroom',
            name='participants',
            field=models.ManyToManyField(related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
