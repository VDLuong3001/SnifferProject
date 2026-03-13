from flask import Flask, jsonify
from flask_cors import CORS
import threading

from sniffer import start_sniffer
from database import packets_collection

app = Flask(__name__)
CORS(app)

@app.route("/packets")
def get_packets():

    packets = list(packets_collection.find().limit(50))

    for p in packets:
        p["_id"] = str(p["_id"])

    return jsonify(packets)

if __name__ == "__main__":

    # start packet sniffer in background
    thread = threading.Thread(target=start_sniffer)
    thread.daemon = True
    thread.start()

    app.run(port=5000, debug=True)