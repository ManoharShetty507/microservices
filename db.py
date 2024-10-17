from pymongo import MongoClient
from urllib.parse import quote_plus

username = 'admin123'  # Your MongoDB username
password = 'admin123'  # Replace with your actual password
password_encoded = quote_plus(password)

# Attempt to connect using the SRV connection string
try:


    client = MongoClient('mongodb://admin123:admin123@mongodb:27017/')
    db = client['your_database_name']
    users_collection = db['users']  # Make sure this collection exists

    print("MongoDB connection successful!")

except Exception as e:
    print(f"Error while connecting to MongoDB with SRV: {e}")
    # Attempt to connect using standard connection string (update with your actual hosts)
    try:
        client = MongoClient(f"mongodb://{username}:{password_encoded}@<host1>:<port1>,<host2>:<port2>,<host3>:<port3>/myDatabaseName?ssl=true&authSource=admin")
        client.admin.command('ping')  # Test connection
        print("MongoDB connection successful with direct connection!")
    except Exception as e:
        print(f"Error while connecting to MongoDB with direct connection: {e}")
