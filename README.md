**Запуск сервиса локально**  
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

Чтобы собрать контейнер
- docker build -t tagname:version -f Dockerfile .  

Чтобы запустить контейнер
docker run -p 3000:3000 <image_name>:<tag> 