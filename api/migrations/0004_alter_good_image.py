# Generated by Django 5.1.3 on 2024-12-01 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_good_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
