# Generated by Django 4.0.6 on 2024-10-07 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_category_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='desc',
            field=models.TextField(max_length=2555, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(null=True, upload_to='category-img'),
        ),
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=models.TextField(max_length=2555, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=2555),
        ),
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.TextField(max_length=2555),
        ),
    ]