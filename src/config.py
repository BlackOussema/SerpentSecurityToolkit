class Config:
    """Configuration settings for the Flask application."""
    
    DEBUG = True  # Set to False in production
    SECRET_KEY = 'your_secret_key_here'  # Change this to a random secret key
    DATABASE_URI = 'sqlite:///your_database.db'  # Example database URI
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Allowed hosts for the application
    LOGGING_LEVEL = 'DEBUG'  # Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    
    # Add any additional configuration settings as needed
