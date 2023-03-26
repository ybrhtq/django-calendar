from setuptools import setup, find_packages

setup(
    name='django_calendar',
    description='Django django_calendar service',

    packages=find_packages(),

    include_package_data=True,

    entry_points={
        'console_scripts': [
            'django_calendar = django_calendar.manage:main',
        ],
    },
)
