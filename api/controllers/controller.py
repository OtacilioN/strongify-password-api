from api import app, jsonify, request


@app.route("/", methods=['GET'])
def start():
    return "Foi"


@app.route("/api/strongify-password", methods=['POST'])
def strongify_password():
    """
        This route will return all products
    """

    password = request.args.get("password")

    try:
        return jsonify({"status": "success", "data": password})
    except Exception as error:
        return jsonify({"status": "error", "error": str(error)})
