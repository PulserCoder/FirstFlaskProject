import json


def load_candidates():
    return json.load(open('candidates.json', 'r', encoding='utf8'))


def get_all():
    return [i['name'] for i in load_candidates()]


def get_by_pk(pk):
    try:
        return True, [i for i in load_candidates() if i['pk'] == pk][0]
    except:
        url = 'https://n1s1.elle.ru/48/7b/36/487b36300c62c5f0cb905da52aa874b4/728x486_1_30b570c2f6c0da65bb56095068e05768@940x627_0xc0a839a4_18087198581488362059.jpeg'
        return False, f'<h1>Такого юзера не существует</h1><img src="{url}"><h3><a href="http://127.0.0.1:5000/">Main page (BACK)</a></h3>'



def get_by_skill(skill_name):
    return [name for name in filter(lambda x: skill_name.lower() in x['skills'].lower(), load_candidates())]
