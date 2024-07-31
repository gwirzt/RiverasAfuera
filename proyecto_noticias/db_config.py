DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'riverasAfuera',
        'USER': 'sa',
        'PASSWORD': 'Nacion1846',
        'HOST': '192.168.0.3',
        'PORT': '',  # Usualmente el puerto predeterminado es 1433, puedes dejarlo vacío
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
