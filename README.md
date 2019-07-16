# Рассчет надежности пароля

## Описание
Скрипт проверяет надежность пароля и выдает его оценку от 1(слабый) до 10 (сильный)

Требования к хорошему паролю:
* Длина пароля не менне 8 символов.
* Есть буквы как в нижнем регистре, так и в верхнем.
* Есть хотя бы одна цифра.
* Есть символы типа #$%.

## Требования

*Python3*

## Как запустить

```sh
git clone https://github.com/Safintim/6_password_strength.git
cd 6_password_strength
python 6_password_strength <password>
```

## Примеры

```sh
python 6_password_strength 123
Стойкость вашего пароля: 2
```

```sh
python 6_password_strength Ared47#fasd
Стойкость вашего пароля: 10
```

```sh
python 6_password_strength aredfs3d
Стойкость вашего пароля: 5
```

## Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
