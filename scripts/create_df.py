from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
import sys
sys.path.append(r'c:\Users\SHWETA\Downloads\GPT_synData_proj')
from config.db_config import DB_CONFIG
from logs.logger_config import logger



def create_df(user,password,DB,host='localhost'):
    try:
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{DB}")

        customers_df = pd.read_sql(
            "SELECT customer_id, signup_date, country FROM customers", con=engine
        )
        products_df = pd.read_sql(
            "SELECT product_id, product_name, category, price FROM products", con=engine
        )
        orders_df = pd.read_sql(
            "SELECT order_id, order_date,product_id, quantity, total_amount, payment_method, status FROM orders", con=engine
        )
        return customers_df,orders_df,products_df
        logger.info("DataFrames created successfully")
        print("DataFrames created successfully")
        
    except SQLAlchemyError as e:
        logger.error(f"Error while connecting to the DataBase {e}")
        print(f"Database error, check logs")
        return None,None,None

    except Exception as e:
        logger.error("Error while creating DataFrames", e )
        print("Error,check logs")
        return None, None, None
