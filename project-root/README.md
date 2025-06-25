# 🚀 Инструкция по запуску проекта

## 📋 Описание проекта

Полноценное веб-приложение с React frontend и Flask backend для работы с данными о товарах и услугах стран.

### 🏗️ Архитектура
- **Frontend**: React + TypeScript + Material-UI
- **Backend**: Flask + SQLAlchemy + SQLite
- **Контейнеризация**: Docker + Docker Compose

## 🛠️ Требования

- Docker Desktop (версия 20.10+)
- Docker Compose (версия 2.0+)
- Минимум 4GB RAM
- 10GB свободного места на диске

## 🚀 Быстрый запуск

### 1. Клонирование и переход в директорию
```bash
cd "project-root"
```

### 2. Запуск всех сервисов
```bash
docker-compose up --build
```

### 3. Открытие приложения
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000

## 📁 Структура проекта

```
project-root/
├── frontend/          # React приложение
│   ├── Dockerfile
│   ├── .dockerignore
│   └── src/
├── backend/           # Flask API
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── requirements.txt
│   └── app.py
└── docker-compose.yml # Конфигурация сервисов
```

## ⚙️ Команды управления

### Запуск в фоновом режиме
```bash
docker-compose up -d --build
```

### Просмотр логов
```bash
# Все сервисы
docker-compose logs

# Конкретный сервис
docker-compose logs frontend
docker-compose logs backend
```

### Остановка сервисов
```bash
docker-compose down
```

### Пересборка и запуск
```bash
docker-compose up --build --force-recreate
```

### Очистка данных
```bash
docker-compose down -v  # Удаляет volumes
docker system prune     # Очищает неиспользуемые образы
```

## 🔧 Конфигурация

### Переменные окружения

**Frontend** (в docker-compose.yml):
- `REACT_APP_API_URL`: URL backend API

**Backend** (в docker-compose.yml):
- `FLASK_DEBUG`: Режим отладки (0/1)
- `FLASK_APP`: Главный файл приложения

### Портты
- **3000**: React приложение
- **5000**: Flask API

## 🐛 Устранение неполадок

### Проблема: Порт уже занят
```bash
# Проверить что использует порт
netstat -ano | findstr :3000
netstat -ano | findstr :5000

# Остановить процесс или изменить порт в docker-compose.yml
```

### Проблема: Ошибка сборки
```bash
# Очистить кэш Docker
docker system prune -a

# Пересобрать образы
docker-compose build --no-cache
```

### Проблема: База данных не создается
```bash
# Проверить volumes
docker volume ls

# Пересоздать volume
docker-compose down -v
docker-compose up --build
```

### Проблема: Медленная сборка
```bash
# Использовать кэш Docker
docker-compose build

# Или собрать только измененные сервисы
docker-compose build frontend
docker-compose build backend
```

## 📊 Мониторинг

### Проверка состояния сервисов
```bash
docker-compose ps
```

### Использование ресурсов
```bash
docker stats
```

### Health check
Сервисы автоматически проверяют свое состояние каждые 30 секунд.

## 🔒 Безопасность

- Все образы обновлены до последних версий
- Используются slim версии базовых образов
- Минимальный набор установленных пакетов
- Production режим для backend

## 📝 Разработка

### Локальная разработка без Docker
```bash
# Backend
cd backend
pip install -r requirements.txt
python app.py

# Frontend
cd frontend
npm install
npm start
```

### Добавление новых зависимостей
```bash
# Backend
docker-compose exec backend pip install package_name

# Frontend
docker-compose exec frontend npm install package_name
```

## 🚀 Production развертывание

### Сборка production образов
```bash
docker-compose -f docker-compose.yml build
```

### Запуск в production
```bash
docker-compose -f docker-compose.yml up -d
```

## 📞 Поддержка

При возникновении проблем:
1. Проверьте логи: `docker-compose logs`
2. Убедитесь в достаточности ресурсов
3. Проверьте версии Docker и Docker Compose
4. Очистите кэш: `docker system prune`

---

**Версия**: 1.0  
**Последнее обновление**: 2024 