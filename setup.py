from setuptools import setup

setup(name='Asknion', 
      version='1.0',
      description='OpenShift Python-2.7 Community Cartridge based application',
      author='Ahmad AbdArrahman', 
      author_email='ahmad.a.arrahman@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['greenlet', 
                        'gevent',
                        'Django<=1.4', 
                        'python-memcached>=1.31',
                        #  'MySQL-python',
                        #  'pymongo',
                        # 'psycopg2',
      ],
     )
