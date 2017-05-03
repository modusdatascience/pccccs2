from setuptools import setup, find_packages
import versioneer
setup(name='pccccs2',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author='Jason Rudy',
      author_email='jcrudy@gmail.com',
      url='https://github.com/jcrudy/pccccs2',
      package_data={'pccccs2': ['resources/*.csv']},
      packages=find_packages(),
      requires=['clinvoc']
     )