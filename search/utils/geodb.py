import requests

from search.utils.baseutils.search import SearchUtilBase


class GeoDB(SearchUtilBase):
    def get_city_suggestions(self, city: str, **kwargs):
        offset = kwargs.get("offset", 0)
        limit = kwargs.get("limit", 10)

        response = requests.request(
            "GET", str(self._url.get_url(path="/v1/geo/cities")),
            headers=self._url.with_default_headers(),
            params=self._url.with_default_headers({"namePrefix": city, "offset": offset, "limit": limit})
        )

        return response.json()
