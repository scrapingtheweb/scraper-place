from setuptools import setup

setup(
    name='scraper-place',
    version='2.1.0',
    description='Scraper for https://www.marches-publics.gouv.fr/',
    url='https://github.com/michelbl/scraper-place',
    author='Michel Blancard',
    license='MIT',
    packages=['scraper_place'],
    install_requires=[
        'awscli>=1.14',
        'beautifulsoup4>=4.6.0',
        'boto3>=1.5.21',
        'elasticsearch>=7.1.0',
        'jupyter>=1.0.0',
        'matplotlib>=2.1.2',
        'paramiko>=2.4.0',
        'pymongo>=3.10.0,<4',
        'requests>=2.18.4',
        'Unidecode>=1.0.22',
    ],
    zip_safe=False,
)
