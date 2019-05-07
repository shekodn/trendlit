import urllib.request, json
import datetime
import dateutil.parser


class PullRequest:
    def __init__(self):
        self.merged_at = None
        self.body = None
        self.title = None


d = dateutil.parser.parse("2008-09-26T01:51:42.000Z")
print(d.strftime("%m/%d/%Y"))  # ==> '09/26/2008'


titles_of_pulls = []
time_of_pulls = []


def pretty_time(ugly_time_format):
    """
    Description: converts YYYY-MM-DDTHH:mm:ss.000Z time format to MM/DD/YYYY time
    format
    """
    try:
        d = dateutil.parser.parse(ugly_time_format)
        return d.strftime("%d/%m/%Y")
    except:
        return "Null"


def get_pulls(page):
    repo = (
        "https://api.github.com/repos/anakarenbm/trendlit/pulls?state=all&page="
        + str(page)
    )

    aux_pr = PullRequest()

    with urllib.request.urlopen(repo) as url:
        data = json.loads(url.read().decode())
        if len(data) > 0:
            for i in range(len(data)):
                # print(data[i]['title'])
                aux_pr.title = data[i]["title"]
                aux_pr.body = data[i]["body"]
                formatted_time = pretty_time(data[i]["merged_at"])
                aux_pr.merged_at = formatted_time
                if aux_pr.body is "":
                    print(aux_pr.title)
                    print(aux_pr.merged_at + "\n")
                else:
                    print(aux_pr.title)
                    print(aux_pr.merged_at)
                    print(aux_pr.body + "\n")


get_pulls(1)
get_pulls(2)
get_pulls(3)
get_pulls(4)


# counter = 1
# number_of_pulls = 1
#
# while (number_of_pulls != 0 or couner == 8):
#     number_of_pulls = get_pulls(counter)
#     counter = counter + 1


# titles_of_pulls.reverse()
# filename = "docs/working_log.txt"
#
# with open(filename, 'w') as out:
#     for pull_title in titles_of_pulls:
#         out.write(pull_title)
#         out.write('\n')
