import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

print(f"Value of test env variable is: {os.getenv('test_var', 'value not found in env file')}")