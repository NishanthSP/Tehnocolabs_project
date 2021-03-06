# Generated by Django 3.1.7 on 2021-06-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organic', '0005_auto_20210627_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Banner_products')),
            ],
        ),
        migrations.CreateModel(
            name='Brand_logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_image', models.ImageField(upload_to='Brand_logo')),
            ],
        ),
        migrations.CreateModel(
            name='Featured_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('image', models.ImageField(upload_to='organic_product')),
                ('design', models.TextField(default='STUDIO DESIGN')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('new_tag', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hot_deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('image', models.ImageField(upload_to='organic_product')),
                ('design', models.TextField(default='STUDIO DESIGN')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('new_tag', models.BooleanField(default=False)),
                ('availability', models.IntegerField()),
                ('time_left', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='New_arrivals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('image', models.ImageField(upload_to='organic_product')),
                ('design', models.TextField(default='STUDIO DESIGN')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('new_tag', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Popular_categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_img', models.ImageField(upload_to='category')),
                ('product_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recently_added',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('image', models.ImageField(upload_to='organic_product')),
                ('design', models.TextField(default='STUDIO DESIGN')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('new_tag', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_1', models.CharField(max_length=255)),
                ('header_2', models.CharField(max_length=255)),
                ('header_3', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='slider_products')),
            ],
        ),
    ]
