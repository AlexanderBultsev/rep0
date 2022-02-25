/* Найти предметы определенной редкости */
/* Вместо <'Arcana'> указывается редкость */

SELECT
	ID,
	Name,
	(SELECT Rarity_name FROM Rarity WHERE ID = Rarity_ID) AS "Rarity",
	(SELECT Hero_name FROM Hero WHERE ID = Hero_ID) AS "Hero",
	Price
FROM Products
WHERE Rarity_ID = (SELECT ID FROM Rarity WHERE Rarity_name = 'Arcana');


/* Найти предметы на определенного героя */
/* Вместо <'Pudge'> указывается герой */

SELECT
	ID,
	Name,
	(SELECT Rarity_name FROM Rarity WHERE ID = Rarity_ID) AS "Rarity",
	(SELECT Hero_name FROM Hero WHERE ID = Hero_ID) AS "Hero",
	Price
FROM Products
WHERE Hero_ID = (SELECT ID FROM Hero WHERE Hero_name = 'Pudge');


/* Найти предметы определенной редкости на определенного героя */
/* Вместо <'Arcana'> указывается редкость, вместо <'Pudge'> - герой */

SELECT
	ID,
	Name,
	(SELECT Rarity_name FROM Rarity WHERE ID = Rarity_ID) AS "Rarity",
	(SELECT Hero_name FROM Hero WHERE ID = Hero_ID) AS "Hero",
	Price
FROM Products
WHERE 
	Hero_ID = (SELECT ID FROM Hero WHERE Hero_name = 'Pudge')
	AND Rarity_ID = (SELECT ID FROM Rarity WHERE Rarity_name = 'Arcana');


/* Найти предметы стоимости от <MinPrice> до <MaxPrice> */
/* Вместо 1000 указывается <MinPrice>, вместо 1700 - <MaxPrice> */

SELECT
	ID,
	Name,
	(SELECT Rarity_name FROM Rarity WHERE ID = Rarity_ID) AS "Rarity",
	(SELECT Hero_name FROM Hero WHERE ID = Hero_ID) AS "Hero",
	Price
FROM Products
WHERE 
	Price BETWEEN 1000 AND 1700


/* Отсортировать предметы по редкости и стоимости */

SELECT
	ID,
	Name,
	(SELECT Rarity_name FROM Rarity WHERE ID = Rarity_ID) AS "Rarity",
	(SELECT Hero_name FROM Hero WHERE ID = Hero_ID) AS "Hero",
	Price
FROM Products
ORDER
	BY Rarity_ID DESC, Price ASC