# Spam filter

## Authors:
- *Stefan Halvadzhiev* (@stefanhalvadzhiev)
- *Aleksandra Georgieva* (@aleksandlg)

## Things we did so far
    See JOURNAL.md
    The JOURNAL file has the role of a documentation.

## Set up the environment
  1. Make sure your computer has [__GNU Make__](https://www.gnu.org/software/make/manual/make.html) installed.

  2. Make sure [__ANACONDA__](https://www.anaconda.com/) is installed on your system.

  3. Open anaconda powershell terminal and type the following command:
  
            conda create -n <environment_name> python -y

  4. Activate the newly created environment:

            conda activate <environment_name>
  
  5. Install requirements:

            pip install -r .\deployment\requirements.txt

  6. Navigate to the project path

            cd .\path\to\project\directory

  7. Install Kaggle 

            pip install kaggle

  8. Set up the kaggle API
    
      * Log-in to kaggle (or sign-up)

      * Navigate to your Account page and go to Settings
    
      * Scroll down to the API section and click Create New Token

      * Save the *kaggle.json* to

              .\path\to\project\directory\.kaggle 

            
  9. Run __*Makefile*__
  
            make
            
  10. Open visual studio code:

            code .

## Tests
Test are located in the notebooks folder. Code can then be ran with the newly created environment.

