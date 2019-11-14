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
import enum
import typing as t

from rest_client import BaseModel
from rest_client.typing import JSONType

__author__ = "EUROCONTROL (SWIM)"


class QOS(enum.Enum):
    """
    The Quality of Service required by the broker that will handle messages of some topic from a producer to a consumer
    """
    AT_LEAST_ONCE = "AT_LEAST_ONCE"
    AT_MOST_ONCE = "AT_MOST_ONCE"
    EXACTLY_ONCE = "EXACTLY_ONCE"

    @classmethod
    def all(cls):
        return [e.value for e in cls]


class Topic(BaseModel):

    def __init__(self, name: str, id: int = None) -> None:
        """
        :param name: the name of the topic
        :param id: the DB id of the topic
        """
        self.name: str = name
        self.id: int = id

    @classmethod
    def from_json(cls, object_dict: JSONType):
        """

        :param object_dict:
        :return: Topic
        """
        return cls(
            name=object_dict['name'],
            id=object_dict.get('id')
        )

    def to_json(self) -> JSONType:
        result = {
            'name': self.name
        }
        _update_if_not_none(result, 'id', self.id)

        return result


class Subscription(BaseModel):

    def __init__(self,
                 queue: t.Optional[str] = None,
                 active: t.Optional[bool] = None,
                 qos: t.Optional[QOS] = None,
                 durable: t.Optional[bool] = None,
                 topics: t.Optional[t.Union[t.List[Topic], t.List[str]]] = None,
                 id: t.Optional[int] = None) -> None:
        """
        :param queue: the unique name of the created queue upon a subscription request
        :param active: indicates whether the subscription is active or not
        :param qos: the Quality of Service handled by the broker for the specific subscription
        :param durable: expresses the durability of the subscription (if the messages will be kept while subscribers
                        are offline
        :param topic: the full topic structure associated with this subscription
        :param id: the DB id of the subsription
        """

        self.queue: str = queue
        self.active: bool = active
        self.durable: bool = durable
        self.topics: t.Union[t.List[Topic], t.List[str]] = topics
        self.id: int = id

        self._qos = None
        self.qos = qos

    @property
    def qos(self):
        return self._qos

    @qos.setter
    def qos(self, value):
        if value is not None and value not in QOS.all():
            raise ValueError(f'qos should be one of {QOS.all()}')

        self._qos = value

    @staticmethod
    def _topic_from_json(topic: t.Union[str, t.Dict[str, t.Any]]):
        if isinstance(topic, dict) and topic.get('id'):
            return Topic.from_json(topic)

        return topic

    @classmethod
    def from_json(cls, object_dict: JSONType):
        """

        :param object_dict:
        :return: Subscription
        """
        return cls(
            queue=object_dict['queue'],
            active=object_dict['active'],
            qos=object_dict['qos'],
            durable=object_dict['durable'],
            topics=[cls._topic_from_json(topic) for topic in object_dict['topics']],
            id=object_dict['id'],
        )

    def to_json(self):
        props = ['queue', 'topics', 'active', 'qos', 'durable', 'id']

        result = {}

        for prop in props:
            attr = getattr(self, prop)
            attr_json = _to_json(attr)
            _update_if_not_none(result, prop, attr_json)

        return result


def _to_json(value: t.Any):
    if isinstance(value, list):
        return [_to_json(val) for val in value]

    if hasattr(value, 'to_json'):
        return value.to_json()

    return value


def _update_if_not_none(d, prop, value):
    if value is not None:
        d[prop] = value
