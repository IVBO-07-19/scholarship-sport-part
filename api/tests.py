import pytest
import requests
from django.apps import apps
from . import views
import json
from datetime import datetime

from django.test import TestCase

from .models import *


def get_access_token():
    r = requests.post('https://suroegin503.eu.auth0.com/oauth/token', data={
        'grant_type': 'password',
        'username': 'testingemail@gmail.com',
        'password': 'TestPassword1_',
        'scope': 'openid profile email',
        'audience': 'https://welcome/',
        'client_id': 'PdkS09Ig0EYVGK9KPYwncjKMGzXnAasI'})
    return r.json()['access_token']

token = get_access_token()
class Test(TestCase):
    def setUp(self):
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {token}'

    @classmethod
    def setUpTestData(cls):
        GlobalEvent.objects.create(userID=1, name="Футбол", level="Международное", degree="индивидуальное", place=1,
                                   date=datetime.now(), points=3)
        TRPBadge.objects.create(trp_badge=True, age_group=3, date=datetime.now(), points=3)
        NationalPart.objects.create(requestID=7, userID=54, name="veagsrgsr", degree= "командное", date="2021-06-13",
            points= 0)
        NotNationalPart.objects.create(requestID=7, userID=54, name="veagsrgsr", degree= "командное",level="всероссийское", date="2021-06-13",
            points= 0)


        Online.objects.create(requestID=794, name="Футбол",date = datetime.now(),points=323124135)
    def test_authorized(self):
        response = self.client.get("/api/sport/global_event/")
        assert response.status_code != 401 and response.status_code != 403

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

    # def test_get_global_events_by_id(self):
    #     response = self.client.get(f"/api/sport/global_event/2/")
    #     assert response.status_code == 200

    def test_get_trp(self):
        response = self.client.get("/api/sport/trp/")
        assert response.status_code == 200

    # def test_get_trp_by_id(self):
    #     response = self.client.get("/api/sport/trp/1/")
    #     assert response.status_code == 200

    def test_create_trp_with_incorrect_age_group(self):
        data={
            "requestID": 794,
            "userID": "ignore_this",
            "trp_badge": True,
            "date":"2021-06-13",
            "age_group":"170",
            "points": 20
        }
        response = self.client.post("/api/sport/trp/", data)
        assert response.status_code / 100 == 4

    def test_get_national(self):
        response = self.client.get("/api/sport/national/")
        assert response.status_code == 200

    def test_create_national_with_incorrect_degree(self):
        data={
            "requestID": 794,
            "userID":"ignore_this",
            "name": "gggggg",
            "degree": "aaaaaaaaaa",
            "date":"2021-06-13",
            "points": 0
        }
        response = self.client.post("/api/sport/national/", data)
        assert response.status_code / 100 == 4

    # def test_get_national_by_id(self):
    #     response = self.client.get("/api/sport/national/2/")
    #     assert response.status_code == 200

    def test_get_not_national(self):
        response = self.client.get("/api/sport/not_national/")
        assert response.status_code == 200

    def test_create_not_national_with_incorrect_degree(self):
        data={
            "requestID": 794,
            "userID":"ignore_this",
            "name": "gggggg",
            "level":"региональное",
            "degree": "aaaaaaaaaa",
            "date":"2021-06-13",
            "points": 0
        }
        response = self.client.post("/api/sport/national/", data)
        assert response.status_code / 100 == 4

    def test_create_not_national_with_incorrect_level(self):
        data={
            "requestID": 794,
            "userID":"ignore_this",
            "name": "gggggg",
            "level":"раолцарпцдкп",
            "degree": "индивидуальное",
            "date":"2021-06-13",
            "points": 0
        }
        response = self.client.post("/api/sport/not_national/", data)
        assert response.status_code / 100 == 4


    def test_get_online_event(self):
        response = self.client.get("/api/sport/online_event/")
        assert response.status_code == 200

    # def test_get_online_event_by_id(self):
    #     response = self.client.get("/api/sport/online_event/3/")
    #     assert response.status_code == 200

    def test_get_request(self):
        response = self.client.get("/api/sport/request/10")
        print(response.status_code)
        assert response.status_code == 200

    def test_create_global_event_with_incorrect_place_returns_400(self):
        response = self.client.post("/api/sport/global_event/", data={
            "requestID": 794,
            "userID": "ignore_this",
            "name": "string",
            "level": "string",
            "degree": "string",
            "place": -10,
            "date": "2021-05-13",
            "points": 0
        })
        assert response.status_code / 100 == 4

    def test_get_by_request_id(self):
        response = self.client.get("/api/sport/request/1")
        assert response.status_code == 200
        data = response.json()
        assert type(data) is dict
        assert list(data.keys()) == ['1', '2', '3.1', '3.2', '3.3']
