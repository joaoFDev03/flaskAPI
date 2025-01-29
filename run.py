import os
from dotenv import load_dotenv
from app import create_app, db
from app.models.user import User
import pyodbc
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializar a aplicação Flask
app = create_app()

# Detalhes da conexão com o Azure SQL Database
server = os.getenv('AZURE_SQL_SERVER')
database = os.getenv('AZURE_SQL_DATABASE')
driver = os.getenv('AZURE_SQL_DRIVER', '{ODBC Driver 18 for SQL Server}')
username = os.getenv('AZURE_SQL_USERNAME')
password = os.getenv('AZURE_SQL_PASSWORD')

# String de conexão para o Azure SQL Server
AZURE_SQL_CONNECTIONSTRING = (
    f"Driver={driver};Server={server};Database={database};"
    f"Uid={username};Pwd={password};Encrypt=yes;"
    "TrustServerCertificate=no;Connection Timeout=30;"
    "Authentication=ActiveDirectoryPassword"
)
app.config['JWT_SECRET_KEY'] = '123'
# Testar a conexão com o banco de dados
try:
    with pyodbc.connect(AZURE_SQL_CONNECTIONSTRING) as conn:
        print("Conexão estabelecida com sucesso!")
except pyodbc.Error as e:
    print(f"Erro na conexão: {e}")

# Iniciar o servidor Flask
if __name__ == "__main__":
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')