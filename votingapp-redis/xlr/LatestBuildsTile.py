import json
import urllib2
separator = "%2F"
url = 'https://api.travis-ci.org/repo/%s%s%s/builds?branch.name=master' % (repositoryOwner, separator, repositoryName)

headers = {}
headers['Content-Type'] = "application/json"
headers['Accept'] = "application/json"
headers['Travis-API-Version'] = 3
headers['Authorization'] = "token XXXXXXXXXXXXXXXX"

req = urllib2.Request(url, headers = headers)
resp = urllib2.urlopen(req)
respData = resp.read()

builds = json.loads(respData)

data = {
    "builds": builds
}
