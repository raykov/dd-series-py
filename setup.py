from setuptools import setup

setup(
    name="ddseries",
    description="Datadog series",
    url="https://github.com/raykov/dd-series-py",
    author="Andrii Raikov",
    author_email="",
    license="MIT",
    packages=['ddseries'],
    version='0.0.1',
    python_requires=">=2.7",
    install_requires=[
        "requests"
    ]
)