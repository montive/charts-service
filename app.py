import io
import requests
from flask import Response
from flask_cors import CORS
from charts import bar_chart, table
from flask import Flask, jsonify, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)
CORS(app)

RANKINGS_MS_URL = "http://0.0.0.0:5002"
QS_RANKING_ENDPOINT = "get_qs_ranking"

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/get_ranking/<string:name>", methods=["GET"])
def get_ranking(name):
    if name == "qs":
        year = request.args.get("year", "")
        limit = request.args.get("limit", "")
        response = requests.get(f"{RANKINGS_MS_URL}/{QS_RANKING_ENDPOINT}?year={year}&limit={limit}")
        print(jsonify(response.json()))
        return jsonify(response.json())


@app.route("/get_bar_chart", methods=["GET"])
def get_bar_chart():
    year = request.args.get("year", "")
    limit = request.args.get("limit", "")
    group_by = request.args.get("groupBy", "")

    response = requests.get(f"{RANKINGS_MS_URL}/{QS_RANKING_ENDPOINT}?year={year}&limit={limit}&group_by={group_by}")
    chart = bar_chart(response.json())
    output = io.BytesIO()
    FigureCanvas(chart).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route("/get_top_10_table")
def get_top_10_table():
    year = request.args.get("year", "")
    limit = request.args.get("limit", "10")
    response = requests.get(f"{RANKINGS_MS_URL}/{QS_RANKING_ENDPOINT}?year={year}&limit={limit}")
    chart = table(response.json())
    output = io.BytesIO()
    FigureCanvas(chart).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001,debug=True)
