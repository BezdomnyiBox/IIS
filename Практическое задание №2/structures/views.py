from app import app, auth
from flask import jsonify, abort, make_response, request
from structures.models import *
from structures.serializers import *

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request - Missing required fields'}), 400)

@app.route("/structures/api/v1/regions", methods=["GET"])
@auth.login_required
def get_regions():
    regions = get_all_regions()
    return jsonify({"regions": regions_cschema.dump(regions)})

@app.route("/structures/api/v1/subregions", methods=["GET"])
@auth.login_required
def get_subregions():
    subregions = get_all_subregions()
    return jsonify({"subregions": subregions_cschema.dump(subregions)})

@app.route("/structures/api/v1/countries", methods=["GET"])
@auth.login_required
def get_countries():
    countries = get_all_countries()
    return jsonify({"countries": countries_cschema.dump(countries)})

@app.route("/structures/api/v1/exports", methods=["GET"])
@auth.login_required
def get_exports():
    exports = get_all_exports()
    return jsonify({"exports": exports_cschema.dump(exports)})

@app.route("/structures/api/v1/regions/<int:region_id>", methods=["GET"])
@auth.login_required
def get_region_by_id(region_id):
    region = get_one_region(region_id)
    if region is None:
        abort(404)
    return jsonify({"region": region_cschema.dump(region)})

@app.route("/structures/api/v1/subregions/<int:subregion_id>", methods=["GET"])
@auth.login_required
def get_subregion_by_id(subregion_id):
    subregion = get_one_subregion(subregion_id)
    if subregion is None:
        abort(404)
    return jsonify({"subregion": subregion_cschema.dump(subregion)})

@app.route("/structures/api/v1/countries/<int:country_id>", methods=["GET"])
@auth.login_required
def get_country_by_id(country_id):
    country = get_one_country(country_id)
    if country is None:
        abort(404)
    return jsonify({"country": country_cschema.dump(country)})

@app.route("/structures/api/v1/exports/<int:export_id>", methods=["GET"])
@auth.login_required
def get_export_by_id(export_id):
    export = get_one_export(export_id)
    if export is None:
        abort(404)
    return jsonify({"export": export_cschema.dump(export)})

@app.route("/structures/api/v1/regions/<int:region_id>/subregions", methods=["GET"])
@auth.login_required
def get_subregions_by_region_id(region_id):
    subregions = get_subregion_by_region(region_id)
    return jsonify({"subregions": subregions_cschema.dump(subregions)})

@app.route("/structures/api/v1/subregions/<int:subregion_id>/countries", methods=["GET"])
@auth.login_required
def get_countries_by_subregion_id(subregion_id):
    countries = get_country_by_subregion(subregion_id)
    return jsonify({"countries": countries_cschema.dump(countries)})

@app.route("/structures/api/v1/countries/<int:country_id>/exports", methods=["GET"])
@auth.login_required
def get_exports_by_country_id(country_id):
    exports = get_export_by_country(country_id)
    return jsonify({"exports": exports_cschema.dump(exports)})

@app.route("/structures/api/v1/exports/year/<int:year>", methods=["GET"])
@auth.login_required
def get_exports_by_year(year):
    exports = get_export_by_year(year)
    return jsonify({"exports": exports_cschema.dump(exports)})

@app.route("/structures/api/v1/regions", methods=["POST"])
@auth.login_required
def create_region():
    if (not request.json or 'name' not in request.json):
        abort(400)
    new_region = request.get_json()

    region_new = insert_region(new_region)
    return jsonify({'region': region_cschema.dump(region_new)}), 201

@app.route("/structures/api/v1/subregions", methods=["POST"])
@auth.login_required
def create_subregion():
    if (not request.json
        or 'name' not in request.json
        or 'region_id' not in request.json):
        abort(400)
    new_subregion = request.get_json()
    subregion_new = insert_subregion(new_subregion)
    return jsonify({'subregion': subregion_cschema.dump(subregion_new)}), 201

@app.route("/structures/api/v1/countries", methods=["POST"])
@auth.login_required
def create_country():
    if (not request.json
        or 'name' not in request.json
        or 'sub_region_id' not in request.json):
        abort(400)
    new_country = request.get_json()
    country_new = insert_country(new_country)
    return jsonify({'country': country_cschema.dump(country_new)}), 201

@app.route("/structures/api/v1/exports", methods=["POST"])
@auth.login_required
def create_export():
    if (not request.json 
        or 'country_id' not in request.json 
        or 'year' not in request.json 
        or 'value' not in request.json):
        abort(400)
    new_export = request.get_json()
    export_new = insert_export(new_export)
    return jsonify({'export': export_cschema.dump(export_new)}), 201

@app.route('/structures/api/v1/regions/<int:id>', methods=['PUT'])
@auth.login_required
def update_one_region(id):
    region = get_one_region(id)
    if region is None or not request.json:
        abort(404)
    if 'name' in request.json and type(request.json['name']) is not str:
        abort(400)
    region_update = update_region(id, request.get_json())
    return jsonify({'region': region_cschema.dump(region_update)})

