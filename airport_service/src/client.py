import requests

from airport_service.src.constans import Endpoint


class AeroportClient:

    def get_airports(self, raise_for_status=True) -> dict:
        resource = requests.get(Endpoint.airports)

        if raise_for_status:
            resource.raise_for_status()
        return resource.json()

    def get_distance_between_airports(self, from_airport: str, to_airport: str, raise_for_status=True) -> dict:
        resource = requests.post(
            Endpoint.airports_distance,
            data={
                "from": from_airport,
                "to": to_airport,
            },
        )

        if raise_for_status:
            resource.raise_for_status()
        return resource.json()
