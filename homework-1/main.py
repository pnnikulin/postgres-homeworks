"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv
import os
import psycopg2

"""Создаём путь к файлам csv"""
PATH = os.path.abspath('.')
PATH_TO_CUSTOMERS_DATA = os.path.join(PATH, 'north_data', 'customers_data.csv')
PATH_TO_EMPLOYEES_DATA = os.path.join(PATH, 'north_data', 'employees_data.csv')
PATH_TO_ORDERS_DATA = os.path.join(PATH, 'north_data', 'orders_data.csv')


def adding_into_table_customers():
    with psycopg2.connect(host='localhost', database='north', user='admin', password='12345678') as conn:
        with conn.cursor() as cur:
            with open(PATH_TO_CUSTOMERS_DATA, 'r', encoding='utf-8') as csvfile:
                data_csv = csv.DictReader(csvfile)
                for row in data_csv:
                    customer_id = row["customer_id"]
                    company_name = row["company_name"]
                    contact_name = row["contact_name"]
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (customer_id, company_name, contact_name))
                    # cur.execute('SELECT * FROM customers')
                    conn.commit()

def adding_into_table_employees():
    with psycopg2.connect(host='localhost', database='north', user='admin', password='12345678') as conn:
        with conn.cursor() as cur:
            with open(PATH_TO_EMPLOYEES_DATA, 'r', encoding='utf-8') as csvfile:
                data_csv = csv.DictReader(csvfile)
                for row in data_csv:
                    employee_id = row["employee_id"]
                    first_name = row["first_name"]
                    last_name = row["last_name"]
                    title = row["title"]
                    birth_date = row["birth_date"]
                    notes = row["notes"]
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                                (employee_id, first_name, last_name, title, birth_date, notes))
                    # cur.execute('SELECT * FROM customers')
                    conn.commit()

def adding_into_table_orders():
    with psycopg2.connect(host='localhost', database='north', user='admin', password='12345678') as conn:
        with conn.cursor() as cur:
            with open(PATH_TO_ORDERS_DATA, 'r', encoding='utf-8') as csvfile:
                data_csv = csv.DictReader(csvfile)
                for row in data_csv:
                    order_id = row["order_id"]
                    customer_id = row["customer_id"]
                    employee_id = row["employee_id"]
                    order_date = row["order_date"]
                    ship_city = row["ship_city"]
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                                (order_id, customer_id, employee_id, order_date, ship_city))
                    # cur.execute('SELECT * FROM customers')
                    conn.commit()


if __name__ == '__main__':
    adding_into_table_customers()
    adding_into_table_employees()
    adding_into_table_orders()
