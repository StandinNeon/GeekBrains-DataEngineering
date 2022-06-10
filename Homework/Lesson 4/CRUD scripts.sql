USE vk;
-- ii. Написать скрипт, возвращающий список имен (только firstname) пользователей без повторений в алфавитном порядке
-- iii. Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = false). 
-- Предварительно добавить такое поле в таблицу profiles со значением по умолчанию = true (или 1)
-- iv. Написать скрипт, удаляющий сообщения «из будущего» (дата больше сегодняшней)

SELECT DISTINCT firstname FROM users ORDER BY firstname ASC;

UPDATE vk.profiles
SET is_active = FALSE
WHERE date(NOW()) - birthday < 180000;

UPDATE vk.messages 
SET is_active = FALSE
WHERE date(NOW()) - birthday < 180000;

DELETE FROM vk.messages
WHERE created_at > date(NOW());


































































