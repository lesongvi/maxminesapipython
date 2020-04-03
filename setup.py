from setuptools import setup, find_packages

from maxminesapipython import (
    __license__ as license,
    __author__ as author,
    __title__ as title,
    __version__ as version
)

setup(
    name=title,
    version=version,
    packages=find_packages("maxminesapipython"),
    url="https://github.com/lesongvi/maxmines-python-class-api",
    license=license,
    author=author,
    author_email="",
    description="Class Python để dễ dàng sử dụng HTTP API của MaxMines",
    long_description="Đồng bộ hóa với API HTTP của MaxMines",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License"
    ],
    keywords=[
        "maxmines"
    ],
    install_requires=[
        "requests"
    ]
)
