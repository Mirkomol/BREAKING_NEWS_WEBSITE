# Generated by Django 3.2 on 2021-06-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_latest_post',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='business_pics'),
        ),
        migrations.AlterField(
            model_name='business_post',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='business_pics'),
        ),
        migrations.AlterField(
            model_name='business_trending_post',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='business_pics'),
        ),
        migrations.AlterField(
            model_name='it_post',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='it_pics'),
        ),
    ]