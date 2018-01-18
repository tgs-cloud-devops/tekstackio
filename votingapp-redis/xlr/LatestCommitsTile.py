import json
from xlrelease.HttpRequest import HttpRequest

if accessToken is not None and accessToken.strip() == "":
    accessToken = None

url = "/repos/%s/commits?sha=%s%s" % \
    (repositoryId, branch, "&access_token=" + accessToken if accessToken else "")

print "Querying commits from GitHub API by URL %s" % url

request = HttpRequest({"url": "https://api.github.com"})
response = request.get(url, contentType='application/json')

if response.status != 200:
    raise Exception("Request to GitHub failed with status %s, response %s" % (response.status, response.response))

commits = json.loads(response.response)

data = {
    "commits": commits
}
