from sqlalchemy import Column, BigInteger, String, sql

from handlers.utils.db_api.db_TelegramBot import TimedBaseModel


class Results(TimedBaseModel):
    __tablename__ = 'results'
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger)
    test_number = Column(String(50))
    test_name = Column(String(200))
    results = Column(String(4000))
    status = Column(String(30))

    query: sql.select