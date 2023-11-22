from googletrans import Translator as GoogleTranslator
from translate import Translator as TranslateTranslator
from translators import translate_text

from datetime import datetime
import requests
from pydantic import BaseModel
import pandas as pd
import json

class YandexAPI(BaseModel):
    text:str
    detectedLanguageCode:str

class YandexAPItranslate(BaseModel):
    translations: list[YandexAPI]



class TranslateWordWithLibs:

    def __init__(self,word:str, language:str = 'ru') -> None:
        self.word = word
        self.language = language
        self.full_translation_dict = [
            "niutrans","myMemory","alibaba",
            "baidu", "modernMt","volcEngine",
            "iciba","iflytek","google","bing",
            "lingvanex","itranslate"
            ]

        ##self.dF = pd.DataFrame()

    def transalate_with_translators(self) -> dict[str,tuple]:
        d = {}
        for translator in self.full_translation_dict:
            start = datetime.now()
            try:
                translate_word = translate_text(self.word, translator=translator, from_language='auto', to_language=self.language)
                final_time = datetime.now() - start
                d[translator] = (translate_word,final_time.microseconds)
            except Exception as e:
                d[translator] = (f'error {type(e)}',0)
            
        return d
            
    def translate_word_lib_yandex(self) -> str:
        IAM_TOKEN = "t1.9euelZrOlM6LjZHJnZaei5HHyceJlu3rnpWayZSUic6OmpaQjZXMnMabkM_l8_d9c0dV-e95IGZD_t3z9z0iRVX573kgZkP-zef1656VmpuQlpWZj8uZkI7Hnc6XicyO7_zF656VmpuQlpWZj8uZkI7Hnc6XicyO.eKaqBCrOZQVxde9-FI_Dylor-6SqtMBzPxTAAf1BEDckoUBoOKCNP_fc4VbGJhghPQZKeuPVzv5nbaUxe8RyAA"
        folder_id = "b1g3f0mtv1k8hb6phip7"
        words = self.word.split(' ')
        print(words)

        body = {
            "targetLanguageCode": self.language,
            "texts": self.word,
            "folderId": folder_id,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {IAM_TOKEN}"
        }

        response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
            json = body,
            headers = headers
        )
        
        result = YandexAPItranslate.parse_raw(response.text)
        
        return result.translations[0].text

    def translate_word_lib_niutrans(self):
        url = 'http://api.niutrans.com/NiuTransServer/translation?'

        data = {"from": 'auto', 
                "to": self.language, 
                "apikey": "eefca1e99ced7527d1769c02a36ef687", 
                "src_text": self.word}
        
        response = requests.get(url,params=data)
        return response.text

    def translate_word_lib_google(self) -> str:
        translator = GoogleTranslator()
        translated = translator.translate(self.word, dest=self.language)
        
        return translated.text
    
    def translate_word_lib_MyMemory(self) -> str:
        
        url = "https://api.mymemory.translated.net/get?q=Привет, мир!&langpair=en|it"
        api_key = "836ab8ba5705319710a1"
        params = {"q": self.word,
                   "langpair": f" autodetected|{self.language}"}

        response = requests.get(url, params=params)
        response_json = response.json()
        return response_json

    def translate_word_lib_translate(self) -> str:
        translator = TranslateTranslator(to_lang=self.language)
        translated = translator.translate(self.word)
        return translated
