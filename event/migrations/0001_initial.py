# Generated by Django 2.2.16 on 2020-09-10 06:41

from django.db import migrations, models
import django.db.models.deletion
import event.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrideGroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bridegroom', models.CharField(choices=[('bride', 'Bride'), ('groom', 'Groom')], max_length=100, verbose_name='Bride/Groom')),
                ('name', models.CharField(max_length=100, verbose_name='Fullname')),
                ('short_name', models.CharField(max_length=100, verbose_name='Shortname')),
                ('mother', models.CharField(max_length=100, verbose_name='Mother')),
                ('father', models.CharField(max_length=100, verbose_name='Father')),
                ('image', models.ImageField(blank=True, height_field='image_height', upload_to=event.models.UploadImage('bridegroom-images/'), width_field='image_width')),
                ('image_width', models.PositiveIntegerField(default=0)),
                ('image_height', models.PositiveIntegerField(default=0)),
                ('dt_add', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_ceremony', models.DateField(verbose_name='Ceremony (Date)')),
                ('d_reception', models.DateField(verbose_name='Reception (Date)')),
                ('p_ceremony', models.CharField(max_length=100, verbose_name='Ceremony (Time)')),
                ('p_reception', models.CharField(max_length=100, verbose_name='Reception (Time)')),
                ('image', models.ImageField(blank=True, height_field='image_height', upload_to=event.models.UploadImage('event-images/'), width_field='image_width')),
                ('image_width', models.PositiveIntegerField(default=0)),
                ('image_height', models.PositiveIntegerField(default=0)),
                ('dt_add', models.DateTimeField(auto_now_add=True)),
                ('bride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bride_event_set', to='event.BrideGroom', verbose_name='Bride')),
                ('groom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groom_event_set', to='event.BrideGroom', verbose_name='Groom')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('phone', models.CharField(max_length=16, verbose_name='Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('lat', models.DecimalField(decimal_places=8, max_digits=10, verbose_name='Latitude')),
                ('lng', models.DecimalField(decimal_places=8, max_digits=11, verbose_name='Longitude')),
                ('image', models.ImageField(blank=True, height_field='image_height', upload_to=event.models.UploadImage('venue-images/'), width_field='image_width')),
                ('image_width', models.PositiveIntegerField(default=0)),
                ('image_height', models.PositiveIntegerField(default=0)),
                ('dt_add', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('is_attend', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event', verbose_name='Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('image', models.ImageField(blank=True, height_field='image_height', upload_to=event.models.UploadImage('gallery-images/'), width_field='image_width')),
                ('image_width', models.PositiveIntegerField(default=0)),
                ('image_height', models.PositiveIntegerField(default=0)),
                ('dt_add', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event', verbose_name='Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Venue', verbose_name='Venue'),
        ),
        migrations.CreateModel(
            name='CongratulationWhises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('invitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Invitation', verbose_name='Invitation')),
            ],
        ),
    ]
