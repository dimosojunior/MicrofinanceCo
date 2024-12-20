# Generated by Django 4.2.6 on 2024-12-08 07:41

import App.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MalipoYaFainiCopies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(blank=True, max_length=100000, null=True, verbose_name='Namba Ya Mteja')),
                ('JinaKamiliLaMteja', models.CharField(blank=True, max_length=500, null=True, verbose_name='Jina Kamili La Mteja')),
                ('JinaLaKituo', models.CharField(blank=True, max_length=500, null=True, verbose_name='Jina La Kituo Cha Mteja')),
                ('SimuYaMteja', models.IntegerField(blank=True, null=True, verbose_name='Namba Ya Simu Ya Mteja')),
                ('EmailYaMteja', models.EmailField(blank=True, max_length=500, null=True, verbose_name='Email Ya Mteja')),
                ('Mahali', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mahali Anapoishi')),
                ('KiasiAnachokopa', models.IntegerField(blank=True, default=0, null=True, verbose_name='Kiasi Anachokopa')),
                ('KiasiAlicholipa', models.IntegerField(blank=True, default=0, null=True, verbose_name='Kiasi Alicholipa')),
                ('RejeshoKwaSiku', models.IntegerField(blank=True, default=0, null=True, verbose_name='Rejesho Kwa Siku')),
                ('JumlaYaDeni', models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumla Ya Deni Analodaiwa')),
                ('Riba', models.IntegerField(blank=True, default=0, null=True, verbose_name='Riba')),
                ('FainiIliyoPokelewaLeo', models.IntegerField(blank=True, default=0, null=True, verbose_name='Faini Iliyopokelewa Leo')),
                ('FainiKwaSiku', models.IntegerField(blank=True, default=0, null=True, verbose_name='Faini Kwa Siku')),
                ('AmesajiliwaNa', models.CharField(blank=True, max_length=500, null=True, verbose_name='Amesajiliwa Na ?')),
                ('PichaYaMteja', models.ImageField(blank=True, null=True, upload_to='media/PichaZaVyakula/', verbose_name='Picha Ya Mteja')),
                ('Ni_Mteja_Hai', models.BooleanField(blank=True, default=True, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('Up_To', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Malipo Ya Faini Copies',
            },
        ),
        migrations.CreateModel(
            name='MarejeshoCopies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(blank=True, max_length=100000, null=True, verbose_name='Namba Ya Mteja')),
                ('JinaKamiliLaMteja', models.CharField(blank=True, max_length=500, null=True, verbose_name='Jina Kamili La Mteja')),
                ('JinaLaKituo', models.CharField(blank=True, max_length=500, null=True, verbose_name='Jina La Kituo Cha Mteja')),
                ('SimuYaMteja', models.IntegerField(blank=True, null=True, verbose_name='Namba Ya Simu Ya Mteja')),
                ('EmailYaMteja', models.EmailField(blank=True, max_length=500, null=True, verbose_name='Email Ya Mteja')),
                ('Mahali', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mahali Anapoishi')),
                ('KiasiAnachokopa', models.IntegerField(blank=True, default=0, null=True, verbose_name='Kiasi Anachokopa')),
                ('KiasiAlicholipa', models.IntegerField(blank=True, default=0, null=True, verbose_name='Kiasi Alicholipa')),
                ('RejeshoKwaSiku', models.IntegerField(blank=True, default=0, null=True, verbose_name='Rejesho Kwa Siku')),
                ('JumlaYaDeni', models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumla Ya Deni Analodaiwa')),
                ('Riba', models.IntegerField(blank=True, default=0, null=True, verbose_name='Riba')),
                ('RejeshoLililoPokelewaLeo', models.IntegerField(blank=True, default=0, null=True, verbose_name='Rejesho Lililo Pokelewa Leo')),
                ('FainiKwaSiku', models.IntegerField(blank=True, default=0, null=True, verbose_name='Faini Kwa Siku')),
                ('AmesajiliwaNa', models.CharField(blank=True, max_length=500, null=True, verbose_name='Amesajiliwa Na ?')),
                ('PichaYaMteja', models.ImageField(blank=True, null=True, upload_to='media/PichaZaVyakula/', verbose_name='Picha Ya Mteja')),
                ('Ni_Mteja_Hai', models.BooleanField(blank=True, default=True, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('Up_To', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Marejesho Copies',
            },
        ),
        migrations.CreateModel(
            name='NjeYaMkatabaCopies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(blank=True, max_length=100000, null=True, verbose_name='Namba Ya Mteja')),
                ('JinaKamiliLaMteja', models.CharField(blank=True, max_length=500, null=True, verbose_name='Jina Kamili La Mteja')),
                ('JinaLaKituo', models.CharField(blank=True, max_length=500, null=True, verbose_name='Jina La Kituo Cha Mteja')),
                ('SimuYaMteja', models.IntegerField(blank=True, null=True, verbose_name='Namba Ya Simu Ya Mteja')),
                ('EmailYaMteja', models.EmailField(blank=True, max_length=500, null=True, verbose_name='Email Ya Mteja')),
                ('Mahali', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mahali Anapoishi')),
                ('KiasiAnachokopa', models.IntegerField(blank=True, default=0, null=True, verbose_name='Kiasi Anachokopa')),
                ('KiasiAlicholipa', models.IntegerField(blank=True, default=0, null=True, verbose_name='Kiasi Alicholipa')),
                ('RejeshoKwaSiku', models.IntegerField(blank=True, default=0, null=True, verbose_name='Rejesho Kwa Siku')),
                ('JumlaYaDeni', models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumla Ya Deni Analodaiwa')),
                ('Riba', models.IntegerField(blank=True, default=0, null=True, verbose_name='Riba')),
                ('RejeshoLililoPokelewaLeo', models.IntegerField(blank=True, default=0, null=True, verbose_name='Rejesho Lililo Pokelewa Leo')),
                ('FainiKwaSiku', models.IntegerField(blank=True, default=0, null=True, verbose_name='Faini Kwa Siku')),
                ('AmesajiliwaNa', models.CharField(blank=True, max_length=500, null=True, verbose_name='Amesajiliwa Na ?')),
                ('PichaYaMteja', models.ImageField(blank=True, null=True, upload_to='media/PichaZaVyakula/', verbose_name='Picha Ya Mteja')),
                ('Ni_Mteja_Hai', models.BooleanField(blank=True, default=True, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('Up_To', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Nje Ya Mkataba Copies',
            },
        ),
        migrations.CreateModel(
            name='VituoVyote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JinaLaKituo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Jina La Kituo')),
                ('Mahali', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mahali Kilipo')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Vituo Vyote',
            },
        ),
        migrations.CreateModel(
            name='WatejaWote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(blank=True, default=App.models.generated_reg_no, editable=False, max_length=100000, null=True, unique=True)),
                ('JinaKamiliLaMteja', models.CharField(blank=True, max_length=500, null=True, verbose_name='Jina Kamili La Mteja')),
                ('SimuYaMteja', models.IntegerField(blank=True, null=True, verbose_name='Namba Ya Simu Ya Mteja')),
                ('SimuYaMzaminiWa1', models.IntegerField(blank=True, null=True, verbose_name='Namba Ya Simu Ya Mzamini Wa 1')),
                ('SimuYaMzaminiWa2', models.IntegerField(blank=True, null=True, verbose_name='Namba Ya Simu Ya Mzamini Wa 2')),
                ('JinaLaMzaminiWa1', models.CharField(blank=True, max_length=500, null=True, verbose_name='Jina Kamili La Mzamini Wa 1')),
                ('JinaLaMzaminiWa2', models.CharField(blank=True, max_length=500, null=True, verbose_name='Jina Kamili La Mzamini Wa 2')),
                ('EmailYaMteja', models.EmailField(blank=True, max_length=500, null=True, verbose_name='Email Ya Mteja')),
                ('Mahali', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mahali Anapoishi')),
                ('MaelezoYaMteja', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Maelezo Ya Mteja')),
                ('KiasiAnachokopa', models.IntegerField(blank=True, default=0, null=True, verbose_name='Kiasi Kiasi Anachokopa')),
                ('KiasiAlicholipa', models.IntegerField(blank=True, default=0, null=True, verbose_name='Kiasi Alicholipa Mpaka Sasa')),
                ('RejeshoKwaSiku', models.IntegerField(blank=True, default=0, null=True, verbose_name='Rejesho Kwa Siku')),
                ('JumlaYaDeni', models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumla Ya Deni Analodaiwa')),
                ('Riba', models.IntegerField(blank=True, default=0, null=True, verbose_name='Riba')),
                ('AmesajiliwaNa', models.CharField(blank=True, max_length=500, null=True, verbose_name='Amesajiliwa Na ?')),
                ('Amerejesha_Leo', models.BooleanField(blank=True, default=False, null=True)),
                ('PichaYaMteja', models.ImageField(blank=True, null=True, upload_to='media/PichaZaVyakula/', verbose_name='Picha Ya Mteja')),
                ('Ni_Mteja_Hai', models.BooleanField(blank=True, default=True, null=True)),
                ('Nje_Ya_Mkata_Wote', models.BooleanField(blank=True, default=False, null=True)),
                ('Nje_Ya_Mkata_Leo', models.BooleanField(blank=True, default=False, null=True)),
                ('Up_To', models.DateTimeField(blank=True, null=True)),
                ('JumlaYaFainiZote', models.IntegerField(blank=True, default=0, null=True, verbose_name='JumlaYaFainiZote')),
                ('Created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('JinaLaKituo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='App.vituovyote')),
            ],
            options={
                'verbose_name_plural': 'Wateja Wote',
            },
        ),
        migrations.CreateModel(
            name='WatejaWoteCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JinaKamiliLaMteja', models.CharField(blank=True, max_length=500, null=True, verbose_name='Jina Kamili La Mteja')),
                ('ordered', models.BooleanField(default=False)),
                ('total_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumla Ya Kiasi Alicholipa')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'WatejaWote  Cart',
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='email')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='user name')),
                ('company_name', models.CharField(blank=True, default='Gegwajo Microfinance', max_length=500, null=True, verbose_name='company name')),
                ('phone', models.CharField(blank=True, max_length=10, null=True, verbose_name='phone')),
                ('Location', models.CharField(blank=True, max_length=200, null=True, verbose_name='Mahali')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Picha Ya Mtu')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_cashier', models.BooleanField(default=True)),
                ('hide_email', models.BooleanField(default=True)),
                ('JinaLaKituo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='App.vituovyote')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WatejaWoteCartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JinaKamiliLaMteja', models.CharField(blank=True, max_length=500, null=True, verbose_name='Jina Kamili La Mteja')),
                ('KiasiChaRejeshoChaSiku', models.FloatField(blank=True, default=0, null=True)),
                ('KiasiChaFainiChaSiku', models.FloatField(blank=True, default=0, null=True)),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('Mteja', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App.watejawote')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App.watejawotecart')),
            ],
            options={
                'verbose_name_plural': 'WatejaWote  Cart Items',
            },
        ),
        migrations.CreateModel(
            name='Ripoti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JumlaMarejeshoYaLeo', models.IntegerField(blank=True, null=True, verbose_name='Jumla Ya Marejesho Ya Leo')),
                ('JumlaFainiLeo', models.IntegerField(blank=True, null=True, verbose_name='Jumla Ya Faini Za Leo')),
                ('FomuNaBima', models.IntegerField(blank=True, null=True, verbose_name='Fomu Na Bima')),
                ('BakiJana', models.IntegerField(blank=True, null=True, verbose_name='Kiasi Kilichobaji Jana')),
                ('ImetokaKwaBosi', models.IntegerField(blank=True, null=True, verbose_name='Imetoka Kwa Bosi')),
                ('ImetokaKituoJirani', models.IntegerField(blank=True, null=True, verbose_name='Imetoka Kituo Jirani')),
                ('MapatoYaJumla', models.IntegerField(blank=True, null=True, verbose_name='Jumla Ya Mapato Ya Leo')),
                ('Mkopo', models.IntegerField(blank=True, null=True, verbose_name='Mkopo')),
                ('Posho', models.IntegerField(blank=True, null=True, verbose_name='Posho')),
                ('ImeendaKwaBosi', models.IntegerField(blank=True, null=True, verbose_name='Imeenda Kwa Bosi')),
                ('ImeendaKituoJirani', models.IntegerField(blank=True, null=True, verbose_name='Imeenda Kituo Jirani')),
                ('MatumiziMengine', models.IntegerField(blank=True, null=True, verbose_name='Matumizi Mengine')),
                ('MatumiziYaJumla', models.IntegerField(blank=True, null=True, verbose_name='Matumizi Ya Jumla')),
                ('IdadiYaMikopoYaLeo', models.IntegerField(blank=True, null=True, verbose_name='Idadi Ya Mikopo Ya Leo')),
                ('IdadiYaMikatabaMipyaLeo', models.IntegerField(blank=True, null=True, verbose_name='Idadi Ya Mikataba Mipya Leo')),
                ('IdadiYaWenyeMikatabaHai', models.IntegerField(blank=True, null=True, verbose_name='Idadi Ya Wenye Mikataba Hai')),
                ('IdadiYaWaliorejeshaLeo', models.IntegerField(blank=True, null=True, verbose_name='Idadi Ya Waliorejesha Leo')),
                ('IdadiYaFainiZilizopokelewaLeo', models.IntegerField(blank=True, null=True, verbose_name='Idadi Ya Faini Zilizopokelewa Leo')),
                ('Balance', models.IntegerField(blank=True, null=True, verbose_name='Balance')),
                ('KituoIlichoendaHela', models.CharField(blank=True, max_length=500, null=True, verbose_name='Kituo Ilichoenda Hela')),
                ('KituoIlichotokaHela', models.CharField(blank=True, max_length=500, null=True, verbose_name='Kituo Ilichotoka Hela')),
                ('ImeweingizwaNa', models.CharField(blank=True, max_length=500, null=True, verbose_name='Imeweingizwa Na ?')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('JinaLaKituo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='App.vituovyote')),
            ],
            options={
                'verbose_name_plural': 'Ripoti',
            },
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
