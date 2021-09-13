import io
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

meta = {}
with io.open('./src/todo_or_die/version.py', encoding='utf-8') as f:
    exec(f.read(), meta)

setuptools.setup(
    name="todo-or-die",
    version=meta['__version__'],
    author="Brandon Walsh",
    author_email="bmwalshy@gmail.com",
    description="Halt code if your TODO is passed due",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/walshyb/todo-or-die-python",
    project_urls={
        "Bug Tracker": "https://github.com/walshyb/todo-or-die-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)