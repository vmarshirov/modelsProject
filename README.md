### mysite_0412

### !!! не изменять

https://disk.yandex.ru/d/7cwUZfyJNgMvXQ



### git

git clone https://github.com/g00u00/mysite_0412.git

cd mysite_0412

или

mkdir mysite_0412

git init

git remote add origin git@github.com:g00u00/mysite_0412.git

git pull origin main


### Для не Windows env

su

apt install python3.8-venv

exit

python3 -m venv env

. env/bin/activate

deactivate

### Для Windows env: 

python -m venv env

env\Scripts\activate

deactivate

https://medium.com/@ph1l74/python-venv-%D0%BD%D0%B0-windows-10-2118ad685b1 

https://wiki.iphoster.net/wiki/Windows_10_-_%D0%BA%D0%B0%D0%BA_%D0%BF%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B5%D1%82%D1%8C_%D0%B8%D0%BB%D0%B8_%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C_%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5_%D1%81%D1%80%D0%B5%D0%B4%D1%8B_(Environment_Variable)

https://python.land/virtual-environments/virtualenv

### Конфигурирование и запуск 

pip install -r requirements.txt

python manage.py runserver 10.0.2.15:8000

admin root root

------------

### Редирект порта для сервера
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8000

-------------=

pip freeze > requirements.txt

pip install -r requirements.txt

--------------------
