from flask import Flask, request, Response
from datetime import datetime
import json

app = Flask(__name__)
@app.route("/api" )
def home():
    current_datetime = datetime.now()
    weekday = current_datetime.strftime('%A')
    formatted_time = current_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
    
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")

    data_set = {
        "slack_name": "fidelis Abanum",
        "current_day": weekday,
        "utc_time": formatted_time,
        "track": "backend",
        "github_file_url": "https://github.com/Fidelis-7/HNG_workspace/blob/main/app.py",
        "github_repo_url": "https://github.com/Fidelis-7/HNG_workspace.git",
        "status_code": 200
    }

    if slack_name:
        data_set["slack_name"] = slack_name

    if track:
        data_set["track"] = track

    # Define the desired order of keys
    key_order = [
        "slack_name",
        "current_day_of_the_week",
        "utc_time",
        "track",
        "github_file_url",
        "github_repo_url",
        "status_code"
    ]
    custom_json = json.dumps({key: data_set[key] for key in key_order}, indent=4)

 
    return Response(custom_json, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True, port=8080)