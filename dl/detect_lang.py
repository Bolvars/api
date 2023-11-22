import fasttext 
import os
import pandas as pd
import pycld2 as cld2 
from abc import ABC, abstractmethod

class DetectLanguage(ABC):
    @abstractmethod
    def __init__(self):
        ...
    
    @abstractmethod
    def detect_language(self):
        ...

class DetectLanguageFastText(DetectLanguage):
    _instance = None

    def __new__(cls, *args, **kwargs):

        if cls._instance is None: 
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        self._model = fasttext.load_model('models/lid.176.bin')



    def detect_language(self, word:str):
        try:
            predict = self._model.predict(word, k = 1)
        except:
            print(word)
            return 'None_0.0'
        #print(predict)
        detected_language = predict[0][0].split('__')[-1] # __label__ 
        #print(sum(predict[1]))
        return f'{detected_language}_{predict[1][0]}'
    

class DetectLanguageCLD2(DetectLanguage):

    def __init__(self):
        self.isReliable = None
        self.textBytesFound = None
        self.details = None 
        self.vectors = None

    def detect_language(self,word):
        self.isReliable, self.textBytesFound, self.details = cld2.detect(word)
        return cld2.detect(word)


def create_DS(model_cls:DetectLanguage):

    model = model_cls 

    def detect(word:str): 
        res = model.detect_language(word)
        return res



    directory_path = '..\\translate_datasets\\main_ds'

    files = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path,file))]

    for nameDF in files: 
        nameLang = nameDF.split('-')[0] + '_lang'
        print(nameLang)
        dfFastText = pd.DataFrame()
        df = pd.read_csv(os.path.join(directory_path,nameDF),sep='\t')
        df['sentence'] = df['sentence'].apply(detect)
        dfFastText[nameLang], dfFastText['probability'] = df['sentence'].apply(lambda word: word.split('_')[0]), df['sentence'].apply(lambda word: word.split('_')[1])
        dfFastText.to_csv(f"FastDetect_DS\\FastText_Detect_Language-{nameLang}.tsv", sep = '\t', index=False)
    
#df_ft_kk = pd.read_csv('FastDetect_DS\\FastText_Detect_Language-kz_rus_symb_lang.tsv',sep='\t')
#print(len(df_ft_kk['kz_rus_symb_lang'].iloc[1]))
#kk_value =df_ft_kk[(df_ft_kk['kz_rus_symb_lang'] != 'ru')] 
#print(len(kk_value)/len(df_ft_kk))

a = DetectLanguageCLD2()
print(a.detect_language("Жоқ, мен"))
print(os.listdir("C:\\Program Files\\DEV\\vcpkg\\installed\\x64-windows"))