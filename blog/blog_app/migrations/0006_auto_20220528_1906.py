# Generated by Django 3.2.12 on 2022-05-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_auto_20220525_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextended',
            name='userpic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='comments',
            name='images',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='news',
            name='images',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos'),
        ),
    ]
