# Generated by Django 4.0.6 on 2024-10-08 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body1',
            field=models.TextField(max_length=2555, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body2',
            field=models.TextField(max_length=2555, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body3',
            field=models.TextField(max_length=2555, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='section1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='section2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='section3',
            field=models.CharField(max_length=255, null=True),
        ),
    ]