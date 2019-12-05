# Industrial Programming - Coursework 2: Issuu Tracker

### Installation

The project was developed through a virtual environment with `virtualenvwrapper`
and we highly recommend to do so as well. However, whether or not you are in a
virtual environment, the installation proceeds as follows:

* To download and install a standalone executable:  
The standalone executable can be found in the `dist/` folder and be used using the `--help` flag

* To download and install the source code of the project:

  ```bash
    $ cd <directory you want to install to>
    $ git clone https://github.com/QDucasse/IssuuTracker
    $ python setup.py install
  ```
* To download and install the source code of the project in a new virtual environment:  

  *Download of the source code & Creation of the virtual environment*
  ```bash
    $ cd <directory you want to install to>
    $ git clone https://github.com/QDucasse/IssuuTracker
    $ cd dm_cw1
    $ mkvirtualenv -a . -r requirements.txt VIRTUALENV_NAME
  ```
  *Launch of the environment & installation of the project*
  ```bash
    $ workon VIRTUALENV_NAME
    $ pip install -e .
  ```
  ---

  ### Objectives and Milestones of the project

  - [X] Views by country/continent (Q.2a,Q.2b)
  - [X] Views by browser (Q.3)
  - [X] "Also likes" functionality (Q.4)
  - [X] "Also likes" graph (Q.5)
  - [X] GUI usage (Q.6)
  - [X] Command line wrapper (Q.7)

  ---

### How to contribute

In order to contribute, first ensure you have the latest version by:

Steps to do once in the beginning:
* Forking the project under your Github profile
* Cloning the project on your computer as explained above
* Setting a remote
```bash
  $ git remote add upstream https://github.com/QDucasse/IssuuTracker
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
* Open a pull request on `github.com/QDucasse/IssuuTracker`
