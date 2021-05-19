import pytest
import requests
from django.apps import apps
from . import views
import json
from django.test import SimpleTestCase


class Test(TestCase):
    def setUp(self):
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {get_access_token()}'

    @classmethod
    def setUpTestData(cls):
        GlobalEvent.objects.create(userID=1, name="Футбол", level="Международное", degree="индивидуальное", place=1,
                                   date=datetime.now(), points=3)

    def test_not_authorized(self):
        response = self.client.get("/api/sport/global_event/")
        assert response.status_code == 401 or response.status_code == 403

    def test_create_global_event(self):
        data = {
            "requestID": 0,
            "userID": "ignore_this",
            "name": "Баскетбол",
            "level": "международное",
            "degree": "командное",
            "place": 2,
            "date": "2021-05-13",
            "points": 0
        }
        response = self.client.post("/api/sport/global_event/", data=data)
        assert response.status_code == 200
        body = response.json()
        assert type(body) is dict

    def test_get_global_events(self):
        response = self.client.get("/api/sport/global_event/")
        assert response.status_code == 200

    def test_create_global_event_with_incorrect_place_returns_400(self):
        response = self.client.post("/api/sport/global_event/", data={
            "requestID": 0,
            "userID": "ignore_this",
            "name": "string",
            "level": "string",
            "degree": "string",
            "place": -10,
            "date": "2021-05-13",
            "points": 0
        })
        assert response.status_code / 100 == 4

