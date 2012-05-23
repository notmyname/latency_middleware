# Copyright 2011-2012 John Dickinson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from eventlet import sleep


class LatencyController(object):
    """
    Middleware to add simulated latency into a wsgi pipeline.

    latency sets the total latency. request_latency and response_latency can
    be used to set the request or response latency, respectively. If either
    the request or response latency are set to empty (default), the value is
    understood to mean half of the latency value

    Each config value is the number of miliseconds of latency to add.
    """
    def __init__(self, app, conf):
        self.app = app
        latency = conf.get('latency', '')
        if latency == '':
            latency = 0
        else:
            latency = int(latency)
        request_latency = conf.get('request_latency', '')
        if request_latency == '':
            request_latency = None
            self.request_latency = (latency // 2) / 1000.
        else:
            self.request_latency = int(request_latency) / 1000.
        response_latency = conf.get('response_latency', '')
        if response_latency == '':
            response_latency = None
            self.response_latency = (latency // 2) / 1000.
        else:
            self.response_latency = int(response_latency) / 1000.

    def __call__(self, env, start_response):
        self.app.logger.debug('Sleeping %.4f seconds for request latency' %
                                self.request_latency)
        sleep(self.request_latency)
        resp = self.app(env, start_response)
        self.app.logger.debug('Sleeping %.4f seconds for response latency' %
                                self.response_latency)
        sleep(self.response_latency)
        return resp


def filter_factory(global_conf, **local_conf):
    """paste.deploy app factory for creating WSGI container server apps"""
    conf = global_conf.copy()
    conf.update(local_conf)

    def latency_filter(app):
        return LatencyController(app, conf)
    return latency_filter
