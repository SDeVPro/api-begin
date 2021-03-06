# Generated by Django 3.2.4 on 2021-06-22 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Nomi')),
            ],
            options={
                'verbose_name': 'Rubrika',
                'verbose_name_plural': 'Rubrikalar',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='elon')),
                ('content', models.TextField(blank=True, null=True, verbose_name='mazmuni')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='narx')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='chop qilingan sana')),
                ('rubric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bboard.rubric')),
            ],
            options={
                'verbose_name': "E'lon",
                'verbose_name_plural': "E'lonlar",
                'ordering': ['-published'],
            },
        ),
    ]
