-- 1. Вывести 5 самых дорогих записей из таблицы prices
SELECT * FROM prices ORDER BY price DESC LIMIT 5;

-- 2. Вывести 10 последних добавленных записей из таблицы prices, отсортированных по полю created_at
SELECT * FROM prices ORDER BY created_at DESC LIMIT 10;

-- 3. Вывести 10 самых дешёвых цен из таблицы prices
SELECT * FROM prices ORDER BY price ASC LIMIT 10;

-- 4. Вывести записи из таблицы prices: пропустить первые 20 самых дорогих значений и отобразить следующие (следующие 10 записей)
SELECT * FROM prices ORDER BY price DESC OFFSET 20 LIMIT 10;
