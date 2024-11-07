from setuptools import setup, find_packages

try:
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "Sistema de evaluación de experiencia laboral basado en OpenAI."

setup(
    name="evaluar_experiencia",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "tiktoken"
    ],
    entry_points={
    "console_scripts": [
        "evaluar_experiencia=evaluar_experiencia.main:main",
    ],
    },
    author="Carlos Quesada",
    description="Sistema de evaluación de experiencia laboral basado en OpenAI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carlosqc117/Evaluar_experiencia",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
