prompt = """다음에 오는 텍스트에서 S&P500에 상장된 기업명을 모두 추출하고, 기업에 해당하는 감성을 분석하시오. 
각 감성에 스코어링을 하시오. 각 스코어의 합은 1이 되어야 합니다. 소수점 첫째자리까지 표기하시오. 출력포맷은 리스트이며, 
세부 내용은 다음과 같습니다. 반드시 출력포맷만을 생성하고, 다른 텍스트는 생성하지 마시오. 
[{"organization": <기업명>, "positive": 0~1, "negative": 0~1, "neutral": 0~1}, …] 뉴스: """