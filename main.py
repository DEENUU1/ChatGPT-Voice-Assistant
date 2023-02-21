import summaryzer

def main():
    for summary in summaryzer.return_article_summary():
        yield summary



if __name__ == '__main__':
    for i in main():
        print(i)