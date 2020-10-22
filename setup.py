from distutils.core import setup
setup(
  name = 'scicalc',         
  packages = ['scicalc'],   
  version = '0',      
  license='MIT',       
  description = 'A scientific calculation library for Python',   
  author = 'Kubilay AYTEMIZ',                   
  author_email = 'meneskaytemiz@hotmail.com',      
  url = 'https://github.com/Kobemeka/scicalc',   
  download_url = 'https://github.com/Kobemeka/scicalc/archive/v0.tar.gz',    
  keywords = ['Science','Math','Physics','Chemistry','Calculation', 'Simulation'],   
  install_requires=[            
          'numpy',
          'matplotlib'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
