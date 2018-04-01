## db 정보

## postgresql 설치 경로

* DB DATA DIR :
```
/var/lib/pgsql/9.4/data
```

* DB CONF : 
```
/var/lib/pgsql/9.4/data/postgresql.conf
/var/lib/pgsql/9.4/data/pg_hba.conf
```

* DB LOGDIR :

```
/var/lib/pgsql/9.4/data/pg_log
```

```
> ps -ef | grep pgsql
postgres   653     1  0 16:51 ?        00:00:00 /usr/pgsql-9.4/bin/postgres -D /var/lib/pgsql/9.4/data
```

## postgresql 권한 및 db 생성
psql 하면 계정이 없다고 나온다. 기본계정인 postgres 로 계정 바꿔서 들어가본다

```
> sudo -u postgres -i
> psql

> SELECT datname FROM pg_database;
```

계정 및 DB 생성 (admin / admin4321)

```
> CREATE USER admin WITH PASSWORD 'admin4321';
> CREATE DATABASE admin_db;
```

권한 부여

```
> GRANT ALL PRIVILEGES ON DATABASE admin_db to admin;
> \q; (종료)
```
* 참고 문서 : http://postgresguide.com/setup/users.html

## port open
/var/lib/pgsql/9.4/data/postgresql.conf 설정에서 listen_addresses 추가
모든 address 를 허용하므로 "*" 을 추가한다



---


1. 환경 변수 셋팅후 django-admin startproject 실행
2. 기본셋팅후 db 연동

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '_DB_NAME',
        'USER': '_DB_USER',
        'PASSWORD': '_DB_PW',
        'HOST': '_DB_HOST',
        'PORT': '5432',
    }
}
```

으로 작성후 python manage.py migrate 을 하면 에러남 -> No module named 'psycopg2 에러남.

찾아보니 모듈 추가 설치 필요.

```
pip install psycopg2
```


# 환경변수 freeze
http://www.idiotinside.com/2015/05/10/python-auto-generate-requirements-txt/

---

# module migrate

```
python manage.py makemigrations board
python manage.py migrate board
```

---

# front settings


1. vue-cli 로 vue 프로젝트 생성하기

Vue CLI v3.0.0-beta.6 사용

```
vue create vue-front 
```

1. add bootstrap-vue
```
npm i bootstrap-vue
```


