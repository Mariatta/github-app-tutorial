Gigdethub
=========


Gidgethub is an async library in Python for working with GitHub APIs.

REST API calls
--------------

When you make API calls to GitHub, you need to provide API tokens and pass in
certain request headers. Gidgethub provides the abstraction for making such API
calls, as well as deciphering the request response.

Quick example of calling GitHub APIs using ``requests`` library.

::

    import requests
    # construct the request headers
    request_headers = {
        "User-Agent": "cool-octocat-app",
        "Authorization": "token abcde",
        "Accept": "application/vnd.github.v3+json"
    }
    # make an API call
    url = "https://api.github.com/repos/mariatta/gidgethub/strange-relationship/issues"
    response = requests.get(url, headers=request_headers)

With gidgethub::

    async with aiohttp.ClientSession() as session:
            gh = GitHubAPI(session,
                "cool-octocat-app",
                oauth_token="abcde"
            )
            response = await gh.getitem(
                '/repos/mariatta/strange-relationship/issues'
            )

We will go through more detailed examples in the
:ref:`GitHub API using Command Line <gh_api_command_line>` section.


Webhook Events
--------------

Gidgethub provides routings for receiving webhook events from GitHub. Each routings
allows for individual request handlers to be defined. We will cover this in detail
in the :ref:`Responding to Webhook Events <responding_to_webhook>` section.

Additionally, gidgethub takes care of verifying the webhook delivery headers,
and the webhook secret to help protect your webservice.

GitHub App
----------

Certain API endpoints for GitHub Apps require JWT instead of OAuth access token.
Since version 4.1, gidgethub comes several utilities to help with this. We will go further
in detail in the :ref:`Building a GitHub App <gh_app_setup>` section.

GitHub Actions
--------------

Since version 4.0, gidgethub provides support for working with
`GitHub Actions <https://gidgethub.readthedocs.io/en/latest/actions.html>`_.
We will not cover Actions in this tutorial.