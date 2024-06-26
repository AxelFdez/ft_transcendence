# Generated by Django 3.2.4 on 2024-04-15 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('final_score', models.CharField(default='0:0', max_length=25)),
                ('game_type', models.CharField(default=None, max_length=25)),
                ('difficulty', models.CharField(default=None, max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('player_one', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_one', to='account.userprofile')),
                ('player_two', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_two', to='account.userprofile')),
                ('winner', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='account.userprofile')),
            ],
        ),
    ]
