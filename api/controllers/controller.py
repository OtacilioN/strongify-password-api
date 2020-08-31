from api import app, jsonify, request
from api.service import strongify_service

@app.route("/", methods=['GET'])
def home_page():
    return "<h1>Enter in this url to instructions about how to use this api https://github.com/OtacilioN/strongify-password-api<h1/>"


@app.route("/api/strongify-password", methods=['POST'])
def strongify_password():
    """
        This route will recive a password and return five password options
    """

    params = request.json
    password = params["password"]

    try:
        password_array = []

        for i in range(0, 5):
            new_password = strongify_service.strongify_password(
                password=password)
            password_array.append(new_password)
        return jsonify({"msg": "success", "data": password_array})

    except Exception as error:
        return jsonify({"msg": "error", "data": str(error)})
