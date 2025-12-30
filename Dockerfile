# Базовий образ Alpine (дуже легкий Linux)
FROM python:3.9-alpine

# Робоча папка всередині контейнера
WORKDIR /app

# Копіюємо файл залежностей і встановлюємо їх
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код у контейнер
COPY . .

# Команда, яка запуститься при старті контейнера
CMD ["python", "main.py"]