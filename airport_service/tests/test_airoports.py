from pytest import fixture


@fixture(scope='module')
def airports(aeroport_client) -> list:
    return aeroport_client.get_airports()['data']


def test_verify_airport_count(airports) -> None:
    exp_airports_num = 30
    assert len(airports) == exp_airports_num, \
        f'Number of airports should be {exp_airports_num}. Found {len(airports)}'


def test_verify_specific_airports(airports) -> None:
    exp_airports = ['Akureyri Airport', 'St. Anthony Airport', 'CFB Bagotville']
    for airport in airports:
        airport_name = airport['attributes']['name']
        if airport_name in exp_airports:
            exp_airports.remove(airport_name)
    assert not exp_airports, f'Remained airports {exp_airports} are not present in response'


def test_verify_distance_between_airports(aeroport_client) -> None:
    data = aeroport_client.get_distance_between_airports(from_airport='KIX', to_airport='NRT')['data']
    exp_distance = 400
    actual_distance = data['attributes']['kilometers']
    assert actual_distance > exp_distance, \
        f'Expected distance more {exp_distance} kilometers, got {actual_distance}'
