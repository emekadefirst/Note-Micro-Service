import os
from dotenv import load_dotenv

load_dotenv()


JWT_ACCESS_EXPIRY = int(os.getenv('JWT_ACCESS_EXPIRY'))
JWT_REFRESH_EXPIRY = int(os.getenv('JWT_REFRESH_EXPIRY'))
JWT_ACCESS_SECRET = str(os.getenv('JWT_ACCESS_SECRET'))
JWT_ALGORITHM = str(os.getenv('JWT_ALGORITHM'))
ENCRYPTION_KEY = str(os.getenv('ENCRYPTION_KEY'))
DBURL = str(os.getenv('DBURL'))

