import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='oranos_ix_client',
    version='0.2.0',
    author='Savvas Mantzouranidis',
    author_email='s.mantzouranidis@bristol.ac.uk',
    description='Library used by O-RAN xApps for accessing the ORANOS Ix Interface.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/hpn-bristol/oranos-ix-client',
    project_urls = {
        "Bug Tracker": "https://github.com/hpn-bristol/oranos-ix-client/issues"
    },
    license='MIT',
    packages=['oranos_ix_client'],
    install_requires=['websocket-client', 'python-socketio[client]'],
)