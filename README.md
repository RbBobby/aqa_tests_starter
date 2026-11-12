# API Tests

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requairements.txt
```

## Запуск тестов

Запускайте команды из корня проекта с активированным виртуальным окружением:

```bash
python -m pytest
```

Тесты обращаются к внешнему API automationexercise.com и требуют доступа к сети.
Allure автоматически сохраняет результаты в `allure-results/`. Перед каждым
запуском папка очищается, чтобы отчёт содержал только текущий прогон.

Для запуска только smoke-тестов:

```bash
python -m pytest -m smoke
```

## Просмотр отчёта Allure

`allure-pytest` установлен вместе с Python-зависимостями. Для просмотра HTML-отчёта
дополнительно установите Allure CLI по [официальной инструкции](https://allurereport.org/docs/pytest/).
Проверьте установку командой `allure --version`, затем после запуска тестов выполните:

```bash
allure serve allure-results
```

Команда сформирует отчёт и откроет его в браузере. Чтобы сохранить HTML-отчёт:

```bash
allure generate allure-results --clean -o allure-report
```

Папки `allure-results/` и `allure-report/` исключены из Git.
=======
pip3 install -r requirements.txt

## Запуск тестов

python -m pytest -v
