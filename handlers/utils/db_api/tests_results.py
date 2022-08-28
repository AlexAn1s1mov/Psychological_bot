from asyncpg import UniqueViolationError

from handlers.utils.db_api.schemas.results import Results


async def new_result(id: int, user_id: int, test_number: str, test_name: str, results: str, status: str):
    try:
        result = Results(id=id, user_id=user_id, test_number=test_number, test_name=test_name, results=results, status=status)
        await result.create()
    except UniqueViolationError:
        print('Результат не добавлен или обновлён')

async def select_result():
    result = await Results.query.where(Results.status == 'created').gino.first()
    return result

async def select_result_by_user_id(id: int):
    result = await Results.query.where(Results.id == id).gino.first()
    return result

async def update_result(id, results):
    result = await select_result_by_user_id(id)
    await result.update(results=results).apply()

