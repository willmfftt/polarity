import logging

import jsonpickle
import requests


class HostDeployment:

    @staticmethod
    def deploy(base_url, hosts, shared_users=None):
        logging.info("Sending hosts to C&C")

        url = "{}/hosts".format(base_url)

        request_data = {
            "hosts": jsonpickle.encode(hosts)
        }

        if shared_users:
            request_data.update({
                "shared_users": jsonpickle.encode(shared_users)
            })

        requests.post(url, json=request_data)
