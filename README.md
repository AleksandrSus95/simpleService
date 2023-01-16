**Сборка Docker образа**  
Собираем образ:  
docker build -t <your_name>/<your_dockerhub_reposname_publick>:<tag name> -f Dockerfile .  

Пример: docker buid -t myname/publickservice:1 -f Dockerfile .  

Для теста понадобится publick и private репазиторий на Dockerhub  
по этому собирем сразу еще и для приватного репазитория  
docker build -t <your_name>/<your_dockerhub_reposname_private>:<tag name> -f Dockerfile .  

Пример: docker buid -t myname/privateservice:1 -f Dockerfile .  

Запушим собранный образ в репазиторий Dockerhub  
docker push -t <your_name>/<your_dockerhub_reposname>:<tag name>  
Запушить сразу как в паблик так и в приватный репазиторий Dockerhub  

**Запуск контейнера локально**  
docker run --name <container_name> -p 3000:3000 <image_name>:<tag>  
Сервис будет доступен на http://localhost:3000  

**Запуск сервиса локально Linux**  
Чтобы использовать виртуальную среду:
- source venv/bin/activate

Установить Flask
- pip install Flask

Установить num2words
- pip install num2words

Запуск приложения
- export FLASK_APP=testservice.py run
- flask run --port=3000
или
- python -m flask run --host=0.0.0.0 --port=3000

**Запуск сервиса локально Windows**  
Создаем виртуальную среду:  
python -m venv <env_name>

Запустим виртуальную среду:  
Преположим вы находитесь в папке с проектом в котором создана виртуальная среда  
.\<env_name>\Scripts\activate  

Установить Flask  
pip install flask  

Установить num2words  
pip install num2words  

Запуск приложения  
Создать файл для Flask .env  
Записать туда пременные:  
FLASK_APP=testservice.py  
FLASK_ENV=development  
FLASK_RUN_PORT=3000  

Установить python-dotenv  
pip install python-dotenv  

Запустить приложение:  
flask run  

Приложение будет доступно на http://localhost:3000/  

По окончанию работы деактивировать виртуальную среду:  
deactivate  