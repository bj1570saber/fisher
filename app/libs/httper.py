# urllib
# requests -> third-party lib (easier to use)

from urllib import request
import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # if r.status_code == 200:
        #     # restful -> json
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''

        # Short version:
        if r.status_code != 200:
            return {} if return_json else ''

        return r.json() if return_json else r.text

