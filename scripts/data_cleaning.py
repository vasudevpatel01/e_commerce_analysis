from sqlalchemy import create_engine,text
from sqlalchemy.exc import SQLAlchemyError
import sys
sys.path.append(r'c:\Users\SHWETA\Downloads\GPT_synData_proj')
from logs.logger_config import logger

def clean_data(user,password,DB,host="localhost"):
    try:
        engine = create_engine(f"mysql+pymysql://{user}:{password}@localhost/{DB}")
        try:
            with engine.connect() as conn:
                conn.execute(text("""
                    DELETE FROM orders WHERE customer_id IS NULL OR product_id IS NULL;"""))
                conn.execute(text("""
                    UPDATE products SET price = 0 WHERE price < 0;"""))
                conn.execute(text("""
                    UPDATE customers SET email = 'N/A' WHERE email IS NULL;"""))
                conn.execute(text("""
                    UPDATE customers SET country = 'N/A' WHERE country IS NULL;"""))
                conn.execute(text("""
                    DELETE FROM orders WHERE status = 'Cancelled' """))
        
                conn.commit()
                logger.info("Data cleaning completed successfully")
                print(" Cleaning completed on MySQL server.")
        except SQLAlchemyError as e:
            conn.rollback()
            logger.error(f"Error during data cleaning: {e}")
            print(f"Error occured in data_cleaning,check logs")

    except SQLAlchemyError as e:
        logger.error(f"Error connecting to MySQL server,{e}")
        print("Couldn't connect to the MySQL server in data_cleaning,check logs")




