# Generated by Django 4.1.4 on 2022-12-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='saving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=26)),
                ('dept_city', models.CharField(max_length=24)),
            ],
        ),
        migrations.AlterField(
            model_name='emp',
            name='dept_id',
            field=models.IntegerField(),
        ),
    ]
