# Generated by Django 3.2 on 2021-04-23 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Storage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(default='picture.jbg', upload_to='', verbose_name='Product Image'),
            preserve_default=False,
        ),
    ]
