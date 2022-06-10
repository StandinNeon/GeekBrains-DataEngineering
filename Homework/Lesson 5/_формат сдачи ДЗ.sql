-- Урок 5. Видеоурок
/* Задача 1.1
Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.
*/
-- обновление данных
UPDATE shop.users
SET created_at=CURRENT_TIMESTAMP, updated_at=CURRENT_TIMESTAMP;

/* Задача 1.2
Таблица users была неудачно спроектирована. 
Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения в формате "20.10.2017 8:10". 
Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения.
*/
-- изменение таблицы
ALTER TABLE shop.users 
	MODIFY created_at datetime DEFAULT CURRENT_TIMESTAMP,
	MODIFY updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

/* Задача 1.3
В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 
0, если товар закончился и выше нуля, если на складе имеются запасы. 
Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value. 
Однако, нулевые запасы должны выводиться в конце, после всех записей.
*/
-- вывод данных
SELECT * FROM storehouses_products ORDER BY value = 0 ASC;

/* Задача 2.1
Подсчитайте средний возраст пользователей в таблице users
*/
-- вывод данных
SELECT round(AVG(date(now())-birthday_at)/10000, 1) AS average_age FROM users;

/* Задача 2.2
Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. 
Следует учесть, что необходимы дни недели текущего года, а не года рождения.
*/
-- вывод данных
SELECT DAYNAME(birthday_at + round(datediff(date(NOW()), date(birthday_at))/365,0)*10000) AS week_name, count(id) AS counter
FROM users
GROUP BY week_name
ORDER BY week_name;