"""
Copyright 2019 EUROCONTROL
==========================================

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the 
following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following 
   disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following 
   disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products 
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, 
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE 
USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

==========================================

Editorial note: this license is an instance of the BSD license template as provided by the Open Source Initiative: 
http://opensource.org/licenses/BSD-3-Clause

Details on EUROCONTROL: http://www.eurocontrol.int
"""
from unittest.mock import Mock

import pytest
from rest_client.errors import APIError

from subscription_manager_client.subscription_manager import SubscriptionManagerClient
from tests.utils import make_topic_list, make_topic, make_subscription_list, make_subscription

__author__ = "EUROCONTROL (SWIM)"


BASE_URL = 'subscription-manager/api/1.0/'


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_get_topics__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code

    request_handler = Mock()
    request_handler.get = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.get_topics()


def test_get_topics__list_of_topics_is_returned():
    topic_dict_list, expected_topic_list = make_topic_list()

    response = Mock()
    response.status_code = 200
    response.content = topic_dict_list
    response.json = Mock(return_value=topic_dict_list)

    request_handler = Mock()
    request_handler.get = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    topic_list = client.get_topics()

    assert expected_topic_list == topic_list

    called_url = request_handler.get.call_args[0][0]
    assert BASE_URL + 'topics/' == called_url


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_get_topics_own__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code

    request_handler = Mock()
    request_handler.get = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.get_topics_own()


def test_get_topics_own__list_of_topics_is_returned():
    topic_dict_list, expected_topic_list = make_topic_list()

    response = Mock()
    response.status_code = 200
    response.content = topic_dict_list
    response.json = Mock(return_value=topic_dict_list)

    request_handler = Mock()
    request_handler.get = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    topic_list = client.get_topics_own()

    assert expected_topic_list == topic_list

    called_url = request_handler.get.call_args[0][0]
    assert BASE_URL + 'topics/own' == called_url


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_get_topic_by_id__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code

    request_handler = Mock()
    request_handler.get = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.get_topic_by_id(1)


def test_get_topic_by_id__list_of_topics_is_returned():
    topic_dict, expected_topic = make_topic()

    response = Mock()
    response.status_code = 200
    response.content = topic_dict
    response.json = Mock(return_value=topic_dict)

    request_handler = Mock()
    request_handler.get = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    topic = client.get_topic_by_id(1)

    assert expected_topic == topic

    called_url = request_handler.get.call_args[0][0]
    assert BASE_URL + 'topics/1' == called_url


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_post_topic__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code

    request_handler = Mock()
    request_handler.post = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.post_topic(Mock())


def test_post_topic__topic_object_is_returned():
    topic_dict, expected_topic = make_topic()

    response = Mock()
    response.status_code = 201
    response.content = topic_dict
    response.json = Mock(return_value=topic_dict)

    request_handler = Mock()
    request_handler.post = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    topic = client.post_topic(Mock())

    assert expected_topic == topic

    called_url = request_handler.post.call_args[0][0]
    assert BASE_URL + 'topics/' == called_url


# @pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
# def test_put_topic__http_error_code__raises_api_error(error_code):
#     response = Mock()
#     response.status_code = error_code
#
#     request_handler = Mock()
#     request_handler.put = Mock(return_value=response)
#
#     client = SubscriptionManagerClient(request_handler=request_handler)
#
#     with pytest.raises(APIError):
#         client.put_topic(1, Mock())
#
#
# def test_put_topic__topic_object_is_returned():
#     topic_dict, expected_topic = make_topic()
#
#     response = Mock()
#     response.status_code = 200
#     response.content = topic_dict
#     response.json = Mock(return_value=topic_dict)
#
#     request_handler = Mock()
#     request_handler.put = Mock(return_value=response)
#
#     client = SubscriptionManagerClient(request_handler=request_handler)
#
#     topic = client.put_topic(1, Mock())
#
#     assert expected_topic == topic
#
#     called_url = request_handler.put.call_args[0][0]
#     assert BASE_URL + 'topics/1' == called_url


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_delete_topic_by_id__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code

    request_handler = Mock()
    request_handler.delete = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.delete_topic_by_id(1)


