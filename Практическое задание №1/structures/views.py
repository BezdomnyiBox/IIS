from app import app
from flask import render_template
from structures.models import (
    get_countries_in_region, 
    get_exports_for_country, 
    get_top_exporting_countries_per_year,
    get_bottom_20_exporting_countries,
    get_top_20_exporting_countries
)



@app.route('/')
def index():
    
    [countries_in_region_head, countries_in_region_body] = get_countries_in_region('ЮЖНАЯ АЗИЯ');
    [exports_for_country_head, exports_for_country_body] = get_exports_for_country('INDIA');
    [top_exporting_countries_per_year_head, top_exporting_countries_per_year_body] = get_top_exporting_countries_per_year();
    [bottom_20_exporting_countries_head, bottom_20_exporting_countries_body] = get_bottom_20_exporting_countries();
    [top_20_exporting_countries_head, top_20_exporting_countries_body] = get_top_20_exporting_countries();
    
    html = render_template(
        'index.html',
        countries_in_region_region='ЮЖНАЯ АЗИЯ',
        countries_in_region_head=countries_in_region_head,
        countries_in_region_body=countries_in_region_body,
        exports_for_country_country='INDIA',
        exports_for_country_head=exports_for_country_head, 
        exports_for_country_body=exports_for_country_body,
        top_exporting_countries_per_year_head=top_exporting_countries_per_year_head,
        top_exporting_countries_per_year_body=top_exporting_countries_per_year_body,
        bottom_20_exporting_countries_head=bottom_20_exporting_countries_head,
        bottom_20_exporting_countries_body=bottom_20_exporting_countries_body,
        top_20_exporting_countries_head=top_20_exporting_countries_head,
        top_20_exporting_countries_body=top_20_exporting_countries_body
    )

    return html