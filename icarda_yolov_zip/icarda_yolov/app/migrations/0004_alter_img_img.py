# Generated by Django 3.2.9 on 2021-12-29 10:15

import app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_img_predited_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='image/test/', validators=[app.validators.validate_file_size]),
        ),
    ]
