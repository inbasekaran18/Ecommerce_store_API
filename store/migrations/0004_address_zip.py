# Generated by Django 4.1.5 on 2023-01-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default='Null', max_length=255),
            preserve_default=False,
        ),
    ]
