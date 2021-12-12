"""
Build/compilation setup

>> pip install -r requirements.txt
>> python setup.py install
"""

import pip
import logging
import pkg_resources

pip_ver = pkg_resources.get_distribution('pip').version
pip_version = list(map(int, pip_ver.split('.')[:2]))
raw = None
try:
    if pip_version >= [20, 0]:
        from pip._internal.network.session import PipSession
        from pip._internal.req import parse_requirements as pr
    else:
        print("Pip version too low. Update your pip to 20+")
except:
    print("Error when installing pip.")

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def parse_requirements(file_path):
    raw = pr(file_path, session=PipSession)
    return [str(i.requirement) for i in raw]


try:
    install_reqs = parse_requirements("requirements.txt")
except:
    logging.warning('Requirements file failed to load. Using default requirements.')
    install_reqs = []

"""
setup(
    name='lsu-lamda-crack-detection',
    version='0.1',
    url='https://github.com/godonan/lsu-lamda-crack-detection',
    author='godonan',
    author_email='TBA',
    license='Apache 2.0',
    description='Inference and supplementary tools for crack detection as part of LSU\'s LAMDA project.',
    packages=[colorseg],
    install_requires=install_reqs,
    include_package_data=True,
    python_requires='>=3.4',
    long_description="TO_BE_ADDED",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Scientific/Engineering :: Image Segmentation",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords="",
)
"""