#!/bin/bash -x

# 仅在调试模式下进行Python包的重新安装
if [ "$DEBUG" = "True" ];then

pip install --no-cache-dir -e /app/requirements/source/moear-spider-common
pip install --no-cache-dir -e /app/requirements/source/moear-spider-*
pip install --no-cache-dir -r /app/requirements/pip.txt

fi

# 初始化数据库表格
python manage.py makemigrations --settings=$SERVER_SETTINGS --noinput
python manage.py makemigrations --settings=$SERVER_SETTINGS --noinput posts spiders terms core
python manage.py migrate --settings=$SERVER_SETTINGS --noinput

# 仅在生产模式下执行静载资源归集&翻译文件生成等操作
if [ "$PRODUCTION" = "True" ];then

# 归集静态文件
python manage.py collectstatic --noinput

# 更新&编译翻译文件
python manage.py makemessages --settings=$SERVER_SETTINGS --all
python manage.py makemessages --settings=$SERVER_SETTINGS --domain djangojs --all --ignore echarts.js --ignore bootstrap.js --ignore jquery.js
python manage.py compilemessages --settings=$SERVER_SETTINGS

fi