# Generated by Django 2.0.7 on 2020-09-12 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Category Name')),
                ('type', models.CharField(choices=[('e', 'Electronic'), ('s', 'Sculpture'), ('t', 'Toys'), ('f', 'Furniture')], default='1', max_length=20, verbose_name='Category Type')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sub-Category Name')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='category_management.Category')),
            ],
            options={
                'verbose_name': 'Sub - Category',
                'verbose_name_plural': 'Sub - Categories',
            },
        ),
    ]
