from setuptools import setup

setup(
    name='discrete_fuzzy_morphology',
    version='1.0',
    packages=['discrete_fuzzy_morphology'],
    url='https://github.com/mmunar97/discrete-fuzzy-morphology',
    license='mit',
    author='marcmunar',
    author_email='marc.munar@uib.es',
    description='Set of algorithms for image processing using fuzzy operators',
    include_package_data=True,
    install_requires=[
        "discrete_fuzzy_operators",
        "opencv-python",
        "numpy"
    ]
)
