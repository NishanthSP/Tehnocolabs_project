# Generated by Django 3.1.7 on 2021-06-27 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Best_seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
                ('design', models.TextField(default='STUDIO DESIGN')),
                ('cost_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('discount_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('discount_percent', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
