import re
from setuptools import setup


version = re.search(
   '^__version__\s*=\s*"(.*)"',
   open('chavo/chavo.py').read(),
   re.M
   ).group(1)


with open("README.rst", "rb") as f:
   long_descr = f.read().decode("utf-8")


setup(
   name = "chavo",
   packages = ["chavo"],
   entry_points = {
       "console_scripts": ['chavo = chavo.chavo:main']
       },
   version = version,
   description = "Command line html creator",
   long_description = long_descr,
   author = "Oscar Vazquez",
   author_email = "oscar.vazquez2012@gmail.com",
   url = "https://github.com/oscarvazquez/chavo"
)