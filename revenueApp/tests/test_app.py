import pytest
import json
from django.conf import settings
from pathlib import Path
from app.models import Company

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'
    }


@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient


@pytest.mark.django_db
class TestTotalSales:
    endpoint = '/sales/'
    branch_id = '352h67i328fh'
    start = '2020-06-30'
    end = '2020-07-30'

    def test_hourly_sales(self, api_client):
        response = api_client().get(
            self.endpoint + f'hourly?branch_id={self.branch_id}&start={self.start}&end={self.end}'
        )
        
        assert response.status_code == 200
        assert len(json.loads(response.content)) > 0
        content = json.loads(response.content)
        assert content[0]['event_time'] == '2020-07-01T09:00:00'
        assert content[0]['total_sales'] == 60.20000000000016

    def test_daily_sales(self, api_client):
        response = api_client().get(
            self.endpoint + f'daily?branch_id={self.branch_id}&start={self.start}&end={self.end}'
        )
        assert response.status_code == 200
        assert len(json.loads(response.content)) > 0
        content = json.loads(response.content)
        assert content[0]['event_time'] == '2020-07-01T00:00:00'
        assert content[0]['total_sales'] == 1737.5999999999995