# Generated by Django 4.2.11 on 2024-05-01 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='productsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sari_Name', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Image', models.ImageField(upload_to='images/')),
                ('Price', models.TextField()),
                ('LDescription', models.TextField()),
                ('Size', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sari_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('number', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
