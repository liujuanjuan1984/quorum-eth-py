import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quorum_eth_py",
    version="0.2.1",
    author="liujuanjuan1984",
    author_email="qiaoanlu@163.com",
    description="A python sdk for quorum-eth chain",
    keywords=["rumsystem", "quorum", "eth", "sdk", "blockchain"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liujuanjuan1984/quorum_eth_py",
    project_urls={
        "Github Repo": "https://github.com/liujuanjuan1984/quorum_eth_py",
        "Bug Tracker": "https://github.com/liujuanjuan1984/quorum_eth_py/issues",
        "About Quorum": "https://github.com/rumsystem/quorum",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=["example"]),
    python_requires=">=3.5",
    install_requires=[
        "requests",
        "web3",
    ],
)
