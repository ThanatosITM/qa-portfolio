# Документация JSONPlaceholder API

## Базовый URL
`https://jsonplaceholder.typicode.com`

## Ресурсы
- `/posts` - посты (100 записей)
- `/comments` - комментарии (500 записей) 
- `/users` - пользователи (10 записей)

## Методы для /posts
- `GET /posts` - получить все посты
- `GET /posts/1` - получить пост с ID=1
- `POST /posts` - создать пост
- `PUT /posts/1` - обновить пост
- `DELETE /posts/1` - удалить пост

## Структура данных
### Post
```json
{
  "userId": 1,
  "id": 1, 
  "title": "string",
  "body": "string"
}