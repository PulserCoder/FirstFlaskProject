from flask import Flask
import utils

app = Flask(__name__)


@app.route('/')
def main_route():
    html = ''
    candidates_list = utils.load_candidates()
    for candidat in candidates_list:
        html += f'<pre><b>{candidat["name"]}</b> - {candidat["position"]} - {candidat["skills"]}</pre>'
    html += '<h3><a href="http://127.0.0.1:5000/help">Help page</a></h3>'
    return html


@app.route('/candidates/<int:x>')
def candidat(x):
    result, candidat = utils.get_by_pk(x)
    if result:
        html = f'<img src="{candidat["picture"]}"><h1><pre><b>{candidat["name"]}</b></pre></h1><h2><pre>{candidat["position"]}</pre></h2><em><pre>{candidat["skills"]}</pre></em>'
        html += '<h3><a href="http://127.0.0.1:5000/">Main page (BACK)</a></h3>'
        return html
    return candidat


@app.route('/skills/<x>')
def skill(x):
    ll = utils.get_by_skill(x)
    html = ''
    for candidat in ll:
        html += f'<h1><pre><b>{candidat["name"]}</b></pre></h1><h2><pre>{candidat["position"]}</pre></h2><em><pre>{candidat["skills"]}</pre></em>'
    html += '<h3><a href="http://127.0.0.1:5000/help">Main page (BACK)</a></h3>'
    return html

@app.route('/help')
def help():
    return open('help_page.html')


if __name__ == '__main__':
    app.run()