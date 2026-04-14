import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth


# Налаштування логування
def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Формат повідомлень
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Логування у файл
    file_handler = logging.FileHandler('test_search.log', mode='w', encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


setup_logging()


class TestCarsAPI:
    base_url = "http://127.0.0.1:8080"

    @pytest.fixture(scope='class')
    def auth_session(self):
        """Фікстура для аутентифікації, що створює сесію на рівні класу."""
        session = requests.Session()
        auth_url = f"{self.base_url}/auth"

        logging.info(f"Спроба аутентифікації для користувача: test_user")

        # Використовуємо HTTPBasicAuth згідно з документацією
        response = session.post(
            auth_url,
            auth=HTTPBasicAuth('test_user', 'test_pass')
        )

        if response.status_code == 200:
            token = response.json().get("access_token")
            session.headers.update({'Authorization': f'Bearer {token}'})
            logging.info("Аутентифікація успішна, токен отримано.")
            return session
        else:
            logging.error(f"Помилка аутентифікації! Статус: {response.status_code}")
            pytest.fail(f"Failed to authenticate. Status code: {response.status_code}")

    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 10),
        ("price", 1),
        (None, 7),  # Перевірка роботи без сортування
        ("year", None),  # Перевірка роботи без ліміту
        ("brand", 5)  # Сортування за брендом
    ])
    def test_search_cars(self, auth_session, sort_by, limit):
        """Тест пошуку автомобілів з різними параметрами."""
        params = {}
        if sort_by:
            params['sort_by'] = sort_by
        if limit:
            params['limit'] = limit

        logging.info(f"Запуск тесту: GET /cars з параметрами: {params}")

        response = auth_session.get(f"{self.base_url}/cars", params=params)

        # Логування результату запиту
        logging.info(f"Отримано статус: {response.status_code}")

        # Перевірки (Assertions)
        assert response.status_code == 200, f"Очікувався статус 200, але отримано {response.status_code}"

        data = response.json()
        assert isinstance(data, list), "Відповідь має бути списком"

        if limit:
            assert len(data) <= limit, f"Кількість результатів ({len(data)}) перевищує ліміт ({limit})"
            logging.info(f"Перевірка ліміту пройдена: отримано {len(data)} записів.")

        if data and sort_by and len(data) > 1:
            # Перевірка валідності сортування (простий приклад для зростання)
            # В реальному проекті тут варто додати логіку порівняння елементів
            logging.info(f"Перевірка наявності поля сортування '{sort_by}' у першому елементі.")
            assert sort_by in data[0], f"Поле {sort_by} відсутнє в даних відповіді"

        logging.info("-" * 30)