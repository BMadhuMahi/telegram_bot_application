# telegram_bot_application
This is a Django-based backend project that demonstrates skills in:
- Django REST Framework (DRF)
- JWT Authentication
- Celery + Redis integration for background tasks
- Telegram bot integration
- Production-ready settings with `.env`
- Clean code and proper project structure
  
## 🔧 Features
- ✅ User Registration and Login via API
- ✅ JWT Token Authentication
- ✅ Public and Protected API endpoints
- ✅ Celery background task to send email on registration
- ✅ Telegram bot integration to collect user Telegram usernames
- ✅ Environment variable-based configuration (secure and production-ready)
  
## 🔧 Setup project
- create project using command 'Django-admin startproject tele_bot_app'
- created application inside project using command 'py manage.py startapp api_app'
- I installed all requirements using 'pip install -r requirements.txt'
  
## 🔧 Setup Environment Variables
SECRET_KEY=django-insecure-he-$24!d4=zrz1++j3hhm*6_)8s8b203n@yhi&z$h&n2gg5+)4
DEBUG=False
DB_NAME=telebot
DB_USER=root
DB_PASSWORD=madhu
TELEGRAM_BOT_TOKEN=7750406074:AAH5Gy_GkFFC_mKywty2CQYYkOS44F1_uRg
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=madhuboya582@gmail.com
EMAIL_HOST_PASSWORD=agsjolrdznrmtsov

## 🔧 Run Locally
 1. Start Redis (in another terminal)
    redis-server
 2. Run Django Server
    python manage.py runserver
 3. Start Celery Worker
    celery -A tele_bot worker --pool=solo -l info
 4. Start Telegram Bot Listener
    python tele_bot/bot.py(The bot will listen for /start messages and save the user's Telegram username in the database.)

## 🔧 API documentation
- http://127.0.0.1:8000/api/register/  (Register new user and send welcome email)
   post{
  "username": "username",
  "password": "password",
  "email": "abc@gmail.com"
  }
- http://127.0.0.1:8000/api/login/ (Authenticate and receive JWT token)
  post{
  "username": "username",
  "password": "password"
  }
  we will get access and refresh tokens
- http://127.0.0.1:8000/api/public/   (	Accessible by anyone)
- http://127.0.0.1:8000/api/protected/  (Requires JWT token in Authorization header)
   Authorization: Bearer your_token 

