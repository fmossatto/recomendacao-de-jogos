from sqlalchemy import create_engine

from database.connection import DATABASE_URL

from analysis.services.exploratory_service import (
    ExploratoryService
)

engine = create_engine(
    DATABASE_URL
)

ExploratoryService.generate_report(
    engine
)

print("Relatório gerado com sucesso.")