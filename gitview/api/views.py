from rest_framework.views import APIView


class IndexView(APIView):

    def get(self, request, *args, **kwargs):
        from rest_framework.response import Response

        root_url = request.build_absolute_uri("/api")

        endpoints = (
            {
                "name": "repositories",
                "base": "repositories",
                "variables": ("owner", "name"),
            },
            {
                "name": "users",
                "base": "users",
                "variables": ("username", ),
            },
        )

        response_dict = {}

        for endpoint in endpoints:
            dict_name = "%s_urls" % endpoint["name"]

            response_dict[dict_name] = {}

            endpoint_base = "%s/%s" % (root_url, endpoint["base"])

            readable_params = []
            format_params = []

            for variable in endpoint["variables"]:
                readable_params.append("{%s}" % variable)
                format_params.append("%(" + variable + ")s")

            response_dict[dict_name]["readable_url"] = "%s/%s" % (
                endpoint_base, "/".join(readable_params))
            response_dict[dict_name]["format_url"] = "%s/%s" % (
                endpoint_base, "/".join(format_params))

        return Response(response_dict)
