from os import path
import csv

from flask import Flask, abort, render_template

# Data from https://data.seattle.gov/Public-Safety/Seattle-Real-Time-Fire-911-Calls/kzjm-xkqj

app = Flask(__name__)

def get_csv():
    csv_path = path.join('static', 'data.csv')
    with open(csv_path, newline='') as csv_file:
        csv_obj = csv.DictReader(csv_file)
        return list(csv_obj)

@app.route('/')
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

@app.route('/<row_index>/')
def detail(row_index):
    template = 'detail.html'
    object_list = get_csv()
    try:
        row_index = int(row_index)
        assert(object_list[row_index])
    except:
        abort(404)
    return render_template(template, obj=object_list[row_index])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
