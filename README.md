# TaskBoard
Simple task board on Django for 404 Group.

Это тестовое задание. В нем есть места, которые можно оптимизировать, но "совершенству нет предела". Данный сайт сейчас крутится на AWS: http://54.93.84.128/, прошу посмотреть. Все тестировалось на ubuntu 14.04 x64.

Уже зарегистрированные пользователи:

Заказчик:
l: customer
p: customer

Исполнитель:
l: elancer
p: elancer

Суперпользователь:
l: super
p: super

Чтобы изменить процент комиссии надо залогиниться суперпользователем в /admin/ и пройти в /commission/. Если комиссия не была введена, то умолчанию это 10%. Суперпользователь не может вести деятельность внутри системы (ему и не надо), поэтому у него просто нет профайла.

Если попадете в беду: /ajax/logout/

Ниже инструкция для развертывания на своей машине.

**УСТАНОВКА**

Необходимо поставить пакеты ubuntu для "postgresql", "apache", "python". В некоторых случаях понадобится команда "sudo" или быть в той или иной группе, например, www-data.

Рекомендованное обновление системы:
>> apt-get update
>> apt-get upgrade

Пакеты:
>> >>apt-get install python-virtualenv python-dev libpq-dev postgresql postgresql-contrib build-essential git python-pip apache2 libapache2-mod-wsgi

========================================================
**Сначала настраиваем БД**

**Поскольку я использовал AWS образ Ubuntu, мне необходимо было сгенерировать locale**
>> locale-gen ru_RU ru_RU.UTF-8

**И запустить postgresql вручную**
>> pg_createcluster 9.3 main --start

**Могу отметить, что в десктоп-версии эти шаги были проделаны системой автоматически при установке БД.**

Поставим пароль юзеру по умолчанию:
>> sudo -u postgres psql postgres

Появится консоль, необходимо ввести "\password postgres", далее он спросить пароль. Вводим, пусть "postgrespassword". Выходим нажав сочетание клавиш "Ctrl+D".

ПРИМЕЧАНИЕ: естественно, в продакшене нужны "сильные" пароли.

Создаем базу данных для приложения:
>> sudo su - postgres
Вводим "createdb taskboard", где "taskboard" - имя бд.

Создаем пользователя, под которым django будет обращаться к БД. Все в той же консоли вводим "createuser --interactive -P". Консоль спросит имя, пароль. Пусть будут "django" и "djangopassword", соответственно. На остальные вопросы отвечаем 'n'.

Теперь необходимо дать пользователю 'django' права.
>> psql
Вводим на языке sql:
GRANT ALL PRIVILEGES ON DATABASE taskboard TO django;
Консоль подтвердит команду ответом "GRANT"
БД сконфигурирована.

========================================================
**Установка "виртуального" окружения python**

Скачваем приложение из github.com
>> git clone https://github.com/denova/TaskBoard.git
*необходимо быть в группе www-data с возможностью записи в /var/www/ директорию

Далее устанавливаем виртуальное окружение
>> virtualenv env

Заходим в виртуальное окружение
>> source env/bin/activate

И ставим необходимые зависимости из requirements.txt
>> pip install -r requirements.txt

Выходим из окружения
>> deactivate

========================================================
**Найстройка apache**

С помощью консольного редактора nano открываем файл:
>> nano /etc/apache2/sites-enabled/000-default

и добавляем следующие строки, сразу после <VirtualHost *:80>:

"

WSGIDaemonProcess TaskBoard python-path=/var/www/TaskBoard:/var/www/TaskBoard/env/lib/python2.7/site-packages

WSGIProcessGroup TaskBoard

WSGIScriptAlias / /var/www/TaskBoard/taskboard/wsgi.py

Alias /static/ /var/www/TaskBoard/static/

"

Также меняем "DocumentRoot":

"

DocumentRoot /var/www/TaskBoard

"

ПРИМЕЧАНИЕ: в продакш версии (с доменом) необходимо создать новый 'virual host' вместо переписывания дефолтного.

========================================================
**Настройка django**

Первым делом необходимо прописать логин, пароль к БД в файле taskboard/settings.py. Интересующая нас часть будет выглядеть так:

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'taskboard',

        'USER': 'django',

        'PASSWORD': 'djangopassword',

        'HOST': '127.0.0.1',

        'PORT': '5432',

    }

}

ПРИМЕЧАНИЕ: в продакшене следует использовать данные из переменных окружения, текущий способ используется для простоты и оптимизации временных затрат.

Необходимо сделать миграцию баз данных, команда выполняется из /var/www/TaskBoard/ директории:
>> env/bin/python manage.py migrate

Необходимо собрать статичные файлы (в т.ч. из админки) воедино:
>> env/bin/python manage.py collectstatic

Последним шагом необходимо создать суперпользователя для 'django':
>> env/bin/python manage.py createsuperuser

Данный пользователь сможет заходить в админку django, а также менять процент комиссии у "системы".
