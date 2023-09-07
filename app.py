from datetime import datetime, timezone
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_items():
    data = [request.args.get("slack_name"), request.args.get("track")]
    current_day = datetime.now().strftime("%A")
    return jsonify(
        {
            "slack_name": request.args.get("slack_name"),
            "current_day": datetime.now().strftime("%A"),
            "utc_time": datetime.now(timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            ),
            "track": request.args.get("track"),
            "status_code": 200
        }
    )


if __name__ == '__main__':
    app.run(debug=True)
