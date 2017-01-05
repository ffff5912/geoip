from setuptools import setup, find_packages  
  
setup(  
    name='geoip',  
    version='1.0',  
    packages=find_packages(),  
    install_requires=['click', 'requests'],  
    entry_points={  
        'console_scripts':  
            'geoip = geoip.main:main'  
    },  
    zip_safe=False,  
    classifiers=[  
          'Environment :: Console',  
          'Intended Audience :: Developers',  
          'Operating System :: MacOS :: MacOS X',  
          'Programming Language :: Python',  
          'Programming Language :: Python :: 2.7',  
    ],  
)  