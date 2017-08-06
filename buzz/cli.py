import click
import requests
from pprint import pprint

def build_request(airport):

    """creates query string"""

    base_url = 'https://services.faa.gov/airport/status/'
    request_string = base_url + airport + '/?format=application/json'

    return request_string


def get_request(airport='DCA'):

    """queris FAA services for airport information"""

    s = requests.session()
    request_string = build_request(airport)
    r = s.get(request_string)

    return r.json()


def parse_temp(r, unit='f'):

    """parses response object to get temperature"""

    # parse temp
    temp = r['weather']['temp'].split(' ')
    tempF = float(temp[0])
    tempC = float(temp[2].replace('(', ''))

    if unit == 'f':
        return tempF
    else:
        return tempC


@click.command()
@click.argument('airport')
@click.option('--temp_only', is_flag=True)
def cli(airport, temp_only):

    """queries FAA services API and returns airport information"""

    # get airport informaiton
    r = get_request(airport)

    # return what the user wants
    if temp_only:
        temp = parse_temp(r, unit='f')
        print(temp)

    else:
        pprint(r)
