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
import typing as t

from rest_client import Requestor, ClientFactory
from rest_client.typing import RequestHandler

from subscription_manager_client.models import Topic, Subscription

__author__ = "EUROCONTROL (SWIM)"


class SubscriptionManagerClient(Requestor, ClientFactory):

    _BASE_URL = 'subscription-manager/api/1.0/'

    def __init__(self, request_handler: RequestHandler) -> None:
        """
        :param request_handler: an instance of an object capable of handling http requests, i.e. requests.session()
        """
        Requestor.__init__(self, request_handler)
        self._request_handler = request_handler

        self._url_topics = self._BASE_URL + 'topics/'
        self._url_topics_own = self._BASE_URL + 'topics/own'
        self._url_topic_by_id = self._BASE_URL + 'topics/{topic_id}'
        self._url_subscriptions = self._BASE_URL + 'subscriptions/'
        self._url_subscription_by_id = self._BASE_URL + 'subscriptions/{subscription_id}'
        self._url_ping_credentials = self._BASE_URL + 'ping-credentials'

    def get_topics(self) -> t.List[Topic]:
        return self.perform_request('GET', self._url_topics, response_class=Topic, many=True)

    def get_topics_own(self) -> t.List[Topic]:
        return self.perform_request('GET', self._url_topics_own, response_class=Topic, many=True)

    def get_topic_by_id(self, topic_id: int) -> Topic:
        url = self._url_topic_by_id.format(topic_id=topic_id)

        return self.perform_request('GET', url, response_class=Topic)

    def post_topic(self, topic: Topic) -> Topic:
        topic_data = topic.to_json()

        return self.perform_request('POST', self._url_topics, json=topic_data, response_class=Topic)

    # def put_topic(self, topic_id: int, topic: Topic) -> Topic:
    #     url = self._url_topic_by_id.format(topic_id=topic_id)
    #
    #     topic_data = topic.to_json()
    #
    #     return self.perform_request('PUT', url, json=topic_data, response_class=Topic)

    def delete_topic_by_id(self, topic_id: int):
        url = self._url_topic_by_id.format(topic_id=topic_id)

        self.perform_request('DELETE', url)

    def get_subscriptions(self, queue: t.Optional[str] = None) -> t.List[Subscription]:
        extra_params = {'queue': queue} if queue else {}

        return self.perform_request('GET', self._url_subscriptions, extra_params=extra_params,
                                    response_class=Subscription, many=True)

    def get_subscription_by_id(self, subscription_id: int) -> Subscription:
        url = self._url_subscription_by_id.format(subscription_id=subscription_id)

        return self.perform_request('GET', url, response_class=Subscription)

    def post_subscription(self, subscription: Subscription) -> Subscription:
        subscription_data = subscription.to_json()

        return self.perform_request('POST', self._url_subscriptions, json=subscription_data,
                                    response_class=Subscription)

    def put_subscription(self, subscription_id: int, subscription: Subscription) -> Subscription:
        url = self._url_subscription_by_id.format(subscription_id=subscription_id)

        subscription_data = subscription.to_json()

        return self.perform_request('PUT', url, json=subscription_data, response_class=Subscription)

    def delete_subscription_by_id(self, subscription_id: int):
        url = self._url_subscription_by_id.format(subscription_id=subscription_id)

        self.perform_request('DELETE', url)

    def ping_credentials(self):

        return self.perform_request('GET', self._url_ping_credentials)
