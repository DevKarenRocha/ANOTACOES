import cx_Oracle

# Configurar a conexão
dsn = cx_Oracle.makedsn("HOST", "1521", service_name="SERVICE_NAME")
conexao = cx_Oracle.connect(user="USUARIO", password="SENHA", dsn=dsn)

print("Conexão bem-sucedida!")

# Fechar conexão
conexao.close()
