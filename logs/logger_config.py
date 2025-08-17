import logging
import os

if not os.path.exists('logs'):
    os.mkdir('logs')

logging.basicConfig(
    filename='logs/project.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d__%H:%m:%s'

)
logger = logging.getLogger("Project_Logger")