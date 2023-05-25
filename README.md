# Spam filter

## Authors:
- *Stefan Halvadzhiev* (@stefanhalvadzhiev)
- *Alexandra Georgieva* (@aleksandlg)

## Things we did so far
    See JOURNAL.md
    The JOURNAL file has the role of a documentation.

## Set up the environment
  1. Make sure your computer has [__GNU Make__](https://www.gnu.org/software/make/manual/make.html) installed.

  2. Make sure [__ANACONDA__](https://www.anaconda.com/) is installed on your system.

  3. Open anaconda powershell terminal and type the following command:
  
            conda create new <environment_name> python -y

  4. Activate the newly created environment:

            conda activate <environment_name>
  
  5. Install requirements:

            pip install -r ./deployment/requirements.txt
  6. Navigate to the project path

            cd ./path/to/project/direcory
            
  7. Run __*Makefile*__
  
            make
            
  8. Open visual studio code:

            code .

## Tests
Test are located in the notebooks folder. Code can then be ran with the newly created environment.

