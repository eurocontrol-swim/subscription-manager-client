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
from subscription_manager_client.models import Topic, Subscription

__author__ = "EUROCONTROL (SWIM)"


def make_topic(name='topic'):
    topic_dict = {
        'name': name,
        'id': 1
    }

    topic = Topic.from_json(topic_dict)

    return topic_dict, topic


def make_topic_list():
    topic_dict_1, topic_1 = make_topic()
    topic_dict_2, topic_2 = make_topic(name='another_topic')

    return [topic_dict_1, topic_dict_2], [topic_1, topic_2]


def make_subscription(queue='queue'):
    subscription_dict = {
        'queue': queue,
        'topic': {
            'name': 'topic',
            'id': 1
        },
        'active': True,
        'qos': 'EXACTLY_ONCE',
        'durable': True,
        'id': 1
    }

    subscription = Subscription.from_json(subscription_dict)

    return subscription_dict, subscription


def make_subscription_list():
    subscription_dict_1, subscription_1 = make_subscription()
    subscription_dict_2, subscription_2 = make_subscription(queue='another_queue')

    return [subscription_dict_1, subscription_dict_2], [subscription_1, subscription_2]
