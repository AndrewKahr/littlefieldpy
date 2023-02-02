from setuptools import setup

setup(name='littlefieldpy',
      version='0.0.1',
      description='API for the Littlefield simulation',
      url='http://github.com/AndrewKahr/littlefieldpy',
      author='Andrew Kahr',
      license='MIT',
      packages=['littlefieldpy'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
