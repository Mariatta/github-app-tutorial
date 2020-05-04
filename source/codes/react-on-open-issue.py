import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "mariatta", oauth_token=os.getenv("GH_AUTH"))
        response = await gh.post(
            "/repos/mariatta/strange-relationship/issues/276/reactions",
            data={"content": "heart"},
            accept="application/vnd.github.squirrel-girl-preview+json",
        )
        print(f"Reacted on the issue!")


asyncio.run(main())
