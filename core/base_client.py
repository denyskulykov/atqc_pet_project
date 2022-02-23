from core import app_logger
import requests
import urllib3
from warnings import simplefilter

logger = app_logger.get_logger()

simplefilter(
    'ignore',
    urllib3.exceptions.InsecureRequestWarning,
)


def _log_request(method, url, data=None, params=None):
    logger.debug(f'Making HTTP "{method}" request to "{url}", data: "{data}", params: "{params}"')


def _log_response(response):
    message = f'Received HTTP "{response.status_code}" response: "{response.text}"'
    if response.status_code >= 400:
        logger.warning(message)
    else:
        logger.debug(message)


def request(method, url, **kwargs):
    _log_request(method, url, kwargs)
    response = requests.request(method, url, **kwargs)
    _log_response(response)
    return response


def get(url, params=None, **kwargs):
    _log_request('GET', url, kwargs, params=params)
    response = requests.get(url, params, **kwargs)
    _log_response(response)
    return response


def post(url, data=None, json=None, **kwargs):
    _log_request('POST', url, kwargs, data)
    response = requests.post(url, data, json, **kwargs)
    _log_response(response)
    return response


def put(url, data=None, **kwargs):
    _log_request('PUT', url, kwargs, data)
    response = requests.put(url, data, **kwargs)
    _log_response(response)
    return response


def delete(url, **kwargs):
    _log_request('DELETE', url, kwargs)
    response = requests.delete(url, **kwargs)
    _log_response(response)
    return response
