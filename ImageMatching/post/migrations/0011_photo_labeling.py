# Generated by Django 2.0.3 on 2018-11-28 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_google_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo_Labeling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('post_label', models.CharField(max_length=255)),
            ],
        ),
    ]
