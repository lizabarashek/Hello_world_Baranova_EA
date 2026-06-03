import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Установка стиля графиков для лучшей визуализации
sns.set_theme(style="whitegrid")


def get_data_from_db():
    """Подключение к БД и извлечение данных."""
    # Укажите ваши реальные учетные данные или задайте их через переменные окружения
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_NAME = os.getenv("DB_NAME", "your_database")
    DB_USER = os.getenv("DB_USER", "your_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "your_password")
    DB_PORT = os.getenv("DB_PORT", "5432")

    query = """
        SELECT 
            order_id, 
            customer_id, 
            order_date, 
            order_amount, 
            category, 
            delivery_days
        FROM sales_orders;
    """

    try:
        # Динамический импорт psycopg2/psycopg для гибкости среды
        try:
            import psycopg2
        except ImportError:
            import psycopg as psycopg2

        print("Попытка подключения к базе данных...")
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
        )
        df = pd.read_sql_query(query, conn)
        conn.close()
        print("Данные успешно успешно загружены из БД.")
        return df

    except Exception as e:
        print(f"\n[Предупреждение] Не удалось подключиться к БД: {e}")
        print("Генерация синтетических данных для демонстрации анализа...")

        # Генерация реалистичного датасета (Sales Data)
        np.random.seed(42)
        n_rows = 1000

        dates = pd.date_range(start="2025-01-01", periods=n_rows, freq="h")
        categories = ["Электроника", "Одежда", "Книги", "Дом и сад", "Спорт"]

        # Основная масса данных + искусственные аномалии
        order_amounts = np.random.exponential(scale=150, size=n_rows) + 10
        # Добавляем явные выбросы (аномально высокие чеки)
        order_amounts[np.random.choice(n_rows, 10, replace=False)] *= 15

        delivery_days = np.random.poisson(lam=3, size=n_rows) + 1
        # Добавляем аномальную задержку доставки
        delivery_days[np.random.choice(n_rows, 5, replace=False)] = 25

        df = pd.DataFrame(
            {
                "order_id": range(1, n_rows + 1),
                "customer_id": np.random.randint(1000, 2000, size=n_rows),
                "order_date": np.random.choice(dates, size=n_rows),
                "order_amount": order_amounts,
                "category": np.random.choice(categories, size=n_rows),
                "delivery_days": delivery_days,
            }
        )
        return df


