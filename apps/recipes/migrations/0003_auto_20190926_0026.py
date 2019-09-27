<<<<<<< HEAD
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-26 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0001_initial'),
        ('recipes', '0002_auto_20190925_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_creator', to='login_reg.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_users',
            field=models.ManyToManyField(related_name='recipes_tried', to='login_reg.User'),
        ),
    ]
=======
# -- coding: utf-8 --
# Generated by Django 1.10 on 2019-09-26 00:26
from __future__ import unicode_literals
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
   dependencies = [
       ('login_reg', '0001_initial'),
       ('recipes', '0002_auto_20190925_2005'),
   ]
   operations = [
       migrations.AddField(
           model_name='recipe',
           name='creator',
           field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_creator', to='login_reg.User'),
           preserve_default=False,
       ),
       migrations.AddField(
           model_name='recipe',
           name='recipe_users',
           field=models.ManyToManyField(related_name='recipes_tried', to='login_reg.User'),
       ),
   ]
>>>>>>> 559a9f0b7fed41ef55b2758a6cd7689ad82aacf6