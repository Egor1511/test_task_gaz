from typing import List, Any

from pydantic import BaseModel


class BankAPIResponse(BaseModel):
    Columns: List[str]
    Description: str
    RowCount: int
    Rows: List[List[Any]]
