import pandas as pd

def kz_to_ru_with_ru_symbols(df_kz_ru:pd.DataFrame) -> pd.DataFrame:
    
    def to_rus_symbols(sentence:str):
        d_symbols =  {
            'ұ' : 'у',
            'ң' : 'н',
            'ғ' : 'г',
            'ө' : 'о',
            'қ' : 'к',
            'ү' : 'у',
            'ә' : 'а',
            'і' : 'и',
            }
        to_rus_symbols_sentence = ''.join(d_symbols.get(c.lower(), c) for c in sentence)
        return to_rus_symbols_sentence
    
    df_result = df_kz_ru.copy()
    df_result['sentence'] = df_result['sentence'].apply(to_rus_symbols)

    return df_result


dF_kz_rus = pd.read_csv("main_ds/kz-rus.tsv",sep='\t')

new_df = kz_to_ru_with_ru_symbols(dF_kz_rus)
new_df.to_csv("main_ds/kz_rus_symb-rus.tsv", sep = '\t', index=False)
print(new_df.head())
