"""
============================================ №6*
Имеется банковское API возвращающее JSON
{
	"Columns": ["key1", "key2", "key3"],
	"Description": "Банковское API каких-то важных документов",
	"RowCount": 2,
	"Rows": [
		["value1", "value2", "value3"],
		["value4", "value5", "value6"]
	]
}
Основной интерес представляют значения полей "Columns" и "Rows",
которые соответственно являются списком названий столбцов и значениями столбцов

Задание:
	1. Получить JSON из внешнего API
		ендпоинт: GET https://api.gazprombank.ru/very/important/docs?documents_date={"начало дня сегодня в виде таймстемп"}
	2. Валидировать входящий JSON используя модель pydantic
		(из ТЗ известно что поле "key1" имеет тип int, "key2"(datetime), "key3"(str))
	2. Представить данные "Columns" и "Rows" в виде плоского csv-подобного pandas.DataFrame
	3. В полученном DataFrame произвести переименование полей по след. маппингу
		"key1" -> "document_id", "key2" -> "document_dt", "key3" -> "document_name"
	3. Полученный DataFrame обогатить доп. столбцом:
		"load_dt" -> значение "сейчас"(датавремя)
"""

from bank_api import get_bank_data
from data_models import BankAPIResponse
from data_processing import json_to_dataframe, add_load_datetime_column

api_url = r'https://api.gazprombank.ru/very/important/docs'

json_data = get_bank_data(api_url)

try:
    validated_data = BankAPIResponse(**json_data)
    print("The data has been successfully validated")
except Exception as e:
    print("Data validation failed:", e)
    exit()

column_mapping = {"key1": "document_id", "key2": "document_dt",
                  "key3": "document_name"}

df = json_to_dataframe(validated_data.dict(), column_mapping)

df = add_load_datetime_column(df)

print(df)
