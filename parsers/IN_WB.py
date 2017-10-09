from requests import Session
from parsers import countrycode
from parsers import web
from parsers.lib import IN


def fetch_production(country_code='IN-WB', session=None):
    """Fetch West Bengal  production"""
    countrycode.assert_country_code(country_code, 'IN-WB')

    html = web.get_response_soup(country_code,
                                 'http://www.wbseb.gov.in/', session)
    india_date = IN.read_datetime_from_span_id(html, 'lblUpdatedOn', 'DD-MM-YYYY')

    # All thermal centrals are considered coal based production
    thermal_value = IN.read_value_from_span_id(html, 'lblStateGeneration')

    data = {
        'countryCode': country_code,
        'datetime': india_date.datetime,
        'production': {
            'biomass': 0.0,
            'coal': thermal_value,
            'gas': 0.0,
            'hydro': 0.0,
            'nuclear': 0.0,
            'oil': 0.0,
            'solar': 0.0,
            'wind': 0.0,
            'geothermal': 0.0,
        },
        'storage': {
            'hydro': 0.0
        },
        'source': 'http://www.wbseb.gov.in/',
    }

    return data


def fetch_consumption(country_code='IN-WB', session=None):
    """Fetch West Bengal consumption"""
    countrycode.assert_country_code(country_code, 'IN-WB')

    html = web.get_response_soup(country_code,
                                 'http://www.wbseb.gov.in/', session)
    india_date = IN.read_datetime_from_span_id(html, 'lblUpdatedOn', 'DD-MM-YYYY')

    demand_value = IN.read_value_from_span_id(html, 'lblDemandMet')

    data = {
        'countryCode': country_code,
        'datetime': india_date.datetime,
        'consumption': demand_value,
        'source': 'www.wbseb.gov.in'
    }

    return data


if __name__ == '__main__':
    session = Session()
    print fetch_production('IN-WB', session)
    print fetch_consumption('IN-WB', session)
