# from decouple import config

class Config:
    # Configuração do banco de dados principal
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://fernandes@joaopedrofer2003hotmail.onmicrosoft.com:Roy!03092023@proteon.database.windows.net:1433/e-commerce?"
        "driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=no&Connection+Timeout=30&Authentication=ActiveDirectoryPassword"
    )

    # Desabilitar o tracking de modificações do SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False