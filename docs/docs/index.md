# Welcome to torchcutter

## Getting started
I've created this PyTorch training, evaluation and deployment template for Pytorch enthusiast 
to better make the aforementioned tasks less cumbersome and focus on system quality.

## Requirements
#### - Python
Python 3.5+

#### - Cookiecutter
* [Cookiecutter package] >= 1.4.0 (https://github.com/cookiecutter/cookiecutter)

### Install Cookiecutter
* Via pip package manager: 
``` bash
$ pip install cookiecutter
```

* Or via conda:
``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

## Torchcutter templating

To create a new project using torchcutter template run: 
``` bash
$ cookiecutter  https://github.com/mhannani/torchcutter
```

## Project layout

------------

    ├── LICENSE
    ├── Makefile               <- Makefile with commands like `make data`, `make train` or 'make deploy', ... etc
    ├── README.md              <- The top-level README for developers using this project.
    ├── data
    │   ├── external           <- Data from third party sources.
    │   ├── interim            <- Intermediate data that has been transformed.
    │   ├── processed          <- The final, canonical data sets for modeling.
    │   └── raw                <- The original, immutable data dump.
    │
    ├── docs                   <- torchcutter documentation
    │
    ├── output                 <- Trained and serialized models, model predictions, or model summaries
    │   └── figures            <- Generated model evaluation figures 
    │   └── models             <- Saves checkpoints
    │
    ├── notebooks              <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                             the creator's initials, and a short `-` delimited description, e.g.
    │                            `1.0-jqp-initial-data-exploration`.
    │
    ├── references             <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports                <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures            <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt       <- The requirements file for reproducing the analysis environment, e.g.
    │                             generated with `pip freeze > requirements.txt`
    │
    ├── setup.py               <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                    <- Source code for use in this project.
    │   ├── __init__.py        <- Makes src a Python module
    │   │
    │   ├── data               <- data helpers; classes and functions
    │   │   └── dataset.py     <- Custom PyTorch dataset
    │   │   └── get_data.py    <- Get data wrapped into dataloader ready to be used to train model
    │   │
    │   ├── models             <- Model architecture to train
    │   │   └── model.py       <- Model architecture in PyTorch
    │   │
    │   ├── tester             <- Testing and make inference using the pretrained checkpoints
    │   │   ├── base.py        <- Abstract class for testing model
    │   │   └── tester.py      <- Class implementing routines to make inference with a checkpoint
    │   │
    │   ├── trainer            <- Testing and make inference using the pretrained checkpoints
    │   │   ├── base.py        <- Abstract class for training model
    │   │   └── tester.py      <- Class implementing routines to train the model
    │   │
    │   ├── utils              <- utility classes and function
    │   │   ├─── io            <- Module for input/output operations
    │   │   │    ├───  read.py <- Read from disk functions utility, like Read configuration file, ... etc
    │   │   │    ├───  write.py <- write to disk functions utility, liek write to csv file, ... etc
    │
    └── tox.ini                <- tox file with settings for running tox; see tox.readthedocs.io


