# Generated by Django 4.1.7 on 2023-03-28 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='heroes.abilitytype')),
                ('hero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='heroes.hero')),
            ],
        ),
        migrations.AddField(
            model_name='hero',
            name='ability_types',
            field=models.ManyToManyField(through='heroes.Ability', to='heroes.abilitytype'),
        ),
    ]