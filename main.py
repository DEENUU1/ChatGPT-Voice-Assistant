from openAI import get_openAI_data
from news import News


def main():
    news = News()
    article_text = news.get_html_text()
    return get_openAI_data(article_text)


if __name__ == '__main__':
    print(main())