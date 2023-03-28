# Generated by Django 4.1.7 on 2023-03-28 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0002_ability_hero_ability_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hero1', to='heroes.hero')),
                ('hero2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hero2', to='heroes.hero')),
                ('relationship_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='heroes.relationshiptype')),
            ],
        ),
    ]
