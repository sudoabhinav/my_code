import os
from dotenv import find_dotenv, load_dotenv
import boto3
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig
from botocore.exceptions import ClientError

load_dotenv(find_dotenv())

values = {
    "region_name":  os.getenv("REGION_NAME"),
    "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
    "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY")
}

client = boto3.client('secretsmanager', **values)
cache_config = SecretCacheConfig()
secret_cache = SecretCache( config = cache_config, client = client)

try:
    secret_name_value = secret_cache.get_secret_string(os.getenv("SECRET_MANAGER_KEY_READ", "SECRET_MANAGER_KEY_READ"))
    print(f"Secret value fetched from AWS Secret Manager is: {secret_name_value}")
except ClientError as e:
    print(f"Got client error with exception as: {e}")
except Exception as e:
    print(f"general exception occured: {e}")


try:
    response = client.create_secret(Name=os.getenv("SECRET_MANAGER_KEY_WRITE", "SECRET_MANAGER_KEY_WRITE"), SecretString="secret_string")
except ClientError as e:
    print(f"Secret already present, updating value for the key {os.getenv('SECRET_MANAGER_KEY_WRITE', 'SECRET_MANAGER_KEY_WRITE')}")
    response = client.put_secret_value(SecretId=os.getenv("SECRET_MANAGER_KEY_WRITE", "SECRET_MANAGER_KEY_WRITE"), SecretString="secret_string")
except Exception as e:
    print(f"error in creatng / updating the secret value: {e}")
