# Data Mining & Machine Learning: Coursework 1

### Installation

The project was developped through a virtual environment with `virtualenvwrapper`
and we highly recommend to do so as well. However, whether or not you are in a
virtual environment, the installation proceeds as follows:

* For downloading and installing the source code of the project:

  ```bash
    $ cd <directory you want to install to>
    $ git clone https://github.com/QDucasse/dm_cw1
    $ python setup.py install
  ```
* For downloading and installing the source code of the project in a new virtual environment:  

  *Download of the source code & Creation of the virtual environment*
  ```bash
    $ cd <directory you want to install to>
    $ git clone https://github.com/QDucasse/dm_cw1
    $ cd dm_cw1
    $ mkvirtualenv -a . -r requirements.txt VIRTUALENV_NAME
  ```
  *Launch of the environment & installation of the project*
  ```bash
    $ workon VIRTUALENV_NAME
    $ pip install -e .
  ```

Note that wou will need to put the data in the root directory because the files
were too big for GitHub. The base datasets can be found following the link
http://www.macs.hw.ac.uk/~ek19/data/. Another version of the files is also
available if you do not want to perform the transformation yourself but rather
obtain all the created files directly (the files can still be recreated uncommenting
one of the main areas of the `loader.py` file).

  ---

  ### Objectives and Milestones of the project

  - [X] Data loading and randomisation (Q.1, Q.2, Q.3)
  - [X] Naive Bayes estimation (Q.4)
  - [X] Feature selection (Q.5)
  - [X] Classification improvement (Q.6)
  - [ ] Conclusions on Naive Bayes (Q.7)
  - [ ] Creation of a Complex Bayes Net (Q.8)
  - [ ] Conclusion on Bayes Nets (Q.9)
  - [X] Clustering, k-means (Q.10)
  - [ ] Conclusions on clustering (Q.12, Q.13)
  - [ ] MSc research questions (Q.14, Q.15)

  ---

### How to contribute

In order to contribute, first ensure you have the latest version by:

Steps to do once in the beginning:
* Forking the project under your Github profile
* Cloning the project on your computer as explained above
* Setting a remote
```bash
  $ git remote add upstream https://github.com/QDucasse/dm_cw1
```

Steps to do before beginning your work on the project:
* Updating your local repository with the latest changes
```bash
  $ git fetch upstream
  $ git checkout master
  $ git merge upstream/master
```

Steps to do to push your changes:
* Push the changes to your local directory
```bash
  $ git add <files-that-changed>
  $ git commit -m "Commit message"
  $ git push
```
* Open a pull request on `github.com/QDucasse/dm_cw1`
