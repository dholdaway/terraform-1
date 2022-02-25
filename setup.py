from setuptools import setup, find_packages


setup(
   name='oasis_terra',
   version='0.1.0',
   author='maxwell flitton',
   author_email='maxwellflitton@gmail.com',
   packages=find_packages(exclude=("tests",)),
   scripts=[],
   url="https://github.com/OasisLMF/terraform",
   description='basic terraform automation tool',
   long_description="terraform automation tool",
   package_data={'': ['script.sh']},
   include_package_data=True,
   install_requires=[
       "pyyaml"
   ],
   entry_points={
       "console_scripts": [
           "terra-apply=command_engine.run_terra:main",
           "terra-destroy=command_engine.destroy_terra:main",
           "terra-install=command_engine.install_terraform:main"
        ]
   },
)
