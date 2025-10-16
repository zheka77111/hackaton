# Отчёт по заданию №1

## Общие сведения:
- Целевой объект: 10.62.34.10
- Методы тестирования: Hydra, nmap

## Результаты проверки:
- Уязвимые сервисы:
  * SSH (порт 22)
  * FTP (порт 212)
  * HTTP (порты 80 и 700)

## Найденные учётные записи:
| Сервис | Логин | Пароль |
|--------|-------|--------|
| SSH    | admin | protect |
| SSH    | uftp  | clock   |
| FTP    | admin | protect |
| FTP    | uftp  | clock   |
| HTTP   | admin | protect |
| HTTP   | admin | 666     |
| HTTP   | admin | clock   |
| HTTP   | admin | 123456  |
| HTTP   | user  | protect |
| HTTP   | user  | 666     |
| HTTP   | user  | clock   |
| HTTP   | user  | 123456  |
| HTTP   | uftp  | protect |
| HTTP   | uftp  | 666     |
| HTTP   | uftp  | clock   |
| HTTP   | uftp  | 123456  |
| HTTP   | usmb  | protect |
| HTTP   | usmb  | 666     |
| HTTP   | usmb  | clock   |
| HTTP   | usmb  | 123456  |
