# Generated by Django 5.1.3 on 2024-11-14 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_basket_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterModelOptions(
            name='basketitem',
            options={'verbose_name': 'Товар в корзине', 'verbose_name_plural': 'Товары в корзине'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='good',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='recipient',
            options={'verbose_name': 'Получатель', 'verbose_name_plural': 'Получатели'},
        ),
    ]