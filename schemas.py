from pydantic import BaseModel
from typing import Optional


class Text_data(BaseModel):
    text: str
    num_words: Optional[int] = None
    num_sentences: Optional[int] = None
    num_characters: Optional[int] = None
