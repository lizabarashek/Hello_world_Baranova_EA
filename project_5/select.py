import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",          # База в контейнере, но доступна через localhost
        port="5434",               # Порт из секции ports
        user="postgres",           # POSTGRES_USER
        password="student",        # POSTGRES_PASSWORD
        database="student_task"          # POSTGRES_DB
    )
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, category FROM products;")
    products = cursor.fetchall()
    for product in products:
        print(f"ID: {product}, Название: {product}, Категория: {product}")
    cursor.close()
    connection.close()
except Exception as error:
    print(f"Ошибка при подключении или выполнении запроса: {error}")

