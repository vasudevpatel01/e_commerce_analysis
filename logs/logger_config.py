import logging
import os

if not os.path.exists('logs'):
    os.mkdir('logs')


logging.basicConfig(
    level=logging.DEBUG,
    filename=r'C:\Users\SHWETA\Downloads\GPT_synData_proj\logs\project.log',
    filemode='a',
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("Project_Logger")
logger.setLevel(logging.DEBUG)

