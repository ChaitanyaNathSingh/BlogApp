# Generated by Django 4.1.2 on 2022-10-15 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_alter_post_publish_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
