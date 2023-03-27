import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import bq_helper 
from bq_helper import BigQueryHelper
from rake_nltk import Rake

# keywords = rake.apply(full_text)
# print(keywords[:10])

bq_assistant = BigQueryHelper("bigquery-public-data", "stackoverflow")

QUERY = "SELECT title, body FROM bigquery-public-data.stackoverflow.posts_questions"
rows = bq_assistant.query_to_pandas(QUERY)

#rows = bq_assistant.head('posts_questions', 10)
#list(rows.iterrows())
def mapFunc(row):
    titleRake = Rake()
    fullRake = Rake()
    fullText = (row[1]['title'] + ", " + row[1]['body']).replace("<p>", "").replace("</p>", "")
    titleRake.extract_keywords_from_text(row[1]['title'])
    fullRake.extract_keywords_from_text(fullText)
    return {'title': titleRake.get_ranked_phrases(), "full": fullRake.get_ranked_phrases()}
keywords = list(map(mapFunc, rows.iterrows()))

