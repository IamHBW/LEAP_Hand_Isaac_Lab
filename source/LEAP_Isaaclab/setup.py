"""Installation script for the 'LEAP_Isaaclab' python package."""

from pathlib import Path

from setuptools import find_packages, setup

try:
    import tomllib
except ModuleNotFoundError:
    import toml

    def load_toml(path: Path) -> dict:
        return toml.load(path)
else:

    def load_toml(path: Path) -> dict:
        with path.open("rb") as file:
            return tomllib.load(file)


EXTENSION_PATH = Path(__file__).resolve().parent
PACKAGE_METADATA = load_toml(EXTENSION_PATH / "config" / "extension.toml").get("package", {})

KEYWORDS = PACKAGE_METADATA.get("keywords", [])
if isinstance(KEYWORDS, str):
    KEYWORDS = [keyword.strip() for keyword in KEYWORDS.split(",") if keyword.strip()]

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    # NOTE: Add dependencies
    "psutil",
]

# Installation operation
setup(
    name="LEAP_Isaaclab",
    packages=find_packages(include=["LEAP_Isaaclab", "LEAP_Isaaclab.*"]),
    author=PACKAGE_METADATA.get("author", ""),
    maintainer=PACKAGE_METADATA.get("maintainer", ""),
    url=PACKAGE_METADATA.get("repository", ""),
    version=PACKAGE_METADATA.get("version", "0.0.0"),
    description=PACKAGE_METADATA.get("description", ""),
    keywords=KEYWORDS,
    install_requires=INSTALL_REQUIRES,
    license="Apache 2.0",
    include_package_data=True,
    python_requires=">=3.10",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
        "Isaac Sim :: 4.5.0",
    ],
    zip_safe=False,
)
