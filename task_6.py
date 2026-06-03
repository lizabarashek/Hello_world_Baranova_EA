import os
import pandas as pd
import numpy as np
import psycopg2

def get_data_from_db():
    """
    Пункт 1 & 2: Подключение к PostgreSQL-контейнеру и выполнение JOIN-запроса.
    """
    print("=== Пункт 1: Установка соединения с PostgreSQL ===")
    
    # Параметры подключения к вашей базе данных
    db_params = {
        "host": "localhost",
        "port": "5434",
        "user": "postgres",
        "password": "student",
        "database": "student_task"
    }
    
    # SQL-запрос для объединения таблиц согласно ТЗ
    query = """
        SELECT 
            p.product_id,
            pr.name AS product_name,
            pr.category,
            p.price
        FROM prices p
        JOIN products pr ON p.product_id = pr.product_id;
    """
    
    try:
        # Установка соединения
        conn = psycopg2.connect(**db_params)
        print("✅ Соединение с базой данных 'student_task' успешно установлено!")
        
        # Загрузка данных в pandas DataFrame
        print("\n=== Пункт 2: Выполнение SQL-запроса (JOIN) ===")
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        print(f"✅ Данные успешно извлечены. Загружено строк: {len(df)}")
        return df

    except Exception as e:
        print(f"❌ Не удалось подключиться к базе данных: {e}")
        print("\n[Внимание] Переключение на генерацию локального тест-датасета для проверки логики кода...")
        
        # Создание демонстрационного DataFrame (эмуляция таблиц products и prices)
        np.random.seed(42)
        mock_data = {
            'product_id': np.repeat(range(1, 11), 5), # 10 товаров, по 5 записей о ценах на каждый
            'product_name': np.repeat([f"Товар {i}" for i in range(1, 11)], 5),
            'category': np.repeat(['Электроника', 'Одежда', 'Книги', 'Бытовая техника', 'Спорт'][0:5], 10),
            'price': np.concatenate([
                np.random.normal(loc=15000, scale=3000, size=10), # Электроника
                np.random.normal(loc=2500, scale=400, size=10),   # Одежда
                np.random.normal(loc=800, scale=150, size=10),    # Книги
                np.random.normal(loc=25000, scale=5000, size=10), # Бытовая техника
                np.random.normal(loc=4500, scale=800, size=10)    # Спорт
            ]).round(2)
        }
        return pd.DataFrame(mock_data)

def perform_analysis(df):
    """
    Пункты 3 - 6: Статистический анализ данных.
    """
    if df.empty or 'price' not in df.columns:
        print("Ошибка: Данные пусты или отсутствует столбец 'price'.")
        return

    # -------------------------------------------------------------------------
    # Пункт 3: Базовые показатели для столбца price
    # -------------------------------------------------------------------------
    print("\n=== Пункт 3: Основные статистические показатели цен ===")
    mean_price = df['price'].mean()
    median_price = df['price'].median()
    std_price = df['price'].std()
    min_price = df['price'].min()
    max_price = df['price'].max()
    
    print(f"• Среднее значение:         {mean_price:,.2f} руб.")
    print(f"• Медиана:                  {median_price:,.2f} руб.")
    print(f"• Стандартное отклонение:   {std_price:,.2f} руб.")
    print(f"• Минимальная цена:         {min_price:,.2f} руб.")
    print(f"• Максимальная цена:        {max_price:,.2f} руб.")

    # -------------------------------------------------------------------------
    # Пункт 4: Квартили, IQR и дорогие товары (выше Q3)
    # -------------------------------------------------------------------------
    print("\n=== Пункт 4: Расчет квартилей и поиск дорогих товаров ===")
    q1 = df['price'].quantile(0.25)
    q2 = df['price'].quantile(0.50) # эквивалент медианы
    q3 = df['price'].quantile(0.75)
    iqr = q3 - q1
    
    print(f"• Первый квартиль (Q1):       {q1:,.2f} руб.")
    print(f"• Второй квартиль (Q2/Мед.):  {q2:,.2f} руб.")
    print(f"• Третий квартиль (Q3):       {q3:,.2f} руб.")
    print(f"• Межквартильный размах (IQR): {iqr:,.2f} руб.")
    
    # Поиск уникальных товаров, цена которых хоть раз превышала Q3
    expensive_df = df[df['price'] > q3][['product_name', 'category']].drop_duplicates()
    print(f"\nСписок товаров с ценой выше Q3 ({q3:,.2f} руб.):")
    if not expensive_df.empty:
        print(expensive_df.to_string(index=False, header=["Название товара", "Категория"]))
    else:
        print("Товары не найдены.")

    # -------------------------------------------------------------------------
    # Пункт 5: Группировка по категориям
    # -------------------------------------------------------------------------
    print("\n=== Пункт 5: Метрики цен в разрезе категорий (сортировка по убыванию средней цены) ===")
    category_summary = df.groupby('category')['price'].agg(
        Количество_записей='count',
        Средняя_цена='mean',
        Медиана='median',
        Стандартное_отклонение='std'
    ).sort_values(by='Средняя_цена', ascending=False)
    
    # Форматируем вывод для читаемости
    pd.set_option('display.float_format', lambda x: f'{x:,.2f} руб.')
    print(category_summary)

    # -------------------------------------------------------------------------
    # Пункт 6: Анализ разброса цен для каждого товара
    # -------------------------------------------------------------------------
    print("\n=== Пункт 6: Топ-5 товаров с наибольшим разбросом цен ===")
    # Группируем по товарам и находим min и max цены
    product_price_range = df.groupby('product_name')['price'].agg(['min', 'max'])
    # Рассчитываем разницу (разброс)
    product_price_range['разница'] = product_price_range['max'] - product_price_range['min']
    
    # Отбираем топ-5
    top_5_spread = product_price_range.sort_values(by='разница', ascending=False).head(5)
    
    print(top_5_spread.to_string(header=["Минимальная цена", "Максимальная цена", "Разброс цен"]))

if __name__ == "__main__":
    # Запуск аналитического конвейера
    data = get_data_from_db()
    perform_analysis(data)
