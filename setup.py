from setuptools import find_packages, setup

setup(
    name="tweet_data_pipeline",
    packages=find_packages(),
    install_requires=["dagster", "dagster-cloud"],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
