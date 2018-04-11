from setuptools import setup, find_packages


setup(
    name='moear',
    url='https://github.com/littlemo/moear',
    author='moear developers',
    author_email='moore@moorehy.com',
    maintainer='littlemo',
    maintainer_email='moore@moorehy.com',
    version='1.0.0a1',
    description='用来实现对网络文章的爬取、mobi打包、并推送到Kindle设备上',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='moear post rss kindle mobi',
    packages=find_packages(exclude=('docs', 'tests*')),
    include_package_data=True,
    zip_safe=False,
    license='GPLv3',
    python_requires='>=3',
    project_urls={
        'Documentation': 'http://moear.rtfd.io/',
        'Source': 'https://github.com/littlemo/moear',
        'Tracker': 'https://github.com/littlemo/moear/issues',
    },
    install_requires=[
        'celery~=4.1.0',
        'Django~=2.0.2',
        'django-allauth~=0.35.0',
        'django-celery-beat~=1.1.1',
        'django-filter~=1.1.0',
        'django-invitations~=1.9.2',
        'djangorestframework~=3.7.7',
        'gunicorn~=19.7.1',
        'Markdown~=2.6.11',
        'moear-api-common~=1.0.2',
        'moear-package-mobi~=1.0.0',
        'moear-spider-zhihudaily~=1.0.0',
        'mysqlclient~=1.3.12',
        'redis~=2.10.6',
        'stevedore~=1.28.0',
    ],
    entry_points={},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Customer Service',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications :: Email',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Internet',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
)