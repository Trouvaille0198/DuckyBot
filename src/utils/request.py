from typing import Optional

from aiohttp import ClientSession

default_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}


async def get_text(url: str, params: Optional[dict] = None,
                   headers: dict = default_headers) -> str:
    async with ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as r:
            result = await r.text()
    return result


async def get_bytes(url: str, params: Optional[dict] = None,
                    headers: dict = default_headers) -> bytes:
    async with ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as r:
            result = await r.read()
    return result


# async def get_content(url: str, headers: dict = default_headers):
#     async with ClientSession() as session:
#         async with session.get(url, headers=headers) as r:
#             result = await r.content.read()
#     return result


async def post_bytes(
        url: str, params: Optional[dict] = None, json: Optional[dict] = None
) -> bytes:
    async with ClientSession() as session:
        async with session.post(url, params=params, json=json) as r:
            result = await r.read()
    return result
