from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    print("Warning: .env file not found!")
else:
    load_dotenv()