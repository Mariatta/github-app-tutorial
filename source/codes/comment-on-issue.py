import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "mariatta", oauth_token=os.getenv("GH_AUTH"))
        response = await gh.post(
            "/repos/mariatta/strange-relationship/issues/276/comments",
            data={"body": "Use more emoji!",},
        )
        print(f"Commented on the issue!")


asyncio.run(main())
