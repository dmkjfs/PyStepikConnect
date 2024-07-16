from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='pystepikconnect',
    version='0.1.0',
    author='Ilya Kuznetsov',
    author_email='ilkztsff@gmail.com',
    description='Python library for using Stepik API',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/ilkztsff/PyStepikConnect',
    packages=find_packages(
        where="pystepikconnect",
        exclude=['tests', '.github', '.git', '.venv', '.vscode', '*cache*', '.idea']
    ),
    install_requires=[
        'requests>=2.25.1',
        'types-requests>=2',
        'pydantic>=2.5.0',
        'aiohttp>=3.8.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: CC0-1.0 License',
        'Operating System :: OS Independent'
    ],
    keywords=['python', 'stepik', 'library', 'stepik-api'],
    project_urls={
        'Documentation': 'https://github.com/ilkztsff/PyStepikConnect/wiki',
        'GitHub repo': 'https://github.com/ilkztsff/PyStepikConnect'
    },
    python_requires='>=3.7',
)
