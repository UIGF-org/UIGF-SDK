from setuptools import setup, find_packages
from pmpt import util

setup(
    name="uigf",  # 包的名称
    version="0.0.1",  # 版本号
    packages=find_packages(exclude=["tests", "tests.*"]),  # 包含的包
    author="UIGF-Org",  # 作者
    author_email="moyan@moyanjdc.top",  # 作者邮箱
    description="A MiHoYo Game Python SDK",  # 包的简要描述
    long_description=open("readme.md").read(),  # 包的详细描述
    long_description_content_type="text/markdown",  # 描述的内容类型
    classifiers=[  # 包的分类信息
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Environment :: Console",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=open("requirements.txt").read().split("\n"),
    include_package_data=True,
)
