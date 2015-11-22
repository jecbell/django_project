# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0003_auto_20151122_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadimage',
            old_name='filename',
            new_name='image',
        ),
    ]
