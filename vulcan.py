import requests
import json


class Vulcan:

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get_hosts(self):
        """
        GET /v2/hosts
        """
        resp = requests.get(self.endpoint +
                            "/v2/hosts")

        return resp.json()

    def upsert_host(self, hostname):
        """
        POST 'application/json' /v2/hosts
        """
        payload = {"Host": {"Name": hostname,
                            "Settings": {}}}
        print(payload)
        resp = requests.post(self.endpoint +
                             "/v2/hosts", data=json.dumps(payload))

        return resp.json()

    def delete_host(self, hostname):
        """
        DELETE /v2/hosts/<name>
        """
        resp = requests.delete(self.endpoint +
                               "/v2/hosts/{}".format(hostname))

        return resp.json()

    def get_backends(self):
        """
        GET /v2/backends
        """
        resp = requests.get(self.endpoint +
                            "/v2/backends")

        return resp.json()

    def upsert_backend(self, be_id, timeout_read=5, keepalive=30, idle_cons=12):
        """
        POST 'application/json' /v2/backends
        """

        payload = {"Backend": {"Id": be_id,
                               "Type": "http",
                               "Settings": {"Timeouts": {"Read": "{}s".format(timeout_read),
                                                         "Dial": "5s",
                                                         "TLSHandshake": "10s"},
                                            "KeepAlive": {"Period": "{}s".format(keepalive),
                                                          "MaxIdleConnsPerHost": idle_cons}}}}

        resp = requests.post(self.endpoint +
                             "/v2/backends",
                             data=json.dumps(payload))

        return resp.json()

    def delete_backend(self, backend):
        """
        DELETE /v2/backends/<id>
        """
        resp = requests.delete(self.endpoint +
                               "/v2/backends/{}".format(backend))

        return resp.json()

    def get_servers(self, backend):
        """
        GET /v2/backends/<id>/servers
        """
        resp = requests.get(self.endpoint +
                            "/v2/backends/{}/servers".format(backend))

        return resp.json()

    def get_server(self, backend, server):
        """
        GET /v2/backends/<backend>/servers/<server>

        """
        resp = requests.get(self.endpoint +
                            "/v2/backends/{}/servers/{}".format(backend,
                                                                server))

        return resp.json()

    def upsert_server(self, backend, server, server_url):
        """
        POST /v1/upstreams/<id>/endpoints
        """
        payload = {"Server": {"Id": server, "URL": server_url}}
        resp = requests.post(self.endpoint +
                             "/v2/backends/{}/servers".format(backend),
                             data=json.dumps(payload))
        print(payload)
        print(resp.text)

        return resp.json()

    def delete_server(self, backend, server):
        """
        DELETE /v2/backends/<id>/servers/<server-id>
        """
        resp = requests.delete(self.endpoint +
                               "/v2/backends/{}/servers/{}".format(backend,
                                                                   server))
        return resp.json()

    def get_frontends(self):
        """
        GET /v2/frontends
        """
        resp = requests.get(self.endpoint + "/v2/frontends")

        return resp.json()

    def get_frontend(self, fe_id):
        """
        GET /v2/frontends/<frontend-id>
        """
        resp = requests.get(self.endpoint +
                            "/v2/frontends/{}".format(fe_id))

        return resp.json()

    def upsert_frontend(self, fe_id, be_id, route="Path(`\/`)"):
        """
        POST 'application/json' /v2/frontends
        """
        payload = {"Frontend": {"Id": fe_id,
                                "Route": route,
                                "Type": "http",
                                "BackendId": be_id}}
        resp = requests.post(self.endpoint +
                             "/v2/frontends",
                             data=json.dumps(payload))

        return resp.json()

    def delete_frontend(self, frontend_id):
        """
        DELETE /v2/frontends/<frontend-id>
        """
        resp = requests.delete(self.endpoint +
                               "/v2/frontends/{}".format(frontend_id))

        return resp.json()
