~~~~~~~~~~~~~Linux或者Mac搭建Django指南~~~~~~~~~~~~~

第一步： Root权限登陆，然后安装相关依赖
yum install -y mysql-devel gcc gcc-devel python-devel libtiff-devel libjpeg-devel libzip-devel freetype-devel lcms2-devel libwebp-devel tcl-devel tk-devel openldap-devel


第二步：安装django环境 （依赖第四步的拷贝工程代码）
pip install -r requirement.txt  -i   https://pypi.douban.com/simple


第三步：启动工程
python manage.py runserver


~~~~~~~~~~~~~线上环境服务器端搭建指南~~~~~~~~~~~~~

1. 完成Linux搭建Django指南前两步

2. settings.py改成如下内容:
from settings_online import *

3. 把settings_online.py里的数据库配置信息改对

4. 创建授权库
CREATE DATABASE IF NOT EXISTS django_emarket_cms_auth
  DEFAULT CHARSET utf8mb4
  COLLATE utf8mb4_general_ci;

5. 创建授权需要的表, 在工程的根目录执行命令
python manage.py syncdb

6. 创建其他用户来访问该网站