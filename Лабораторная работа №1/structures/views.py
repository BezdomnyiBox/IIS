from app import app
from flask import render_template
from structures.models import get_all_buildings, get_building_stats_by_type, get_building_stats_by_country, get_building_stats_by_year, get_buildings_by_year_range


@app.route('/')
def index():

    [buildings_head, buildings_body] = get_all_buildings()
    [building_stats_by_type_head, building_stats_by_type_body] = get_building_stats_by_type()
    [building_stats_by_country_head, building_stats_by_country_body] = get_building_stats_by_country()
    [building_stats_by_year_head, building_stats_by_year_body] = get_building_stats_by_year()
    [building_stats_by_year_range_head, building_stats_by_year_range_body] = get_buildings_by_year_range(2000,2018)
    

    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body,
        building_stats_by_type_head=building_stats_by_type_head,
        building_stats_by_type_body=building_stats_by_type_body,
        building_stats_by_country_head=building_stats_by_country_head,
        building_stats_by_country_body=building_stats_by_country_body,
        building_stats_by_year_head=building_stats_by_year_head,
        building_stats_by_year_body=building_stats_by_year_body,
        building_stats_by_year_range_head=building_stats_by_year_range_head,
        building_stats_by_year_range_body=building_stats_by_year_range_body
    )

    return html