from gdeltdoc import GdeltDoc, Filters
from newspaper import Article

f = Filters(

    keyword = "Microsoft",
    start_date = "2024-05-01",
    end_date = "2024-05-25",
    num_records = 10,
    domain = "nytimes.com",
    country = "US"
)

gd = GdeltDoc()

# Search for articles matching the filters
articles = gd.article_search(f)

#print(articles)
# Get a timeline of the number of articles matching the filters
timeline = gd.timeline_search("timelinevol", f)

url = articles.loc[1, "url"]
print(articles.loc[1, "title"])
print("--------------------------")

# Article 객체 생성 및 다운로드
article = Article(url)
article.download()
article.parse()

# 기사 정보 출력
print(f'제목: {article.title}')
print(f'저자: {article.authors}')
print(f'발행일: {article.publish_date}')
print(f'본문: {article.text[:500]}...')  # 본문 일부 출력
