# Generated by Django 2.2.24 on 2021-10-31 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20211031_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='framework',
            field=models.CharField(choices=[('Django', 'Django'), ('React Native', 'React Native')], max_length=50),
        ),
        migrations.AlterField(
            model_name='app',
            name='type',
            field=models.CharField(choices=[('Web', 'Web'), ('Mobile', 'Mobile')], max_length=50),
        ),
    ]
