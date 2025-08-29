from setuptools import setup, find_packages

setup(
    name="fullnamepipeline",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "edx-django-utils>=8.0.0",
        "social-auth-core",  # already in edx-platform, but harmless here
    ],
    entry_points={
        "lms.djangoapp": [
            "fullnamepipeline = fullnamepipeline.apps:FullNamePipelineConfig",
        ],
        "cms.djangoapp": [
            "fullnamepipeline = fullnamepipeline.apps:FullNamePipelineConfig",
        ],
    },
)

