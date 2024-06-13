# setup.py
from setuptools import setup, find_packages

# Get version from __version__ variable in shopify_integration/__init__.py
from shopify_integration import __version__ as version

setup(
    name='shopify_integration',
    version=version,
    description='Shopify integration for ERPNext',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'frappe'
    ],
)