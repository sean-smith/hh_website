import requests

class generate():
    def __init__(self, file_location):
        self.file_location = file_location

    def get_json(self):

        doc = requests.get("https://raw.githubusercontent.com/HackathonHackers/hh-personal-sites/master/README.md").content
        doc = doc.split('\n')
        return self.get_json_online(doc)

        print "failed to load members"



    def get_json_online(self, text):
        lst = []
        for each in text:
            if each != "" and each[0]=="-":
                words = each.split()
                first = words[1]
                last = words[-2]
                url = words[-1]
                if url[0]=="w":
                    url = "http://"+url
                lst.append({"first": first, "last":last, "url":url })
                print first,last,url
        json = {"all_users": lst}
        return json





x = generate("README.md")
x.get_json()
