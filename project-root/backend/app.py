from extensions import app, api, auth
from flask import jsonify, request

@auth.get_password
def get_password(username):
    if username == 'student':
        return 'dvfu'
    return None

@auth.error_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized access'}), 401

@app.route("/")
def hello_world():
    return jsonify({"app": "Экспорт товаров и услуг"})

# Импортируем ресурсы только после создания app, api, auth
from structures.views import (
    RegionListResource, RegionResource,
    SubRegionListResource, SubRegionResource,
    CountryListResource, CountryResource,
    ExportListResource, ExportResource,
    SubregionsByRegionResource, CountriesBySubregionResource, ExportsByCountryResource, ExportsByYearResource,
    MaxExportByRegionResource, MinExportByRegionResource, AvgExportByRegionResource,
    MaxExportByYearResource, MinExportByYearResource, AvgExportByYearResource,
    MaxExportByCountryResource, MinExportByCountryResource, AvgExportByCountryResource,
    GroupedByCountryResource, GroupedByYearResource, GroupedByRegionResource
)

api.add_resource(RegionListResource, '/structures/api/v1/regions')
api.add_resource(RegionResource, '/structures/api/v1/regions/<int:region_id>')

api.add_resource(SubRegionListResource, '/structures/api/v1/subregions')
api.add_resource(SubRegionResource, '/structures/api/v1/subregions/<int:subregion_id>')

api.add_resource(CountryListResource, '/structures/api/v1/countries')
api.add_resource(CountryResource, '/structures/api/v1/countries/<int:country_id>')

api.add_resource(ExportListResource, '/structures/api/v1/exports')
api.add_resource(ExportResource, '/structures/api/v1/exports/<int:export_id>')

# Вложенные ресурсы
api.add_resource(SubregionsByRegionResource, '/structures/api/v1/regions/<int:region_id>/subregions')
api.add_resource(CountriesBySubregionResource, '/structures/api/v1/subregions/<int:subregion_id>/countries')
api.add_resource(ExportsByCountryResource, '/structures/api/v1/countries/<int:country_id>/exports')
api.add_resource(ExportsByYearResource, '/structures/api/v1/exports/year/<int:year>')

# Агрегации
api.add_resource(MaxExportByRegionResource, '/structures/api/v1/regions/<int:region_id>/max_export')
api.add_resource(MinExportByRegionResource, '/structures/api/v1/regions/<int:region_id>/min_export')
api.add_resource(AvgExportByRegionResource, '/structures/api/v1/regions/<int:region_id>/avg_export')

api.add_resource(MaxExportByYearResource, '/structures/api/v1/exports/year/<int:year>/max_export')
api.add_resource(MinExportByYearResource, '/structures/api/v1/exports/year/<int:year>/min_export')
api.add_resource(AvgExportByYearResource, '/structures/api/v1/exports/year/<int:year>/avg_export')

api.add_resource(MaxExportByCountryResource, '/structures/api/v1/countries/<int:country_id>/max_export')
api.add_resource(MinExportByCountryResource, '/structures/api/v1/countries/<int:country_id>/min_export')
api.add_resource(AvgExportByCountryResource, '/structures/api/v1/countries/<int:country_id>/avg_export')

# Grouped data for charts
api.add_resource(GroupedByCountryResource, '/structures/api/v1/exports/grouped_by_country')
api.add_resource(GroupedByYearResource, '/structures/api/v1/exports/grouped_by_year')
api.add_resource(GroupedByRegionResource, '/structures/api/v1/exports/grouped_by_region')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
        