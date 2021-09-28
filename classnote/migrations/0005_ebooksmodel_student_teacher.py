# Generated by Django 3.2.6 on 2021-09-10 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classnote', '0004_alter_classroom_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='EBooksModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('pdf', models.FileField(upload_to='pdfs/')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191, null=True)),
                ('studentId', models.CharField(max_length=12, null=True)),
                ('age', models.CharField(max_length=20, null=True)),
                ('username', models.CharField(max_length=20, null=True)),
                ('course', models.CharField(max_length=191, null=True)),
                ('phone', models.CharField(max_length=191, null=True)),
                ('email', models.CharField(max_length=191, null=True)),
                ('password', models.CharField(max_length=15, null=True)),
                ('photo', models.ImageField(upload_to='')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191, null=True)),
                ('initials', models.CharField(max_length=10, null=True)),
                ('course', models.CharField(max_length=191, null=True)),
                ('phone', models.CharField(max_length=191, null=True)),
                ('email', models.CharField(max_length=191, null=True)),
                ('password', models.CharField(max_length=15, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]