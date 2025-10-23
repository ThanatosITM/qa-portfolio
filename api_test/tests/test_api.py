import requests
import pytest


class TestJSONPlaceholderAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def test_get_post(self):
        """Тест GET запроса для получения поста"""
        response = requests.get(f"{self.BASE_URL}/posts/1")

        # Проверяем статус код
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"

        # Проверяем структуру JSON
        data = response.json()
        assert "userId" in data, "Поле userId отсутствует в ответе"
        assert "id" in data, "Поле id отсутствует в ответе"
        assert "title" in data, "Поле title отсутствует в ответе"
        assert "body" in data, "Поле body отсутствует в ответе"

        # Проверяем типы данных
        assert isinstance(data["userId"], int), "userId должен быть числом"
        assert isinstance(data["id"], int), "id должен быть числом"
        assert isinstance(data["title"], str), "title должен быть строкой"
        assert isinstance(data["body"], str), "body должен быть строкой"

        print("✅ GET тест прошел успешно!")

    def test_get_all_posts(self):
        """Тест GET запроса для получения всех постов"""
        response = requests.get(f"{self.BASE_URL}/posts")

        assert response.status_code == 200
        posts = response.json()

        # Проверяем что это список
        assert isinstance(posts, list), "Ответ должен быть списком"

        # Проверяем что есть как минимум 1 пост
        assert len(posts) > 0, "Список постов не должен быть пустым"

        # Проверяем структуру первого поста
        first_post = posts[0]
        assert all(key in first_post for key in ['userId', 'id', 'title', 'body'])

        print("✅ GET ALL POSTS тест прошел успешно!")

    def test_create_post(self):
        """Тест POST запроса для создания поста"""
        new_post = {
            "title": "Мурз учит API тестированию",
            "body": "Это мой первый автотест с POST запросом!",
            "userId": 1
        }

        response = requests.post(f"{self.BASE_URL}/posts", json=new_post)

        # POST запрос должен вернуть статус 201 (Created)
        assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"

        # Проверяем ответ
        data = response.json()
        assert data["id"] == 101  # JSONPlaceholder всегда возвращает id=101 для новых постов
        assert data["title"] == new_post["title"]
        assert data["body"] == new_post["body"]
        assert data["userId"] == new_post["userId"]

        print("✅ POST тест прошел успешно!")

    def test_404_error(self):
        """Тест обработки ошибки 404"""
        response = requests.get(f"{self.BASE_URL}/posts/99999")  # Несуществующий пост

        assert response.status_code == 404, f"Ожидался статус 404, получен {response.status_code}"

        print("✅ 404 ERROR тест прошел успешно!")