import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "mariatta", oauth_token=os.getenv("GH_AUTH"))
        response = await gh.patch(
            "/repos/mariatta/strange-relationship/issues/28", data={"state": "closed",}
        )
        print(f"Issue closed")


asyncio.run(main())
