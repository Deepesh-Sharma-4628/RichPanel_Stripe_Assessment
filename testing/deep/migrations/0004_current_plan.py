# Generated by Django 4.2.4 on 2023-08-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deep', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='current_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_type', models.CharField(max_length=50)),
                ('Plan_Name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
