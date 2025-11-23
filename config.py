"""
Configuration file for Smart Garden App
Loads environment variables from Streamlit secrets (Cloud) or .env file (Local)
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

def get_api_key(key_name):
    """
    Get API key from Streamlit Cloud Secrets first, then fallback to local .env
    Priority: st.secrets > .env file > None
    
    This function is called at runtime when Streamlit is already initialized
    """
    # Try to get key from Streamlit Cloud Secrets first
    try:
        import streamlit as st
        if hasattr(st, 'secrets') and st.secrets and key_name in st.secrets:
            return st.secrets[key_name]
    except:
        pass
    
    # Fallback to local .env (for when you run on VS Code)
    return os.getenv(key_name)

# API Keys
# These will be loaded at runtime when Streamlit is initialized
# Priority: Streamlit Cloud secrets > .streamlit/secrets.toml > .env file > None
# IMPORTANT: Never commit API keys to GitHub!

# We'll use a function that gets called after Streamlit initializes
# For now, set to None - they'll be loaded dynamically
OPENWEATHER_API_KEY = None
GEMINI_API_KEY = None
GROQ_API_KEY = None
PERENUAL_API_KEY = None
HUGGINGFACE_API_KEY = None

# Default Settings
DEFAULT_LOCATION = os.getenv("DEFAULT_LOCATION", "Sialkot,PK")
DEFAULT_CITY = "Sialkot"
DEFAULT_COUNTRY = "PK"

def load_api_keys():
    """
    Load API keys from secrets or environment variables
    Call this function after Streamlit is initialized (in app.py)
    """
    global OPENWEATHER_API_KEY, GEMINI_API_KEY, GROQ_API_KEY, PERENUAL_API_KEY, HUGGINGFACE_API_KEY, DEFAULT_LOCATION
    
    # Load keys using the robust pattern: st.secrets first, then os.getenv
    OPENWEATHER_API_KEY = get_api_key("OPENWEATHER_API_KEY")
    GEMINI_API_KEY = get_api_key("GEMINI_API_KEY")
    GROQ_API_KEY = get_api_key("GROQ_API_KEY")
    PERENUAL_API_KEY = get_api_key("PERENUAL_API_KEY")
    HUGGINGFACE_API_KEY = get_api_key("HUGGINGFACE_API_KEY")
    
    DEFAULT_LOCATION = get_api_key("DEFAULT_LOCATION") or os.getenv("DEFAULT_LOCATION", "Sialkot,PK")

# API Endpoints
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5"
PERENUAL_BASE_URL = "https://perenual.com/api"

# Data Storage
PLANTS_DB_FILE = "plants_database.json"
CHAT_HISTORY_FILE = "chat_history.json"

# App Settings
WATERING_CHECK_TIME = "08:00"  # Daily check time
MAX_PLANTS = 50  # Maximum number of plants user can add

