from database.connection import engine

try:
    with engine.connect() as conn:
        print("Conexão OK!")
except Exception as e:
    print(e)