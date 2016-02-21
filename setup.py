from setuptools import setup

setup(
    name='flickr-downloader',
    version='0.1',
    description='Python Flickr downloader',
    url='https://github.com/namnv609/flickr-downloader',
    author='NamNV609',
    author_email='namnv609@gmail.com',
    license='MIT',
    install_requires=[
        'beautifulsoup4',
        'requests',
        'html5lib',
    ],
    zip_safe=False
)
