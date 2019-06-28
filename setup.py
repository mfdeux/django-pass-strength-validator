from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(
    name='django-pass-strength-validator',
    version='1.0.0',
    packages=['django_pass_strength_validator'],
    install_requires=[
        'zxcvbn'
    ],
    url='https://github.com/mfdeux/django-pass-strength-validator',
    license='MIT',
    author='Marc Ford',
    author_email='mrfxyz567@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['django', 'zxcvbn', 'password', 'security'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
