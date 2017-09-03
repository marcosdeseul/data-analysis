from typing import List
import pandas as pd

SPECIFIC_DATE = "20170824"
TYPE_ARTICLE = "article"
TYPE_FOLLOWER = "follower"
TYPE_FOLLOWING = "following"
TYPE_MAGAZINE = "magazine"
TYPE_RELATED = "related"
WRITER_IMAGINEER = "imagineer"
DIR_DATA = "data"

def get_list_df_by_writers(writers:List[str], type_:str) -> pd.DataFrame:
    list_ = []
    for writer in writers:
        try:
            csv_ = pd.read_csv(f"{DIR_DATA}/{SPECIFIC_DATE}-{writer}-{type_}.csv", sep="\t")
            list_.append(csv_)
        except FileNotFoundError:
            print(f"{writer}-{type_} file does not exist")
    return pd.concat(list_)

def get_article_df_by_writers(writers:List[str]) -> pd.DataFrame:
    return get_list_df_by_writers(writers, TYPE_ARTICLE)

def get_follower_df_by_writers(writers:List[str]) -> pd.DataFrame:
    return get_list_df_by_writers(writers, TYPE_FOLLOWER)

def get_following_df_by_writers(writers:List[str]) -> pd.DataFrame:
    result = []
    for writer in writers:
        try:
            result.append(
                pd.read_csv(f"{DIR_DATA}/{SPECIFIC_DATE}-{writer}-{TYPE_FOLLOWING}.csv", 
                            sep="\t") )
        except:
            pass
    return pd.concat(result)

def parse_datetime(df:pd.DataFrame, fields:List[str]) -> None:
    for field in fields:
        df[field] = pd.to_datetime(df[field], format='%Y-%m-%d %H:%M:%S')

def read_related_data() -> pd.DataFrame:
    related_file_name = f"{DIR_DATA}/{SPECIFIC_DATE}-{WRITER_IMAGINEER}-{TYPE_RELATED}.csv"
    return pd.read_csv(related_file_name, sep="\t")
