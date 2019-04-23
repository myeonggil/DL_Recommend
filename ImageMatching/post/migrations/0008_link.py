# Generated by Django 2.0.3 on 2018-08-11 11:21

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_learning_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', imagekit.models.fields.ProcessedImageField(upload_to='')),
                ('price', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
