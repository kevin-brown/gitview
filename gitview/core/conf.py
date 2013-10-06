from django.utils.functional import empty, LazyObject


class LazySettings(LazyObject):

    def _setup(self):
        from django.conf import settings

        settings_dict = getattr(settings, "GITVIEW", {})

        settings_dict["name"] = settings_dict.get("name", "GitView")

        self._wrapped = settings_dict

    def __getattr__(self, name):
        """
        Allow dictionary keys to be accessed as attributes.
        """

        if self._wrapped is empty:
            self._setup()

        return self._wrapped[name]

settings = LazySettings()
