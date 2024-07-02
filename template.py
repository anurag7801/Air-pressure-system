from pathlib import Path
import os
import logging

PROJECT_NAME = 'sensor'
list_of_files = [
    f"{PROJECT_NAME}/__init__.py",
    f"{PROJECT_NAME}/logging/__init__.py",
    f"{PROJECT_NAME}/logging/logger.py",
    f"{PROJECT_NAME}/exception/__init__.py",
    f"{PROJECT_NAME}/exception/exception.py",
    f"{PROJECT_NAME}/components/__init__.py",
    f"{PROJECT_NAME}/components/data_ingestion.py",
    f"{PROJECT_NAME}/components/data_validation.py",
    f"{PROJECT_NAME}/components/data_transformation.py",
    f"{PROJECT_NAME}/components/model_trainer.py",
    f"{PROJECT_NAME}/components/model_pusher.py",
    f"experiments/experiments.ipynb",
    f"config/config.yaml",
    "setup.py",
    'requirements.txt',
    "main.py",
    "app.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created file directory : {filedir}")
    
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            logging.info(f"Created file : {filename}")
            pass

    else:
        logging.info(f"file is already present as : {filepath}")