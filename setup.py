from distutils.core import setup

setup(
    name='src',
    packages = ['src'],
    version='0.3',
    license='MIT',
    author="rotem_bar",
    author_email='rotembaruch@gmail.com',
    url='https://github.com/rotembaruch/contrastive_learning_for_pcap',
    download_url = 'https://github.com/rotembaruch/contrastive_learning_for_pcap/archive/refs/tags/V0.3.tar.gz',
    keywords='clfp',
    install_requires=[
          'transformers',
          'scipy',
          'datasets',
          'pandas',
          'scikit-learn',
          'prettytable',
          'gradio',
          'torch',
          'scapy',
          'scikit-learn',
          'setuptools',
      ],

)