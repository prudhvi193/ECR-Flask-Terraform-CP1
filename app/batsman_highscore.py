import os
import boto3

from flask import Flask, jsonify, request

app = Flask(__name__)
client = boto3.client('dynamodb', region_name='us-east-1')
dynamoTableName = 'cricketersTable'

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/v1/bestscore/2010s/<string:batsman>")
def get_batsman(batsman):
    resp1 = client.get_item(
        TableName = dynamoTableName,
        Key={
            'batsman' : { 'S' : batsman}
        }
    )
    item = resp1.get('Item')
    if not item:
        return jsonify({'error': 'Batsman does not exist'}), 404

    return jsonify({
        'batsman': item.get('batsman').get('S'),
        'highest_score': item.get('highest_score')
    })

@app.route("/v1/bestscore/2010s", methods=["POST"])
def create_batsman():
    batsman = request.json.get('batsman')
    highest_score = request.json.get('highest_score')
    if not batsman or not highest_score:
        return jsonify({'error': 'Please provide Batsman and Highest Score Details'}), 400
    resp = client.put_item(
        TableName = dynamoTableName,
        Item = {
            'artist'
        }
    )
    return jsonify{(
        'batsman': batsman,
        'highest_score': highest_score
    )}

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=5000)