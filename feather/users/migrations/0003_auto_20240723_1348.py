# Generated by Django 2.2.16 on 2024-07-23 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20240723_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(choices=[('AK', 'Абхазия'), ('AU', 'Австралия'), ('AT', 'Австрия'), ('AZ', 'Азербайджан'), ('AL', 'Албания'), ('DZ', 'Алжир'), ('AI', 'Ангилья'), ('AO', 'Ангола'), ('AD', 'Андорра'), ('AG', 'Антигуа и Барбуда'), ('AR', 'Аргентина'), ('AR', 'Армения'), ('AW', 'Аруба'), ('AF', 'Афганистан'), ('BD', 'Бангладеш'), ('BB', 'Барбадос'), ('BH', 'Бахрейн'), ('BY', 'Беларусь'), ('BE', 'Бельгия'), ('BG', 'Болгария'), ('BA', 'Босния и Герцеговина'), ('BW', 'Ботсвана'), ('BR', 'Бразилия'), ('BN', 'Бруней'), ('BT', 'Бутан'), ('VU', 'Вануату'), ('VA', 'Ватикан'), ('VE', 'Венесуэла'), ('VN', 'Вьетнам'), ('GA', 'Габон'), ('GH', 'Гана'), ('DE', 'Германия'), ('HN', 'Гондурас'), ('GD', 'Гренада'), ('GR', 'Греция'), ('GE', 'Грузия'), ('DK', 'Дания'), ('CD', 'Демократическая Республика Конго'), ('DJ', 'Джибути'), ('DM', 'Доминика'), ('DO', 'Доминиканская Республика'), ('EG', 'Египет'), ('ZM', 'Замбия'), ('ZW', 'Зимбабве'), ('IL', 'Израиль'), ('IN', 'Индия'), ('AD', 'Индонезия'), ('JO', 'Иордания'), ('IQ', 'Ирак'), ('IR', 'Ирак'), ('IE', 'Ирландия'), ('IS', 'Исландия'), ('ES', 'Испания'), ('IT', 'Италия'), ('KP', 'КНДР'), ('KZ', 'Казахстан'), ('KH', 'Камбоджа'), ('CM', 'Камерун'), ('CA', 'Канада'), ('KE', 'Кения'), ('CY', 'Кипр'), ('CN', 'Китай'), ('CO', 'Колумбия'), ('CR', 'Коста-Рика'), ('CI', 'Кот д Ивуар'), ('CU', 'Куба'), ('KG', 'Кыргызстан'), ('LV', 'Латвия'), ('LB', 'Ливан'), ('LT', 'Литва'), ('LU', 'Люксембург'), ('AD', 'Малайзия'), ('MX', 'Мексика'), ('AD', 'Нидерланды'), ('AD', 'Норвегия'), ('AE', 'Объединённые Арабские Эмираты'), ('PS', 'Палестина'), ('AD', 'Парагвай'), ('AD', 'Перу'), ('AD', 'Польша'), ('CG', 'Республика Конго'), ('KR', 'Республика Корея'), ('RU', 'Россия'), ('RW', 'Руанда'), ('RO', 'Румыния'), ('RS', 'Сербия'), ('SG', 'Сингапур'), ('SY', 'Сирия'), ('GB', 'Соединенное Королевство'), ('US', 'Соединенные Штаты Америки'), ('TJ', 'Таджикистан'), ('UZ', 'Узбекистан'), ('UA', 'Украина'), ('UY', 'Уругвай'), ('FI', 'Финлядния'), ('FR', 'Франция'), ('HR', 'Хорватия'), ('CF', 'Центральноафриканская Республика'), ('CZ', 'Чехия'), ('CL', 'Чили'), ('CH', 'Швейцария'), ('EC', 'Эквадор'), ('ER', 'Эритрея'), ('EE', 'Эстония'), ('ZA', 'Южноафриканская Республика'), ('JM', 'Ямайка'), ('JP', 'Япония')], max_length=50),
        ),
    ]
