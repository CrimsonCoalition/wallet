FROM python:3.8
# указываем место где хранятся файлы
WORKDIR /usr/wallet/
# копируем файлы
COPY . /usr/wallet
# устанавливаем aiogram и тд
RUN pip install --user aiogram
# запускаем бота
CMD ["python", "main.py"]
