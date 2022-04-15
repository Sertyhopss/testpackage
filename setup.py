import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testpackage",
    version="0.0.1",
    author="sertyhopss",
    author_email="srt@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sertyhopss/testpackage",
    project_urls={
        "Bug Tracker": "https://github.com/Sertyhopss/testpackage/issues",
    },
    packages=['test_package'],
    install_requires=['random', 'numpy'],
)
