from datetime import datetime, timezone
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_items():
    return jsonify(
        {
            "slack_name": request.args.get("slack_name"),
            "current_day": datetime.now().strftime("%A"),
            "utc_time": datetime.now(timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            ),
            "track": request.args.get("track"),
            "github_file_url": "https://github.com/kengoon/hng_intern_endpoint/blob/master/app.py",
            "github_repo_url": "https://github.com/kengoon/hng_intern_endpoint",
            "status_code": 200
        }
    )


if __name__ == '__main__':
    app.run(debug=True)