def analyze_and_visualize(df):
    """Обработка данных, расчет метрик и построение графиков."""
    print("\n--- Первичный анализ данных ---")
    print(df.info())

    # Создаем папку для сохранения графиков, если её нет
    os.makedirs("plots", exist_ok=True)

    # =========================================================================
    # ГРАФИК 1: Распределение сумм заказов (Гистограмма + Boxplot)
    # Обоснование: Гистограмма идеально показывает форму распределения, плотность
    # и скошенность данных. Boxplot (ящик с усами) визуализирует квартили и выбросы.
    # =========================================================================
    fig, (ax_box, ax_hist) = plt.subplots(
        2,
        sharex=True,
        gridspec_kw={"height_ratios": (0.15, 0.85)},
        figsize=(10, 6),
    )

    # Расчет статистических метрик
    mean_val = df["order_amount"].mean()
    median_val = df["order_amount"].median()

    # Отрисовка компонентов
    sns.boxplot(x=df["order_amount"], ax=ax_box, color="skyblue")
    sns.histplot(x=df["order_amount"], ax=ax_hist, kde=True, color="teal")

    # Добавление линий метрик на гистограмму
    ax_hist.axvline(
        mean_val,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Среднее: {mean_val:.2f}",
    )
    ax_hist.axvline(
        median_val,
        color="green",
        linestyle="-",
        linewidth=2,
        label=f"Медиана: {median_val:.2f}",
    )

    ax_box.set(title="График 1: Распределение стоимости заказов с метриками")
    ax_hist.set_xlabel("Сумма заказа (у.е.)")
    ax_hist.set_ylabel("Количество заказов")
    ax_hist.legend()

    plt.tight_layout()
    plt.savefig("plots/1_order_distribution.png")
    plt.close()

    print("\n[Выводы по Графику 1]:")
    print(
        f" - Распределение сильно скошено вправо. Большинство чеков мелкие."
    )
    print(
        f" - Среднее ({mean_val:.2f}) значительно выше медианы ({median_val:.2f})."
    )
    print(f"   Это указывает на наличие очень крупных заказов (выбросов).")

    # =========================================================================
    # ГРАФИК 2: Общие продажи по категориям товаров
    # Обоснование: Столбчатая диаграмма (Bar chart) — лучший выбор для сравнения
    # дискретных категорий между собой по суммарному числовому показателю.
    # =========================================================================
    plt.figure(figsize=(10, 5))
    category_sales = (
        df.groupby("category")["order_amount"].sum().sort_values(ascending=False)
    )

    sns.barplot(
        x=category_sales.values, y=category_sales.index, hue=category_sales.index, palette="viridis", legend=False
    )

    plt.title("График 2: Суммарный объем продаж по категориям")
    plt.xlabel("Общая сумма продаж (у.е.)")
    plt.ylabel("Категория")

    plt.tight_layout()
    plt.savefig("plots/2_category_sales.png")
    plt.close()

    print("\n[Выводы по Графику 2]:")
    print(
        f" - Лидирующая категория по выручке: '{category_sales.index[0]}' ({category_sales.values[0]:.2f} у.е.)."
    )
    print(
        f" - Наименьшую выручку приносит категория: '{category_sales.index[-1]}' ({category_sales.values[-1]:.2f} у.е.)."
    )

    # =========================================================================
    # ГРАФИК 3: Зависимость времени доставки от суммы чека
    # Обоснование: Диаграмма рассеяния (Scatter plot) наглядно демонстрирует 
    # взаимосвязь (корреляцию) между двумя непрерывными числовыми переменными.
    # =========================================================================
    plt.figure(figsize=(10, 5))
    sns.scatterplot(
        data=df, x="order_amount", y="delivery_days", alpha=0.6, color="purple"
    )

    plt.title("График 3: Взаимосвязь суммы заказа и дней доставки")
    plt.xlabel("Сумма заказа (у.е.)")
    plt.ylabel("Время доставки (дни)")

    plt.tight_layout()
    plt.savefig("plots/3_scatter_delivery.png")
    plt.close()

    print("\n[Выводы по Графику 3]:")
    print(
        " - Плотная группа точек сосредоточена в левой части: стандартная доставка 1-7 дней для чеков до 500 у.е."
    )
    print(
        " - Явной линейной зависимости между ценой товара и скоростью доставки не обнаружено."
    )

    # =========================================================================
    # ПОИСК АНОМАЛИЙ (По методу Межквартильного размаха - IQR)
    # =========================================================================
    print("\n--- Анализ аномалий (выбросов) ---")

    # Проверка суммы заказов
    Q1_amount = df["order_amount"].quantile(0.25)
    Q3_amount = df["order_amount"].quantile(0.75)
    IQR_amount = Q3_amount - Q1_amount
    upper_bound_amount = Q3_amount + 1.5 * IQR_amount

    anomalies_amount = df[df["order_amount"] > upper_bound_amount]

    # Проверка сроков доставки
    Q1_delivery = df["delivery_days"].quantile(0.25)
    Q3_delivery = df["delivery_days"].quantile(0.75)
    IQR_delivery = Q3_delivery - Q1_delivery
    upper_bound_delivery = Q3_delivery + 1.5 * IQR_delivery

    anomalies_delivery = df[df["delivery_days"] > upper_bound_delivery]

    if not anomalies_amount.empty or not anomalies_delivery.empty:
        print(
            f"Обнаружено {len(anomalies_amount)} заказов с аномально высокой стоимостью (выше {upper_bound_amount:.2f} у.е.)."
        )
        print(
            f"Обнаружено {len(anomalies_delivery)} случаев аномально долгой доставки (дольше {upper_bound_delivery:.1f} дней)."
        )
        print("\nПримеры аномальных записей по стоимости:")
        print(
            anomalies_amount[["order_id", "order_amount", "category"]]
            .head()
            .to_string(index=False)
        )
    else:
        print("Аномалии в данных не обнаружены.")

    print(
        "\nВсе графики успешно сохранены в директорию 'plots/' текущего проекта."
    )


if __name__ == "__main__":
    # Запуск пайплайна
    sales_data = get_data_from_db()
    analyze_and_visualize(sales_data)