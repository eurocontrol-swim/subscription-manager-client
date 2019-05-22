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
import pytest

from subscription_manager_client.models import Topic, Subscription, QOS

__author__ = "EUROCONTROL (SWIM)"


@pytest.mark.parametrize('topic_dict, expected_topic', [
    (
        {
            'name': 'topic',
            'id': 1
        },
        Topic(name='topic', id=1)
    )
])
def test_topic__from_json(topic_dict, expected_topic):
    topic = Topic.from_json(topic_dict)

    assert expected_topic == topic


@pytest.mark.parametrize('topic, expected_dict', [
    (
        Topic(name='topic', id=1),
        {
            'name': 'topic',
            'id': 1
        }
    )
])
def test_topic__to_json(topic, expected_dict):
    topic_dict = topic.to_json()

    assert expected_dict == topic_dict


@pytest.mark.parametrize('subscription_dict, expected_subscription', [
    (
        {
            'queue': 'queue name',
            'topic': {
                'name': 'topic',
                'id': 1
            },
            'active': True,
            'qos': 'EXACTLY_ONCE',
            'durable': True,
            'id': 1
        },
        Subscription(
            queue='queue name',
            topic=Topic(name='topic', id=1),
            active=True,
            qos=QOS.EXACTLY_ONCE.value,
            durable=True,
            id=1
        )
    )
])
def test_subscription__from_json(subscription_dict, expected_subscription):
    subscription = Subscription.from_json(subscription_dict)

    assert expected_subscription == subscription


@pytest.mark.parametrize('subscription, expected_dict', [
    (
        Subscription(
            queue='queue name',
            topic_id=1,
            topic=Topic(name='topic', id=1),
            active=True,
            qos=QOS.EXACTLY_ONCE.value,
            durable=True,
            id=1
        ),
        {
            'queue': 'queue name',
            'topic_id': 1,
            'topic': {
                'name': 'topic',
                'id': 1
            },
            'active': True,
            'qos': 'EXACTLY_ONCE',
            'durable': True,
            'id': 1
        }
    )
])
def test_subscription__to_json(subscription, expected_dict):
    subscription_dict = subscription.to_json()

    assert expected_dict == subscription_dict


@pytest.mark.parametrize('qos', ['invalid', 1, '', True])
def test_subscription__invalid_qos__raises_valueerror(qos):
    subscription = Subscription(queue='queue')

    with pytest.raises(ValueError) as e:
        subscription.qos = qos
    assert f'qos should be one of {QOS.all()}' == str(e.value)
