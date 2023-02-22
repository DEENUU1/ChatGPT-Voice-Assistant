import asyncio

from summaryzer import return_article_summary_async


async def main_async():
    async for summary in return_article_summary_async():
        print(summary)


if __name__ == '__main__':
    asyncio.run(main_async())
