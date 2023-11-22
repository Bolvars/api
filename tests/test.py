from dl.detect_lang import detect_lang
from datetime import datetime

def testTime(func):
    start = datetime.now()
    def wrapper():
        return func
    word = wrapper()
    print(word)
    return (datetime.now() - start).microseconds


def detect(word:str): 
    a = DetectLanguage('шалбар')
    res = a.detect_language()
    return res


print([1,2,3,4,5])
print(detect())

