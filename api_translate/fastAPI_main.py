from .translate_words import TranslateWordWithLibs
from fastapi import FastAPI
import uvicorn 
from pydantic import BaseModel

app = FastAPI()



class TranslatedWord(BaseModel):
    word:str

@app.get("/catalog/0/google_translate/{word}")
async def translate_google(word:str) -> str:

    if word.isdigit():
        return word

    res = TranslateWordWithLibs(word)
    return res.translate_word_lib_google()

@app.get("/catalog/0/translate/{word}")
async def translate(word:str) -> str:

    if word.isdigit():
        return word

    res = TranslateWordWithLibs(word)
    return res.translate_word_lib_translate()

@app.get("/catalog/0/yandex/{word}")
async def translate_yandex(word:str):

    if word.isdigit():
        return word

    res = TranslateWordWithLibs(word)
    return res.translate_word_lib_yandex()

@app.get("/catalog/0/translators/{word}")
async def translate_with_all_translators(word:str) -> dict[str,tuple]:

    if word.isdigit():
        return word

    res = TranslateWordWithLibs(word)
    return res.transalate_with_translators()

@app.get("/catalog/0/niutrans/{word}")
async def translate_niutrans(word:str):

    if word.isdigit():
        return word

    res = TranslateWordWithLibs(word)
    return res.translate_word_lib_niutrans()

@app.get("/catalog/0/myMemory/{word}")
async def translate_myMemory(word:str):

    if word.isdigit():
        return word

    res = TranslateWordWithLibs(word)
    return res.translate_word_lib_MyMemory()


def start():
    uvicorn.run("api_translate.fastAPI_main:app", host="192.168.0.11", port=8000, reload=True)
    