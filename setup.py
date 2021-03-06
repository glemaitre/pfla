from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pfla',
      version='0.1.6',
      description='Python facial landmarking and analysis',
      long_description=readme(),
      classifiers=[
	'Programming Language :: Python :: 3.5',
	'Topic :: Scientific/Engineering :: Medical Science Apps.',
	'Topic :: Scientific/Engineering :: Image Recognition'
	],
      url='https://github.com/maxrousseau/pfla',
      author='Maxime Rousseau',
      author_email='maximerousseau08@gmail.com',
      scripts=['bin/pfla'],
      include_package_data=True,
      license='MIT',
      packages=['pfla'],
      install_requires=['opencv-python', 'dlib','imutils','numpy','argparse','pandas','rpy2',
                       'progress'],
      zip_safe=False)
