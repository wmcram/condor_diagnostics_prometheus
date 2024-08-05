from flask import Flask, Response
app = Flask("metric_sevrer")

@app.route("/", methods=["GET"])
def home():
    return "ALIVE"

@app.route("/metrics", methods=["GET"])
def getfile():
    with open("metrics.prom", "r") as f:
        return Response(f.read(), mimetype="text/plain")
    
if __name__ == '__main__':
    app.run(host='localhost')