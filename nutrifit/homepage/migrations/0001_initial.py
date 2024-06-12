# Generated by Django 4.0 on 2024-06-06 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sexo', models.CharField(max_length=10)),
                ('estatura', models.IntegerField()),
                ('peso_act', models.FloatField(max_length=5)),
                ('peso_des', models.FloatField(max_length=5)),
                ('edad', models.IntegerField()),
                ('nivel_actividad', models.CharField(max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Historico_micronutrientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('calcium', models.FloatField(max_length=6)),
                ('chromium', models.FloatField(max_length=5)),
                ('copper', models.FloatField(max_length=5)),
                ('fluoride', models.FloatField(max_length=5)),
                ('iodine', models.FloatField(max_length=4)),
                ('iron', models.FloatField(max_length=4)),
                ('magnesium', models.FloatField(max_length=5)),
                ('manganese', models.FloatField(max_length=4)),
                ('molybdenum', models.FloatField(max_length=4)),
                ('phosphorus', models.FloatField(max_length=5)),
                ('selenium', models.FloatField(max_length=4)),
                ('zinc', models.FloatField(max_length=4)),
                ('potassium', models.FloatField(max_length=6)),
                ('sodium', models.FloatField(max_length=6)),
                ('chloride', models.FloatField(max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField()),
                ('tdee', models.FloatField(max_length=15)),
                ('peso', models.FloatField(max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
