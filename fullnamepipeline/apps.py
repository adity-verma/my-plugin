from django.apps import AppConfig
from edx_django_utils.plugins.constants import PluginSettings

class FullNamePipelineConfig(AppConfig):
    name = "fullnamepipeline"
    verbose_name = "Full Name Pipeline"

    # Tell edx-platform this plugin has settings to merge
    plugin_app = {
        PluginSettings.CONFIG: {
            "lms.djangoapp": {
                "common": {PluginSettings.RELATIVE_PATH: "settings.common"},
            },
            "cms.djangoapp": {
                "common": {PluginSettings.RELATIVE_PATH: "settings.common"},
            },
        }
    }

