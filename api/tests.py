import pytest
from django.apps import apps
from . import views
import json
from django.test import SimpleTestCase


class Test(SimpleTestCase):
    def test_not_authorized(self):
        response = self.client.get("/api/sport/global_event/")
        assert response.status_code == 401 or response.status_code == 403

    def test_get_article_writers(self):
        response = self.client.get("/api/sport/global_event/")
        assert response.status_code == 200
        assert type(response.json()) is list

    def test_create_global_event_sace_user_id(self):
        data = {
            "requestID": 0,
            "userID": "ingnore_this",
            "name": "Баскетбол",
            "level": "международное",
            "degree": "командное",
            "place": 2,
            "date": "2021-05-13",
            "points": 0
        }
        token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InBvV3dCYWRCMjIyejlBY3N2SHEwMiJ9.eyJpc3MiOiJodHRwczovL3N1cm9lZ2luNTAzLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDhhY2E0ODVlZmU5NzAwNjg0N2I1M2YiLCJhdWQiOlsiaHR0cHM6Ly93ZWxjb21lLyIsImh0dHBzOi8vc3Vyb2VnaW41MDMuZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMDkxODMxMCwiZXhwIjoxNjIxMDA0NzEwLCJhenAiOiJQZGtTMDlJZzBFWVZHSzlLUFl3bmNqS01HelhuQWFzSSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJndHkiOiJwYXNzd29yZCJ9.ZPBFPXzLTWtax_4XJQerhApz5zn1ICThv57O3qgM36dpPnfR4ZrhQFUzjoPkOu-hjKATkrzT9AnSgDroXJzFhvNp_bD6qjRCrU3vW4pauiE3UbKex5GuKdWa3dEVo0cNIpulMKv2_GdGjR70f2xveMtbrgtdZdU_yaJbIsgJDdW5YKfdSWVprqaMPBgGy_kPJMLdyBt0vPZVEpzyBsCobbSUS8e84X6z5-YKiVZ2IvIwSDM8n5dLGOYrGODcpRXKMA27cz0rkvGTzX4Cc_tIH4ynFKSm8kjHLGGhWJbWHMGRvfY1AaSudcbWjkXEN4XJMjIyb0d9YAhRhtZdcIvZoQ"
        head = {'Authorization': f'Bearer {token}'}
        response = self.client.post("/api/sport/global_event/", data=data, header=head)
        print(response.status_code)
        assert response.status_code == 200
        body = response.json()
        assert type(body) is dict



    def test_create_global_event_with_incorrect_place_returns_400(self):
        response = self.client.post("/api/sport/global_event/", data={
            "requestID": 0,
            "userID": "ingnore_this",
            "name": "string",
            "level": "string",
            "degree": "string",
            "place": -10,
            "date": "2021-05-13",
            "points": 0
        })

        assert response.status_code % 100 == 4
