# Generated by Django 4.2.4 on 2023-08-06 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('contenido', models.TextField(max_length=30000)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='temas/')),
                ('video', models.FileField(blank=True, null=True, upload_to='temas/')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField(max_length=30000)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='comentarios/')),
                ('video', models.FileField(blank=True, null=True, upload_to='comentarios/')),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foro.tema')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
