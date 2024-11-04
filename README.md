### 1. Application Requirements
The application is a simple but effective demonstration of an optimized, scalable web service. Here's the breakdown of the components:
- **Web Service**: A FastAPI application deployed on Azure Web Apps.
- **Database**: An SQL database (like Azure SQL Database) for data persistence.
- **Blob Storage**: Azure Blob Storage for file storage (e.g., user uploads).
- **Caching**: Redis Cache on Azure for performance optimization.
- **Secret Management**: Azure Key Vault for managing secrets like database connection strings or API keys.
- **Containerization**: Dockerize the application and push it to the Azure Container Registry.

### 2. Project Structure

```
/project-root
│
├── /app
│   ├── main.py        # FastAPI entry point
│   ├── routes.py      # API endpoints
│   ├── models.py      # SQLAlchemy models
│   ├── config.py      # Configuration, including Azure Key Vault integration
│   ├── database.py    # Database connection and session management
│   ├── storage.py     # Azure Blob Storage operations
│   ├── cache.py       # Redis Cache operations
│   └── utils.py       # Utility functions
│
├── Dockerfile         # Dockerfile for containerizing the application
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

### 3. Set Up the FastAPI Application
A basic FastAPI app is contained in `main.py` and routes are set up in`routes.py`.

### 4. Database Using SQLAlchemy
In `models.py` and `database.py`, SQLAlchemy manages the SQL database:

Azure Key Vault is used to fetch the DB connection string securely

### 5. Azure Blob Storage

To initialize Blob Service Client using the connection string from Key Vault, the `BlobServiceClient` will be used.
Files are updated to blob through the `update_file_to_blob` method, which takes as input: container name, file path and blob name.


### 6 Redis Cache

Redis client initializes with `StrictRedis`, which requires redis host address, port and password.
Cached data are retrieved by key, and are set using key, value and expiration.

### 7 Application containerization.
The Dockerfile uses the `python:3.9` docker image, and runs the app with `uvicorn`.

### Azure deployment details
1. **Azure Web Apps**: use the Azure CLI to deploy the containerized FastAPI app to Azure Web Apps.
2. **Azure Blob Storage**: ensure that container and permissions are properly configured in Azure.
3. **Key Vault**: use Azure Key Vault for managing secrets, ensuring secure access to sensitive information.
4. **Redis Cache**: integrate Redis using Azure Cache for Redis to cache frequently accessed data and reduce database load.

### Step 9: Optimize SQL Queries
- Use efficient queries with SQLAlchemy.
- Optimize indexing and query caching adoption.
- Profile and monitor the database performance using Azure Monitoring tools.