def test_delete_topic_by_id():
    response = Mock()
    response.status_code = 204
    response.content = {}
    response.json = Mock(return_value={})

    request_handler = Mock()
    request_handler.delete = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    topic = client.delete_topic_by_id(1)

    called_url = request_handler.delete.call_args[0][0]
    assert BASE_URL + 'topics/1' == called_url


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_get_subscriptions__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code

    request_handler = Mock()
    request_handler.get = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.get_subscriptions()


def test_get_subscriptions__list_of_subscriptions_is_returned():
    subscription_dict_list, expected_subscription_list = make_subscription_list()

    response = Mock()
    response.status_code = 200
    response.content = subscription_dict_list
    response.json = Mock(return_value=subscription_dict_list)

    request_handler = Mock()
    request_handler.get = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    subscription_list = client.get_subscriptions()

    assert expected_subscription_list == subscription_list

    called_url = request_handler.get.call_args[0][0]
    assert BASE_URL + 'subscriptions/' == called_url


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_get_subscription_by_id__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code

    request_handler = Mock()
    request_handler.get = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.get_subscription_by_id(1)


def test_get_subscription_by_id__list_of_subscriptions_is_returned():
    subscription_dict, expected_subscription = make_subscription()

    response = Mock()
    response.status_code = 200
    response.content = subscription_dict
    response.json = Mock(return_value=subscription_dict)

    request_handler = Mock()
    request_handler.get = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    subscription = client.get_subscription_by_id(1)

    assert expected_subscription == subscription

    called_url = request_handler.get.call_args[0][0]
    assert BASE_URL + 'subscriptions/1' == called_url


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_post_subscription__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code

    request_handler = Mock()
    request_handler.post = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.post_subscription(Mock())


def test_post_subscription__subscription_object_is_returned():
    subscription_dict, expected_subscription = make_subscription()

    response = Mock()
    response.status_code = 201
    response.content = subscription_dict
    response.json = Mock(return_value=subscription_dict)

    request_handler = Mock()
    request_handler.post = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    subscription = client.post_subscription(Mock())

    assert expected_subscription == subscription

    called_url = request_handler.post.call_args[0][0]
    assert BASE_URL + 'subscriptions/' == called_url


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_put_subscription__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code

    request_handler = Mock()
    request_handler.put = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.put_subscription(1, Mock())


def test_put_subscription__subscription_object_is_returned():
    subscription_dict, expected_subscription = make_subscription()

    response = Mock()
    response.status_code = 200
    response.content = subscription_dict
    response.json = Mock(return_value=subscription_dict)

    request_handler = Mock()
    request_handler.put = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    subscription = client.put_subscription(1, Mock())

    assert expected_subscription == subscription

    called_url = request_handler.put.call_args[0][0]
    assert BASE_URL + 'subscriptions/1' == called_url


@pytest.mark.parametrize('error_code', [400, 401, 403, 404, 500])
def test_delete_subscription_by_id__http_error_code__raises_api_error(error_code):
    response = Mock()
    response.status_code = error_code

    request_handler = Mock()
    request_handler.delete = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    with pytest.raises(APIError):
        client.delete_subscription_by_id(1)


def test_delete_subscription_by_id():
    response = Mock()
    response.status_code = 204
    response.content = {}
    response.json = Mock(return_value={})

    request_handler = Mock()
    request_handler.delete = Mock(return_value=response)

    client = SubscriptionManagerClient(request_handler=request_handler)

    subscription = client.delete_subscription_by_id(1)

    called_url = request_handler.delete.call_args[0][0]
    assert BASE_URL + 'subscriptions/1' == called_url
