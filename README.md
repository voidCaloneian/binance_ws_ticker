
## Запуск проекта
### Через Docker 
```bash
docker compose up --build
```
- Миграции будут уже произведены
- Тесты запускаются при каждом запуске проекта


Хост и порт проекта ```localhost:8000```

## Получение истории тиков
### Последний тик сохраняется в базу данных каждую минуту!
-   **```GET``` /api/tickers/**  
    Пример ответа
    ```json
    [
      {
        "id": 2,
        "symbol": "BTCUSDT",
        "price": "88648.0800000000",
        "trade_time": "2025-03-07T15:51:40.735016Z"
    },
      {
        "id": 1,
        "symbol": "BTCUSDT",
        "price": "88655.9900000000",
        "trade_time": "2025-03-07T15:50:40.729171Z"
      }
    ]
    ```
## Подключение к вебсокету для получения тиков в режиме реального времени
- **```WebSocket```/ws/prices/**

    
