import psycopg2
from psycopg2 import Error

def main():
    try:
        # Устанавливаем соединение с БД
        connection = psycopg2.connect(
            host="localhost",      
            port="5434",         
            user="postgres",     
            password="student",   
            database="student_task"    
        )
        cursor = connection.cursor()
        sql_query = "SELECT id, name, category FROM products WHERE category = 'Электроника';"
        cursor.execute(sql_query)
        results = cursor.fetchall()
        print("Товары из категории 'Электроника':")
        for row in results:
            print(f"ID: {row}, Название: {row}, Категория: {row}")
    except Error as e:
        print(f"Ошибка при работе с PostgreSQL: {e}")
    finally:  
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с базой данных закрыто.")

if __name__ == "__main__":
    main()
