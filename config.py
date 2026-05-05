from dotenv import load_dotenv
import os


load_dotenv(dotenv_path="Task_Management_Saas_Project/.env")

SECRET_CODE=os.getenv("SECRET_CODE")
ALGORITHM=os.getenv("ALGORITHM")
DATABASE_URL=os.getenv("DATABASE_URL")