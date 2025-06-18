

import os
from pathlib import Path

project_name = "app"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/main.py",
    f"{project_name}/routes/__init__.py",
    f"{project_name}/routes/user.py",
    f"{project_name}/models/__init__.py",
    f"{project_name}/models/mysql_models.py",
    f"{project_name}/models/mongo_models.py",
    f"{project_name}/database/__init__.py",
    f"{project_name}/database/mysql.py",
    f"{project_name}/database/mongo.py",
    f"{project_name}/templates/__init__.py",
    f"{project_name}/templates/index.py",
    f"{project_name}/static/__init__.py",
    f"{project_name}/static/style.css",
    # f"{project_name}/configuration/aws_connection.py",
    # f"{project_name}/cloud_storage/__init__.py",
    # f"{project_name}/cloud_storage/aws_storage.py",
    # f"{project_name}/data_access/__init__.py",
    # f"{project_name}/data_access/proj1_data.py",
    # f"{project_name}/constants/__init__.py",
    # f"{project_name}/entity/__init__.py",
    # f"{project_name}/entity/config_entity.py",
    # f"{project_name}/entity/artifact_entity.py",
    # f"{project_name}/entity/estimator.py",
    # f"{project_name}/entity/s3_estimator.py",
    # f"{project_name}/exception/__init__.py",
    # f"{project_name}/logger/__init__.py",
    # f"{project_name}/pipline/__init__.py",
    # f"{project_name}/pipline/training_pipeline.py",
    # f"{project_name}/pipline/prediction_pipeline.py",
    # f"{project_name}/utils/__init__.py",
    # f"{project_name}/utils/main_utils.py",
    "run.py",
    "requirements.txt",
    "README.md"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")