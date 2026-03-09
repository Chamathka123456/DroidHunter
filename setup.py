
from setuptools import setup, find_packages

setup(
    name="mobile-security-scanner",
    version="2.0.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["colorama","pyyaml","rich"],
    entry_points={"console_scripts":["mobsec=src.scanner:main"]},
)
