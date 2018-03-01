#!/bin/bash -x

# 初始化数据库表格
python manage.py makemigrations --settings=$SERVER_SETTINGS --noinput
python manage.py makemigrations --settings=$SERVER_SETTINGS --noinput posts spiders terms core
python manage.py migrate --settings=$SERVER_SETTINGS --noinput

if [ "$PRODUCTION" = "True" ];then

# 归集静态文件
python manage.py collectstatic --noinput

# 更新&编译翻译文件
python manage.py makemessages --settings=$SERVER_SETTINGS --all
python manage.py makemessages --settings=$SERVER_SETTINGS --domain djangojs --all --ignore echarts.js --ignore bootstrap.js --ignore jquery.js
python manage.py compilemessages --settings=$SERVER_SETTINGS

fi
