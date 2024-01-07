
import requests
from datetime import datetime
import time
from bs4 import BeautifulSoup
import pandas as pd
from transformers import pipeline, AutoTokenizer
from transform import transform_data,task_data_upload
import sys


def extract_data():
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained("/Users/niyantmehta/Spiced/final/tokenizer")
    gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}
    pipe = pipeline("summarization", model="/Users/niyantmehta/Spiced/final/pegasus-cnn-model", tokenizer=tokenizer)

    url = 'https://content.guardianapis.com/search?'

    # Set to store the unique article URLs
    fetched_urls = set()

    #while True:
        #try:
    # Create request parameters
    params = {
        'api-key': 'eedb86d3-6032-4525-8b4b-9f1da086f675',
        'q' : 'news',
        'order-by': 'newest',
        'page-size': 1
    }

    # Make the request
    response = requests.get(url, params=params)
    data = response.json()

    # Check if new articles are available
    if data['response']['status'] == 'ok' and data['response']['total'] > 0:
        # Iterate over the fetched articles
        for article in data['response']['results']:
            # Extract the article details
            article_id = article['id']
            article_url = article['webUrl']

            # Check if the article has already been fetched
            if article_url not in fetched_urls:
                fetched_urls.add(article_url)

                # Extract the article information
                timestamp = datetime.strptime(article['webPublicationDate'], '%Y-%m-%dT%H:%M:%SZ')
                section = article['sectionName']
                title = article['webTitle']

                # Get the article text
                response_html = requests.get(article_url)
                text_data = response_html.text
                soup = BeautifulSoup(text_data, 'html.parser')
                article_text = ''

                # Find relevant paragraphs within the article's HTML structure
                paragraphs = soup.find_all('p')
                for paragraph in paragraphs:
                    # Skip any paragraphs with class names indicating non-article content
                    if 'advert' not in paragraph.get('class', []):
                        article_text += paragraph.get_text() + ' '

                summary = pipe(article_text[:1024], **gen_kwargs)[0]["summary_text"]

                # Create a dataframe with the article information
                df = pd.DataFrame({'date': [timestamp], 'section': [section], 'title': [title], 'url':[article_url], 'summary':summary})

                # Print or do something with the fetched article
                print(df)
                #conn = pg.connect()
                #df.to_sql('news_etl', con=conn, if_exists='append', index=False)
                
                # Create a dataframe with the article information
                #df = pd.DataFrame({'Date': [timestamp], 'Section': [section], 'Title': [title], 'Article': [article_text], 'Summary':summary})

                #transform_data(df)
                #print(df)

#extract_data()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "extract_data":
        extract_data()




