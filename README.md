# Викторов Борис Лабораторная 4.

## Данные: Palmer Archipelago (Antarctica) penguin data

## Модели: LOG_REG, RAND_FOREST, KNN, SVM, GNB, D_TREE

# Структура
```
.
├── CD
├── CI
├── data
├── db-data
├── experiments
│   └── exp_test_0_2026_03_06_18_00_59
├── git@github.com:BorisVIkVik
│   └── Penguins_Data_Science_4lab_Kafka.git
│       └── files
│           └── md5
│               └── 97
├── notebooks
├── src
│   ├── __pycache__
│   ├── api
│   │   └── __pycache__
│   ├── db
│   ├── kafka_workers
│   └── unit_tests
└── tests

```

Код разбит на папки:

    data: Папка для данных

    src: Папка для основного кода, где находится логгирование, предобработка данных, обучение, тестирование и API.

    notebooks: Папка для Jupyter Notebooks с экспериментами и EDA

    CI: Папка для Jenkinsfile CI

    CD: Папка для Jenkinsfile CD

## Docker
Для кода написан docker-compose.yml и DockerFile.

## Api 
Реализован POST запрос "/api/predict" для того, чтобы на основе обученных моделей делать классификацию пингвинов.

## БД: PostgreSQL
Добавлена в docker-compose.yml 
В неё сохраняется результат классификации POST запроса.

## Хранилище секретов: Hashicorp Vault
Добавлена в docker-compose.yml 
В vault кладётся пароль от БД. API сервер при запуске получает пароль от БД из vault.

## Добавлена Kafka
Producer создаёт рандомные данные пингвина.
Consumer делате классификацию по данным, который получает от producer через Kafka.