-- Урок 6. Вебинар.
/* Задача 1
Пусть задан некоторый пользователь. Из всех пользователей соц. сетей найдите человека, 
который больше всех общался с выбранным пользователем (написал ему сообщений).
*/
-- выборки данных
SELECT count(from_user_id) AS from_count, from_user_id, to_user_id  FROM messages
WHERE to_user_id = 14 GROUP BY from_user_id ORDER BY from_count DESC LIMIT 1;

/* Задача 2
Подсчитать общее количество лайков, которые получиили пользователи младше 10 лет.
*/
-- выборки данных
SELECT profiles.user_id, profiles.birthday, likes.id 
FROM profiles, likes 
WHERE (date(NOW())-date(profiles.birthday))/10000 < 10 AND profiles.user_id = likes.user_id 
GROUP BY likes.id;

/* Задача 3
Определить, кто поставил больше лайков (в основном мужчины или женщины).
*/
-- выборки данных
SELECT profiles.user_id, profiles.gender, count(gender) AS 'likes_gender' 
FROM profiles, likes 
WHERE profiles.user_id = likes.user_id
GROUP BY profiles.gender
ORDER BY likes_gender DESC LIMIT 1;

