import json
import requests

url = 'http://upload.itcollege.ee/~aleksei/eksam.json'

def parse_json(url):
    
    file_content = json.loads(requests.get(url).text)
    for course in file_content['courses']:
        if 'Scripting languages' in course.values():
            return course['code']
