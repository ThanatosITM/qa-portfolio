# API Autotests Project

## Описание проекта
Автоматизированные тесты для JSONPlaceholder API


## 🚀 Быстрый запуск

### Одиночный запуск тестов
```bash
  pytest tests/test_api.py -v
```

### Многократный запуск: ###
```bash  
  pytest tests/test_api.py --count=3 -v
```

### Создание отчета
```bash
  pytest tests/test_api.py --html=report.html --self-contained-html
```

### Многократный запуск с детальным отчетом
```bash
  pytest tests/test_api.py --count=3 -v -s --html=report.html
```

### Создание Allure отчета

### Генерация результатов
```bash
  pytest tests/test_api.py --alluredir=allure-results
```

### Просмотр отчета
```bash
  allure serve allure-results
```