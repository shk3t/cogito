# Generated by Django 4.0.4 on 2022-05-09 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_cluster_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='author',
            field=models.CharField(default='nice', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cluster',
            name='parent_cluster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.cluster'),
        ),
        migrations.AlterField(
            model_name='source',
            name='cluster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.cluster'),
        ),
    ]