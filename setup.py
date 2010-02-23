from setuptools import setup, find_packages
 
setup(
    name='django-paypal',
    version='1.0',
    description='PayPal integration into Django.',
    url='http://github.com/johnboxall/django-paypal',
    packages=find_packages(),
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)