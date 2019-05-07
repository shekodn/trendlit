import urllib.request, json

titles_of_pulls = []

def get_pulls(page):
    repo = "https://api.github.com/repos/anakarenbm/trendlit/pulls?state=all&page=" + str(page)

    with urllib.request.urlopen(repo) as url:
        data = json.loads(url.read().decode())
        if len(data) > 0:
            for i in range(len(data)):
                # print(data[i]['title'])
                pull_title = data[i]['title']
                titles_of_pulls.append(pull_title)

        return len(data)

counter = 1
number_of_pulls = 1

while (number_of_pulls != 0 or couner == 8):
    number_of_pulls = get_pulls(counter)
    counter = counter + 1

titles_of_pulls.reverse()
filename = "docs/working_log.txt"

with open(filename, 'w') as out:
    for pull_title in titles_of_pulls:
        out.write(pull_title)
        out.write('\n')
