from unittest.mock import patch
from summaryzer import return_article_summary_async
import pytest
from news import News


@pytest.mark.asyncio
async def test_return_article_summary():
    article_urls = ['http://testartcile1.com',
                    'http://testarticle2.com']
    with patch.object(News, 'get_news_urls',
                      return_value=article_urls):
        article_summary = 'This is a test summary'
        with patch('summaryzer.get_openAI_data_async',
                   return_value=article_summary):
            result = []
            async for summary in return_article_summary_async():
                result.append(summary)

            assert article_summary in result
