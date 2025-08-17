import papermill as pm
import sys
sys.path.append(r'c:\Users\SHWETA\Downloads\GPT_synData_proj')
from logs.logger_config import logger

def run_notebook(
        input_path = r'C:\Users\SHWETA\Downloads\GPT_synData_proj\notebook\analysis.ipynb',
        output_path = r'C:\Users\SHWETA\Downloads\GPT_synData_proj\notebook\analysis_output.ipynb'):
    try:
        pm.execute_notebook(input_path,output_path)
        logger.info("Notebook run successful")

    except Exception as e:
        logger.error(f"Error running notebook: {e}")
        print(f"Error running notebook, check logs for details.")
