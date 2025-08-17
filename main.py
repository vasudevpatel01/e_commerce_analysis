import sys
sys.path.append(r'c:\Users\SHWETA\Downloads\GPT_synData_proj')
from scripts.data_cleaning import clean_data
from config.db_config import DB_CONFIG
from scripts.create_df import create_df
from logs.logger_config import logger
from scripts.run_nb import run_notebook



def main():
    try:
        clean_data(**DB_CONFIG)
        customers_df,orders_df,products_df = create_df(**DB_CONFIG)
        # run_notebook()           
        

        logger.info("Workflow completed successfully")
        print("Workflow Completed")
    except Exception as e:
        logger.error(f"An error occurred in main script: {e}")
        print("An error occurred in the main script, check logs for details.")
    



if __name__ =="__main__":
    main()