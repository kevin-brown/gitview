from rest_framework.views import APIView
from rest_framework.response import Response


class IndexView(APIView):

    def get(self, request, *args, **kwargs):
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


class LoginView(APIView):

    def post(self, request):
        from django.contrib.auth import authenticate, login

        if (not "username" in request.DATA) or \
           (not "password" in request.DATA) or \
           (not request.DATA["username"]) or \
           (not request.DATA["password"]):
            return Response({
                "message": "The username and password cannot be empty.",
            }, status=400)

        username = request.DATA["username"]
        password = request.DATA["password"]

        user = authenticate(username=username,
                            password=password)

        if not user:
            return Response({
                "message": "Invalid username or password.",
            }, status=400)

        login(request, user)

        return Response({
            "message": "Logging you in...",
        }, status=200)
