def settings(request):
    from gitview.core.conf import settings

    return {
        "gitview": settings,
    }
