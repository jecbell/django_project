# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0002_auto_20151122_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='user',
        ),
        migrations.RemoveField(
            model_name='uploadimage',
            name='upload',
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='filename',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
    ]
