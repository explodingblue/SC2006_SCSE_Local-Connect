from flask import Blueprint, request, jsonify, current_app
import requests

external_bp = Blueprint("external_bp", __name__)

@external_bp.route("/maps/geocode", methods=["GET"])
def geocode_address():
    address = request.args.get("address")
    if not address:
        return jsonify({"error": "address param required"}), 400

    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": current_app.config["GOOGLE_MAPS_API_KEY"]}
    resp = requests.get(url, params=params)
    return jsonify(resp.json())

@external_bp.route("/govsg/air-temperature", methods=["GET"])
def gov_air_temperature():
    resp = requests.get("https://api.data.gov.sg/v1/environment/air-temperature")
    return jsonify(resp.json())
