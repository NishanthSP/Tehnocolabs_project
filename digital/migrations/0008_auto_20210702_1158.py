# Generated by Django 3.1.7 on 2021-07-02 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0007_microphones'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='digital_prod',
            new_name='digital_products',
        ),
        migrations.DeleteModel(
            name='Microphones',
        ),
    ]
