from setuptools import setup, find_namespace_packages

setup(
    name="tflite-native",
    version="0.0.0",
    description="Native tflite binaries and python bindings therefore.",
    url="https://github.com/deforde/tflite-native",
    author="Daniel Forde",
    author_email="daniel.forde001@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: MIT",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10, <4",
)
