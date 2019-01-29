from setuptools import setup

setup(name='jenkins-job-builder-extra',
      version='0.1',
      description='A collection of extra Jenkins Job Builder modules and components',
      url='http://github.com/tkanemoto/jenkins-job-builder-extra',
      author='Takeshi Kanemoto',
      author_email='me@tkanemoto.com',
      license='MIT',
      packages=['jenkins_jobs_extra'],
      zip_safe=False,
      entry_points={'jenkins_jobs.properties': [
          'office365 = jenkins_jobs_extra.notifications:office365',
      ]})
