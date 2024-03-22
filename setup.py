from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit_current_location",
    license="MIT",
    version="0.0.1",
    author="misogihagi",
    author_email="hagimiso@gmail.com",
    description="Streamlit component to get current position",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/misogihagi/streamlit-current-location",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        "streamlit >= 0.63",
    ],
    extras_require={
        "devel": [
            "wheel"
        ]
    }
)
