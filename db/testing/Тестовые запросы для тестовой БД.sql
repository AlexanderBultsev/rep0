

UPDATE "Пользователи" SET registration_date = SUBSTR(registration_date, 7, 4) || '-' || SUBSTR(registration_date, 4, 2) || '-' || SUBSTR(registration_date, 1, 2);


SELECT login, MAX (registration_date) FROM "Пользователи";


SELECT DISTRINCT(SUBSTR(birth_date, 1, 4)) FROM "Пользователи";


SELECT COUNT(*) AS 'total_items' FROM "Товары";


SELECT AVG(birth_date) FROM "Пользователи" GROUP BY id HAVING (date('now') - registration_date) <= '0000-02-00 00:00:00';