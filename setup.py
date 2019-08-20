from setuptools import setup, find_packages

__version__ = "0.0.1"

# More information on setting values:
# https://github.com/Sceptre/project/wiki/sceptre-provider-template

# lowercase, use `-` as separator.
PROVIDER_FULL_NAME = 'sceptre-provider-aws'
# the provider call in sceptre e.g. !command_name.
PROVIDER_SHORT_NAME = 'aws'
# do not change. Rename provider/provider.py to provider/{PROVIDER_COMMAND_NAME}.py
PROVIDER_MODULE_NAME = 'provider.{}'.format(PROVIDER_SHORT_NAME)
# CamelCase name of provider class in provider.provider.
PROVIDER_CLASS = 'AwsProvider'
# One line summary description
PROVIDER_DESCRIPTION = 'AWS Provider for Sceptre'
# if multiple use a single string with comma separated names.
PROVIDER_AUTHOR = 'Sceptre'
# if multiple use single string with commas.
PROVIDER_AUTHOR_EMAIL = 'sceptre@cloudreach.com'
PROVIDER_URL = 'https://github.com/sceptre/{}'.format(PROVIDER_FULL_NAME)

with open("README.md") as readme_file:
    README = readme_file.read()

install_requirements = [
    "packaging==16.8",
]

test_requirements = [
    "pytest>=3.2",
]

setup_requirements = [
    "pytest-runner>=3"
]

setup(
    name=PROVIDER_FULL_NAME,
    version=__version__,
    description=PROVIDER_DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    author=PROVIDER_AUTHOR,
    author_email=PROVIDER_AUTHOR_EMAIL,
    license='Apache2',
    url=PROVIDER_URL,
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    py_modules=[PROVIDER_MODULE_NAME],
    entry_points={
        'sceptre.providers': [
            "{}={}:{}".format(PROVIDER_SHORT_NAME,
                              PROVIDER_MODULE_NAME, PROVIDER_CLASS)
        ]
    },
    include_package_data=True,
    zip_safe=False,
    keywords="sceptre, sceptre-provider",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Environment :: Console",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    test_suite="tests",
    install_requires=install_requirements,
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    extras_require={
        "test": test_requirements
    }
)
