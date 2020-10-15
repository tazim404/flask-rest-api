from flask import Flask, jsonify

data = {"States": ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chattisgarh", "Goa", "Gujrat", "Haryana",
                   "Himacha Pradesh", "Jharkhand", "Karnataka", "Kerela", "Madhya Pradesh", "Maharashtra", "Manipur",
                   "Mehgalya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajashthan", "Sikkim", "Tamil Nadu",
                   "Telangna",
                   "Tripura", "Uttar Pradesh", "Uttrakhand", "West Bengal"],
        "Union Territory": ["Andaman and Nicobar Island", "Chandigarh", "Daman And Diu", "Dadar and Nagar Haweli",
                            "Delhi", "Jammu and Kashmir", "Ladakh", "Lakhsdeep", "Puducherry"]
        }
app = Flask(__name__)
# Check whater it is in devleopment env or produnction env
ENV = "DEV"
if ENV == "DEV":
    app.debug = True
else:
    app.debug = False


@app.route('/')
def home():
    return "This is home page"


@app.route('/india/state')
def state():
    final_data = data['States']
    return jsonify(final_data)


@app.route('/india/union')
def union():
    final_data = data['Union Territory']
    return jsonify(final_data)


if __name__ == '__main__':
    app.run()
