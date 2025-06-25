from extensions import app, auth
from flask import jsonify, abort, make_response, request
from structures.models import *
from structures.serializers import *
from flask_restful import Resource

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request - Missing required fields'}), 400)


class RegionListResource(Resource):
    method_decorators = [auth.login_required]

    def get(self):
        regions = get_all_regions()
        return {"regions": regions_cschema.dump(regions)}, 200

    def post(self):
        if not request.json or 'name' not in request.json:
            abort(400)
        new_region = request.get_json()
        region_new = insert_region(new_region)
        return {'region': region_cschema.dump(region_new)}, 201

class RegionResource(Resource):
    method_decorators = [auth.login_required]

    def get(self, region_id):
        region = get_one_region(region_id)
        if region is None:
            abort(404)
        return {"region": region_cschema.dump(region)}, 200

    def put(self, region_id):
        region = get_one_region(region_id)
        if region is None or not request.json:
            abort(404)
        if 'name' in request.json and type(request.json['name']) is not str:
            abort(400)
        region_update = update_region(region_id, request.get_json())
        return {'region': region_cschema.dump(region_update)}, 200

    def delete(self, region_id):
        if delete_region(region_id):
            return {'result': True}, 200
        abort(404)

class SubRegionListResource(Resource):
    method_decorators = [auth.login_required]

    def get(self):
        subregions = get_all_subregions()
        return {"subregions": subregions_cschema.dump(subregions)}, 200

    def post(self):
        if not request.json or 'name' not in request.json or 'region_id' not in request.json:
            abort(400)
        new_subregion = request.get_json()
        subregion_new = insert_subregion(new_subregion)
        return {'subregion': subregion_cschema.dump(subregion_new)}, 201

class SubRegionResource(Resource):
    method_decorators = [auth.login_required]

    def get(self, subregion_id):
        subregion = get_one_subregion(subregion_id)
        if subregion is None:
            abort(404)
        return {"subregion": subregion_cschema.dump(subregion)}, 200

    def put(self, subregion_id):
        subregion = get_one_subregion(subregion_id)
        if subregion is None or not request.json:
            abort(404)
        if 'name' in request.json and type(request.json['name']) is not str:
            abort(400)
        subregion_update = update_subregion(subregion_id, request.get_json())
        return {'subregion': subregion_cschema.dump(subregion_update)}, 200

    def delete(self, subregion_id):
        if delete_subregion(subregion_id):
            return {'result': True}, 200
        abort(404)

class CountryListResource(Resource):
    method_decorators = [auth.login_required]

    def get(self):
        countries = get_all_countries()
        return {"countries": countries_cschema.dump(countries)}, 200

    def post(self):
        if not request.json or 'name' not in request.json or 'sub_region_id' not in request.json:
            abort(400)
        new_country = request.get_json()
        country_new = insert_country(new_country)
        return {'country': country_cschema.dump(country_new)}, 201

class CountryResource(Resource):
    method_decorators = [auth.login_required]

    def get(self, country_id):
        country = get_one_country(country_id)
        if country is None:
            abort(404)
        return {"country": country_cschema.dump(country)}, 200

    def put(self, country_id):
        country = get_one_country(country_id)
        if country is None or not request.json:
            abort(404)
        if 'name' in request.json and type(request.json['name']) is not str:
            abort(400)
        country_update = update_country(country_id, request.get_json())
        return {'country': country_cschema.dump(country_update)}, 200

    def delete(self, country_id):
        if delete_country(country_id):
            return {'result': True}, 200
        abort(404)

class ExportListResource(Resource):
    method_decorators = [auth.login_required]

    def get(self):
        exports = get_all_exports()
        return {"exports": exports_cschema.dump(exports)}, 200

    def post(self):
        if not request.json or 'country_id' not in request.json or 'year' not in request.json or 'value' not in request.json:
            abort(400)
        new_export = request.get_json()
        export_new = insert_export(new_export)
        return {'export': export_cschema.dump(export_new)}, 201

