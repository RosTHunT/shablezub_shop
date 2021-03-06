# Generated by Django 4.0.3 on 2022-05-05 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Назва категорії')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Категорія ',
                'verbose_name_plural': 'Категорії',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('content', models.TextField(blank=True, verbose_name='Опис')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('in_stock', models.BooleanField(default=True, verbose_name='В наявності')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубліковано')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Товар ',
                'verbose_name_plural': 'Товари',
                'ordering': ['-created', 'name'],
            },
        ),
    ]
