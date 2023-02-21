
from news import News


def main():
    news = News()
    for summary in news.summary():
        yield summary



if __name__ == '__main__':
    for i in main():
        print(i)