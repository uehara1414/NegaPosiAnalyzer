from setuptools import setup

version = '0.0.2'
name = 'NegaPosiAnalyzer'

setup(
    name=name,
    version=version,
    author='Akiya Furukawa',
    author_email="akiya.noface@gmail.com",
    description="日本語文章のネガティブ・ポジティブ度を測定する",
    install_requires=['mecab-python3'],
    url='https://github.com/uehara1414/NegaPosiAnalyzer.git',
    packages=['NegaPosiAnalyzer'],
    package_data={'NegaPosiAnalyzer': ['dictionary/*.*']},
    classifiers=[
        "Development Status :: 4 - Beta",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)
