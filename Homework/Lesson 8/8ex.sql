-- Урок 8. Вебинар
/* Задача 1.1
Пусть задан некоторый пользователь. 
Из всех пользователей соц. сети найдите человека, 
который больше всех общался с выбранным пользователем (написал ему сообщений).
*/
-- вывод данных
SELECT 
users.id, firstname, lastname, messages.to_user_id, count(*) AS counter
FROM users
	JOIN messages ON users.id = messages.from_user_id AND messages.to_user_id = 14
GROUP BY id
ORDER BY counter DESC
LIMIT 1;

/* Задача 1.2
Подсчитать общее количество лайков, которые получили пользователи младше 10 лет.
*/
-- вывод данных
SELECT 
profiles.user_id, profiles.birthday, count(*)
FROM likes
	JOIN profiles ON profiles.user_id = likes.user_id
	JOIN media ON media.id = likes.media_id AND (date(NOW())-date(profiles.birthday))/10000 < 10;

/* Задача 1.3
Определить кто больше поставил лайков (всего): мужчины или женщины.
*/
-- вывод данных
SELECT profiles.user_id, gender,count(*) AS counter
FROM profiles
	JOIN likes ON profiles.user_id = likes.user_id
GROUP BY gender
ORDER BY counter DESC
LIMIT 1 ;




