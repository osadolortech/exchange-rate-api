from flask import request, jsonify
from application import app
import requests

print("i'm here")

@app.route('/exchange-rate', methods=['POST'])
def currency_conveerter():
    try:
        if request.method == 'POST':

            request_data = request.get_json()

            currency1 = request_data['currency1']
            currency2 = request_data['currency2']

            
            url = f"https://api.exchangerate-api.com/v4/latest/{currency1.upper()}"
            data = requests.get(url).json()

            rate = data['rates'][currency2.upper()]

            data = {"rate": rate}
        else:
            data = {"message": "Method unknown. please pass the right method"}
    except Exception as e:
        print(str(e))
        data = {"message": "Couldn't retrieve the rate between {currency1} and {currency2}"}

    return jsonify(data)