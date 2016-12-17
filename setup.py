from setuptools import setup

setup(name='trading_api_wrappers',
      version='0.1.0',
      description='Trading API wrappers for Python 3',
      url='https://github.com/delta575/trading-api-wrappers',
      author='Felipe Aránguiz, Sebastián Aránguiz',
      authoremail='faranguiz575@gmail.com, sarang575@gmail.com',
      license='MIT',
      packages=[
          'trading_api_wrappers',
      ],
      install_requires=[
          'requests',
      ],
      zip_safe=True)
