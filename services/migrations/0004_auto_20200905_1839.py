# Generated by Django 3.0.3 on 2020-09-05 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20200905_0052'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.AlterField(
            model_name='person',
            name='category',
            field=models.CharField(max_length=50),
        ),
    ]