class ExportResource(Resource):
    method_decorators = [auth.login_required]

    def get(self, export_id):
        export = get_one_export(export_id)
        if export is None:
            abort(404)
        return {"export": export_cschema.dump(export)}, 200

    def put(self, export_id):
        export = get_one_export(export_id)
        if export is None:
            abort(404)
        if not request.json:
            abort(400)
        if 'country_id' in request.json and not isinstance(request.json['country_id'], int):
            abort(400)
        if 'year' in request.json and not isinstance(request.json['year'], int):
            abort(400)
        if 'value' in request.json and not isinstance(request.json['value'], (int, float)):
            abort(400)
        export_update = update_export(export_id, request.get_json())
        return {'export': export_cschema.dump(export_update)}, 200

    def delete(self, export_id):
        if delete_export(export_id):
            return {'result': True}, 200
        abort(404)

# Вложенные ресурсы и агрегации
class SubregionsByRegionResource(Resource):
    method_decorators = [auth.login_required]
    def get(self, region_id):
        subregions = get_subregion_by_region(region_id)
        return {"subregions": subregions_cschema.dump(subregions)}, 200

class CountriesBySubregionResource(Resource):
    method_decorators = [auth.login_required]
    def get(self, subregion_id):
        countries = get_country_by_subregion(subregion_id)
        return {"countries": countries_cschema.dump(countries)}, 200

class ExportsByCountryResource(Resource):
    method_decorators = [auth.login_required]
    def get(self, country_id):
        exports = get_export_by_country(country_id)
        return {"exports": exports_cschema.dump(exports)}, 200

class ExportsByYearResource(Resource):
    method_decorators = [auth.login_required]
    def get(self, year):
        exports = get_export_by_year(year)
        return {"exports": exports_cschema.dump(exports)}, 200

# Агрегации max/min/avg
class MaxExportByRegionResource(Resource):
    method_decorators = [auth.login_required]
    def get(self, region_id):
        max_export = get_max_export_by_region(region_id)
        if max_export is None:
            abort(404)
        return {"max_export": export_cschema.dump(max_export)}, 200

class MinExportByRegionResource(Resource):
    method_decorators = [auth.login_required]
    def get(self, region_id):
        min_export = get_min_export_by_region(region_id)
        if min_export is None:
            abort(404)
        return {"min_export": export_cschema.dump(min_export)}, 200

class AvgExportByRegionResource(Resource):
    method_decorators = [auth.login_required]
    def get(self, region_id):
        avg_export = get_avg_export_by_region(region_id)
        if avg_export is None:
            abort(404)
        return {"avg_export": avg_export}, 200

class MaxExportByYearResource(Resource):
    method_decorators = [auth.login_required]
    def get(self, year):
        max_export = get_max_export_by_year(year)
        if max_export is None:
            abort(404)
        return {"max_export": export_cschema.dump(max_export)}, 200

class MinExportByYearResource(Resource):
    method_decorators = [auth.login_required]
    def get(self, year):
        min_export = get_min_export_by_year(year)
        if min_export is None:
            abort(404)
        return {"min_export": export_cschema.dump(min_export)}, 200

class AvgExportByYearResource(Resource):
    method_decorators = [auth.login_required]
    def get(self, year):
        avg_export = get_avg_export_by_year(year)
        if avg_export is None:
            abort(404)
        return {"avg_export": avg_export}, 200

class MaxExportByCountryResource(Resource):
    method_decorators = [auth.login_required]
    def get(self, country_id):
        max_export = get_max_export_by_country(country_id)
        if max_export is None:
            abort(404)
        return {"max_export": export_cschema.dump(max_export)}, 200

class MinExportByCountryResource(Resource):
    method_decorators = [auth.login_required]
    def get(self, country_id):
        min_export = get_min_export_by_country(country_id)
        if min_export is None:
            abort(404)
        return {"min_export": export_cschema.dump(min_export)}, 200

class AvgExportByCountryResource(Resource):
    method_decorators = [auth.login_required]
    def get(self, country_id):
        avg_export = get_avg_export_by_country(country_id)
        if avg_export is None:
            abort(404)
        return {"avg_export": avg_export}, 200

class GroupedByCountryResource(Resource):
    method_decorators = [auth.login_required]
    def get(self):
        grouped_data = get_exports_grouped_by_country()
        return {"exports": grouped_data}, 200

class GroupedByYearResource(Resource):
    method_decorators = [auth.login_required]
    def get(self):
        grouped_data = get_exports_grouped_by_year()
        return {"exports": grouped_data}, 200

class GroupedByRegionResource(Resource):
    method_decorators = [auth.login_required]
    def get(self):
        grouped_data = get_exports_grouped_by_region()
        return {"exports": grouped_data}, 200
