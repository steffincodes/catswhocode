# Generated by Django 4.0.4 on 2022-06-28 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_meow_options_alter_catroom_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catroom',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='catroom',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='meow',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='meow',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
