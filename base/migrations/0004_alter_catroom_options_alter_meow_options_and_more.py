# Generated by Django 4.0.4 on 2022-06-28 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_catroom_hostcat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catroom',
            options={'ordering': ['-updated', 'created']},
        ),
        migrations.AlterModelOptions(
            name='meow',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.RenameField(
            model_name='meow',
            old_name='cat_room',
            new_name='catRoom',
        ),
    ]