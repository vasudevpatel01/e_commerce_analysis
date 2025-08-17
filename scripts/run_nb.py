import papermill as pm
import sys
sys.path.append(r'c:\Users\SHWETA\Downloads\GPT_synData_proj')
from logs.logger_config import logger



import papermill as pm
import os
try:
    def run_notebook():
        input_path = os.path.join("notebook", "analysis.ipynb")
        output_path = os.path.join("notebook", "analysis_output.ipynb")
        pm.execute_notebook(input_path, output_path)
        logger.info("Notebook executed successfully")
        print("Notebook executed successfully")
except Exception as e:
    logger.error(f"Error running notebook: {e}")
    print(f"Error running notebook, check logs for details: {e}")