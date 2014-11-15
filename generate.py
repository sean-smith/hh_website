import requests, json, os

class generate():
    def __init__(self, file_location):
        self.file_location = file_location

    def get_json(self):
        doc = open("json.txt", "r")
        #doc = json.load(doc)
        #print(str(doc))
        for line in file:
            dict = line
        print(type(dict))
        return doc


    def get_data(self):
        doc = requests.get("https://raw.githubusercontent.com/HackathonHackers/hh-personal-sites/master/README.md").content
        doc = doc.split('\n')
        json = self.get_json_online(doc)
        os.remove("json.txt")
        f = open("json.txt", "w")
        f.write(str(json))

    def get_json_online(self, text):
        lst = []
        for each in text:
            if each != "" and each[0]=="-":
                words = each.split()
                first = words[1]
                last = words[-2]
                url = words[-1]
                image_url = self.get_picture_url(url)
                if image_url != 0:
                    lst.append({"first": first, "last":last, "url":url, "image_url": image_url})
                else:
                    lst.append({"first": first, "last":last, "url":url, "image_url": "http://images.puella-magi.net/thumb/2/27/No_Image_Wide.svg/800px-No_Image_Wide.svg.png?20110202071158"})
                print first,last,url,image_url
        json = {"all_users": lst}
        return json

    def get_picture_url(self,url):
        try:
            data = {"access_token": "CAACEdEose0cBAEUBMSNiFO6xyxcFoq63haUCM0eZB3iqIAjeIQcygNZCKJIEWleXKAFyKauNjaapGwqgC5tPwyRROjyMZAUUdoi22XH5aMvk3B3qWGlmSZB64qvne43Lfc2MbdMk1xvlONlYYies6xenlvZCxP1pCqcYADpUfhYZBWMhszIZAZCDWrCtDqZArCc2PtPaM5nWGKZAxgYqQnYqZA7pZBBoEaseugAZD", "scrape":"true"}
            r = requests.get("https://graph.facebook.com/v2.2/?id="+url, params=data)
            id = r.json()["og_object"]["id"]
            r = requests.get("https://graph.facebook.com/"+id)
            images = r.json()["image"]
            url = images[0]["url"]
            return url
        except:
            return 0



x = generate("README.md")
#x.get_data()
x.get_json()
