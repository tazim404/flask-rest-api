from flask import Flask, request
from flask import jsonify

app = Flask(__name__)
data = {"States": ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chattisgarh", "Goa", "Gujrat", "Haryana",
                   "Himacha Pradesh", "Jharkhand", "Karnataka", "Kerela", "Madhya Pradesh", "Maharashtra", "Manipur",
                   "Mehgalya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajashthan", "Sikkim", "Tamil Nadu",
                   "Telangna",
                   "Tripura", "Uttar Pradesh", "Uttrakhand", "West Bengal"],
        "Union Territory": ["Andaman and Nicobar Island", "Chandigarh", "Daman And Diu", "Dadar and Nagar Haweli",
                            "Delhi", "Jammu and Kashmir", "Ladakh", "Lakhsdeep", "Puducherry"]
        }


@app.route('/')
def home():
    return "This is a homepage"


@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == "GET":
        return jsonify(data['States'])
    elif request.method == "POST":
        return jsonify(data['Union Territory'])


if __name__ == '__main__':
    app.run(debug=True)
