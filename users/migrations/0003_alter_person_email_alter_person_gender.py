# Generated by Django 4.0.4 on 2022-06-01 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_person_years_of_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F')], max_length=1, null=True),
        ),
    ]