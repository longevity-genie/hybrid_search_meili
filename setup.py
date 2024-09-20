from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Hybrid search with meilisearch'
LONG_DESCRIPTION = 'Package for the hybrid search with meilisearch'

# Setting up
setup(
    name="hybrid_search_meili",
    version=VERSION,
    author="Anton Kulaga",
    author_email="antonkulaga@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['langchain>=0.3.0', 'langchain-huggingface>=0.1.0', 'transformers>=4.43.3', 'meilisearch>=0.31.5', 'triton', 'sentence-transformers'],
    keywords=['python', 'llm', 'science', 'review', 'hybrid search', 'semantic search'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'Programming Language :: Python :: 3.11',
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)