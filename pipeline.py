import config
from openai import OpenAI
from gdeltdoc import GdeltDoc, Filters
from newspaper import Article
from prompt_template import prompt


OPENAI_API_KEY = config.OPENAI_API_KEY
openai_client = OpenAI(api_key=OPENAI_API_KEY)
model = "gpt-4o-mini"
gd = GdeltDoc()

def chatgpt_generate(query):
    messages = [{
        "role": "system",
        "content": "You are a helpful assistant."},
        {
            "role": "system",
            "content": query
        }]
    response = openai_client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content
    return answer
    
def get_url(keyword):
    f = Filters(
        keyword = "Microsoft",
        start_date = "2024-05-01",
        end_date = "2024-05-25",
        num_records = 10,
        domain = "nytimes.com",
        country = "US"
        )
    articles = gd.article_search(f)
    return articles

def get_article(df):
    urls = df["url"]
    titles = df["title"]
    texts = []

    for url in urls:
        article = Article(url)
        article.download()
        article.parse()
        texts.append(article.text)
    return texts, titles

#print(prompt)
articles = get_url("Microsoft")
texts, titles = get_article(articles)
answer = chatgpt_generate(prompt + texts[0])
print(answer)
#print(articles)
#print(texts[0], titles[0])