@app.route('/structures/api/v1/subregions/<int:id>', methods=['PUT'])
@auth.login_required
def update_one_subregion(id):
    subregion = get_one_subregion(id)
    if subregion is None or not request.json:
        abort(404)
    if 'name' in request.json and type(request.json['name']) is not str:
        abort(400)
    subregion_update = update_subregion(id, request.get_json())
    return jsonify({'subregion': subregion_cschema.dump(subregion_update)})

@app.route('/structures/api/v1/countries/<int:id>', methods=['PUT'])
@auth.login_required
def update_one_country(id):
    country = get_one_country(id)
    if country is None or not request.json:
        abort(404)
    if 'name' in request.json and type(request.json['name']) is not str:
        abort(400)
    country_update = update_country(id, request.get_json())
    return jsonify({'country': country_cschema.dump(country_update)})

@app.route('/structures/api/v1/exports/<int:id>', methods=['PUT'])
@auth.login_required
def update_one_export(id):
    export = get_one_export(id)
    if export is None:
        abort(404)
    if not request.json:
        abort(400)
    
    # Проверяем типы данных только если поля присутствуют
    if 'country_id' in request.json and not isinstance(request.json['country_id'], int):
        abort(400)
    if 'year' in request.json and not isinstance(request.json['year'], int):
        abort(400)
    if 'value' in request.json and not isinstance(request.json['value'], (int, float)):
        abort(400)
    
    export_update = update_export(id, request.get_json())
    return jsonify({'export': export_cschema.dump(export_update)})

@app.route('/structures/api/v1/regions/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_one_region(id):
    if delete_region(id):
        return jsonify({'result': True})
    abort(404)
    
@app.route('/structures/api/v1/subregions/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_one_subregion(id):
    if delete_subregion(id):
        return jsonify({'result': True})
    abort(404)
    
@app.route('/structures/api/v1/countries/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_one_country(id):
    if delete_country(id):
        return jsonify({'result': True})
    abort(404)    
    
@app.route('/structures/api/v1/exports/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_one_export(id):
    if delete_export(id):
        return jsonify({'result': True})
    abort(404)
    
@app.route('/structures/api/v1/regions/<int:region_id>/max_export', methods=['GET'])
@auth.login_required
def max_export_by_region(region_id):
    max_export = get_max_export_by_region(region_id)
    if max_export is None:
        abort(404)
    return jsonify({"max_export": export_cschema.dump(max_export)})
    
@app.route('/structures/api/v1/regions/<int:region_id>/min_export', methods=['GET'])
@auth.login_required
def min_export_by_region(region_id):
    min_export = get_min_export_by_region(region_id)
    if min_export is None:
        abort(404)
    return jsonify({"min_export": export_cschema.dump(min_export)})

@app.route('/structures/api/v1/regions/<int:region_id>/avg_export', methods=['GET'])
@auth.login_required
def avg_export_by_region(region_id):
    avg_export = get_avg_export_by_region(region_id)
    if avg_export is None:
        abort(404)  
    return jsonify({"avg_export": avg_export})

@app.route('/structures/api/v1/exports/year/<int:year>/max_export', methods=['GET'])
@auth.login_required
def max_export_by_year(year):
    max_export = get_max_export_by_year(year)
    if max_export is None:
        abort(404)
    return jsonify({"max_export": export_cschema.dump(max_export)})

@app.route('/structures/api/v1/exports/year/<int:year>/min_export', methods=['GET'])
@auth.login_required
def min_export_by_year(year):
    min_export = get_min_export_by_year(year)
    if min_export is None:
        abort(404)
    return jsonify({"min_export": export_cschema.dump(min_export)})

@app.route('/structures/api/v1/exports/year/<int:year>/avg_export', methods=['GET'])
@auth.login_required
def avg_export_by_year(year):
    avg_export = get_avg_export_by_year(year)
    if avg_export is None:
        abort(404)
    return jsonify({"avg_export": avg_export})

@app.route('/structures/api/v1/countries/<int:country_id>/max_export', methods=['GET'])
@auth.login_required
def max_export_by_country(country_id):
    max_export = get_max_export_by_country(country_id)
    if max_export is None:
        abort(404)
    return jsonify({"max_export": export_cschema.dump(max_export)})
    
@app.route('/structures/api/v1/countries/<int:country_id>/min_export', methods=['GET'])
@auth.login_required
def min_export_by_country(country_id):
    min_export = get_min_export_by_country(country_id)
    if min_export is None:
        abort(404)
    return jsonify({"min_export": export_cschema.dump(min_export)})

@app.route('/structures/api/v1/countries/<int:country_id>/avg_export', methods=['GET'])
@auth.login_required
def avg_export_by_country(country_id):
    avg_export = get_avg_export_by_country(country_id)
    if avg_export is None:
        abort(404)
    return jsonify({"avg_export": avg_export})
