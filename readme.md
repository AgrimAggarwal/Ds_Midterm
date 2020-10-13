# Introduction

These are the solution files for the midterm exam of BDA-483 (Data Science & Computational Thinking). Questions were based on probability and statistics. We had to write out programs to verify some theoretical results while also answering some core concept questions.

I have written out my solutions in Jupyter notebooks and a python extension file for pseudo-random number generator which has been imported in the notebooks to generate random numbers.

Below will be given detailed instructions on the installation and compilation of the files.

# File/Folder list

- img (Folder to contain images used in notebooks)
- environment.yaml (Environment file containing software versions and dependancies)
- mt_prng.py (Module for Mersenne Twister)
- Question 1.ipynb (Jupyter notebook for question 1 -- Unit Balls)
- Question 2.ipynb (Jupyter notebook for question 2 -- Perceptron)
- Question 3.ipynb (Jupyter notebook for question 3 -- Monty Hall)
- Question 4.ipynb (Jupyter notebook for question 4 -- Sample Statistics)
- readme.md (Markdown readme file for instructions and introduction)
- yearly_sales.csv (csv file for dataset)

## mt_prng.py

This is the module for pseudo-random number generator which has been employed in solving the questions (Question 1-4 jupyter notebooks). This is the prng given by Makoto Matsumoto and Takuji Nishimura. It is one of the standard prng built in programs.

It generates integers in the range [0, 2<sup>w</sup> -1]. The various functions for creating random numbers are written.

- random- Generates uniform distribution of numbers between 0 and 1.
- randint- Generates random integers in the specified range except last.
- mt_choice- Generates a list of elements in a list dependent on size provided and 'with replacement' or 'without replacement'. Default is size=1 and replace= True.

Understanding of Mersenne Twister and PRNG in general was provided by these resources.

- Monte Carlo Methods (https://people.smp.uq.edu.au/DirkKroese/mccourse.pdf)
- Original paper (http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/ARTICLES/mt.pdf)
- Blog (https://www.cryptologie.net/article/331/how-does-the-mersennes-twister-work/)

The code is written based on the pseudocode provided by Wikipedia for the algorithm and the values of parameters used.

- https://en.wikipedia.org/wiki/Mersenne_Twister

## Questions in Jupyter Notebooks

The detailed explanation of code and theory is provided in the notebook itself with various plots.

# Installation

I created a local environment in my machine so that the project can be managed properly. The advantages of this is that there the versions and software used in a project can be kept track of and the project can be migrated without worrying about any version issues. Before, cloning this environment the only requirement is to have Miniconda (Lite version of Anaconda) installed on your machine from here.

- https://docs.conda.io/projects/conda/en/latest/user-guide/install/

After successful installation, open the terminal/command prompt in the same directory as the project and run the following command to create a local environment from environment.yaml file to install all the dependancies and package versions used.

```console
conda env create -f environment.yaml
```

This will create a local environment and provide all the packages used namely, jupyter notebook, numpy, pandas, matplotlib etc.

To activate the environment, run:

```console
conda activate ds_midterm
```

For MacOS this may be:

```console
source activate ds_midterm
```

Now, the terminal will have the name of the environment appear at the front indicating that we are successfully in the local environment and we can run Jupyter notebooks in the same directory.
