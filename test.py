import os
from dotenv import load_dotenv  # python-dotenv 라이브러리를 import

# .env 파일 로드
load_dotenv()

apikey = os.getenv("FLASK_API_KEY")
print(apikey)