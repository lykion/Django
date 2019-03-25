# 相关文章  
第一篇：https://testerhome.com/topics/13269  
第二篇：https://testerhome.com/topics/14801  
第三篇：https://testerhome.com/topics/15352  
第四篇：https://testerhome.com/topics/15657  
其余篇：https://tech.kujiale.com/zi-yan-jie-kou-ce-shi-ping-tai/

项目配置启动过程：
1、修改settings.py文件的DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'request',  # 创建的数据库的名字（需要提前在数据库创建好该数据库）
        'USER': 'root',     # 登录数据的用户名
        'PASSWORD': '123456',   # 登录密码
        # 'HOST': '47.102.110.163',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }

    }
}

2、打开命令行窗口，通过cd切换到该项目更目录

3、数据库迁移
执行命令：python manage.py makemigrations

4、完成库表的生成
执行命令：python manage.py migrate

5、创建第一个用户
执行命令：python manage.py createsuperuser

6、启动服务
执行命令：python manage.py runserver {浏览器访问地址：http://127.0.0.1:8000/}
