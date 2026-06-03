-- 1. Вывести все товары из таблицы products
SELECT * FROM products;

-- 2. Вывести только название и категорию всех товаров из таблицы products
SELECT name, category FROM products;

-- 3. Вывести список всех уникальных категорий товаров из таблицы products
SELECT DISTINCT category FROM products;


-- 4. Вывести все товары, отсортированные по названию в алфавитном порядке
SELECT * FROM products ORDER BY name ASC;

-- 5. Вывести все товары, отсортированные по названию в обратном алфавитном порядке
SELECT * FROM products ORDER BY name DESC;


-- 6. Вывести первые 10 товаров из таблицы products
SELECT * FROM products LIMIT 10;

-- 7. Вывести 10 товаров, начиная с 11‑й записи (пагинация)
SELECT * FROM products OFFSET 10 LIMIT 10;

-- 8. Вывести 5 случайных товаров из таблицы products
SELECT * FROM products ORDER BY RANDOM() LIMIT 5;

-- 9. Вывести все категории товаров (без DISTINCT), отсортированные по алфавиту
SELECT category FROM products ORDER BY category ASC;


-- 10. Вывести все товары, отсортированные сначала по категории, затем по названию
SELECT * FROM products ORDER BY category ASC, name ASC;
