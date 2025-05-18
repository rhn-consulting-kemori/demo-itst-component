# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)
report_viewer_url = os.getenv('REPORT_VIEWER_URL', '')
aap_url = os.getenv('AAP_URL', '')
openshift_url = os.getenv('OPENSHIFT_URL', '')
aap_api_url = os.getenv('AAP_API_URL', '')
aap_token = os.getenv('AAP_TOKEN', '')

# Root
@app.route("/")
def index():
    return render_template('index.html', report_viewer_url=report_viewer_url, aap_url=aap_url, openshift_url=openshift_url)

@app.route("/start", methods=['POST'])
def start():
    if request.form["test_id"] == "":
        return render_template('start.html', report_viewer_url=report_viewer_url, aap_url=aap_url, openshift_url=openshift_url, test_id="", start_result="テストIDが設定されていません。")
    else:
        # test_id
        test_id = request.form["test_id"]

        # request body
        data = {
            'extra_vars': {
                'test_id': test_id
            }
        }

        # API-Call Ansible WorkFlowJob
        response = requests.post(
            aap_api_url,
            json=data,
            headers = {'Authorization': 'Bearer {}'.format(aap_token)}
        )

        print(response.status_code)
        print(response.json())  

        # Response
        if response.status_code == 201:
            return render_template('start.html', report_viewer_url=report_viewer_url, aap_url=aap_url, openshift_url=openshift_url, test_id=test_id, start_result="シナリオテスト開始しました。")
        else:
            return render_template('start.html', report_viewer_url=report_viewer_url, aap_url=aap_url, openshift_url=openshift_url, test_id=test_id, start_result="シナリオテスト実行に失敗しました。")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090, debug=True)
