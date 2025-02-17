import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

db_config = {
    'host': os.environ.get('POSTGRESQLCONNSTR_DBHOST'),
    'user': os.environ.get('POSTGRESQLCONNSTR_DBUSER'),
    'password': os.environ.get('POSTGRESQLCONNSTR_DBPASSWORD'),
    'database': os.environ.get('POSTGRESQLCONNSTR_DBNAME'),
    'sslmode': os.environ.get('POSTGRESQLCONNSTR_SSLMODE'),
    'port': 5432
}

def get_data_from_db():
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT plant_name, plant_quantity_in_stock, plant_base_selling_price, plant_minimum_selling_price, plant_discounted_selling_price, plant_discount_percentage, plant_type_airpurifier, plant_type_balcony, plant_type_bonsai, plant_type_cactus, plant_type_creeper, plant_type_succulent, plant_type_tabletop, plant_type_medicinal, plant_type_ornamental, plant_total_sold FROM plants")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return data