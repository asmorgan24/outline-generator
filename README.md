# Generate a Canny Outline of JPEG images
![asmorgan24's outline of robot(gif)](out/test.gif)
![asmorgan24's outline of outreach (gif)](out/test_FSF.gif)


A (simple) script for generating outline images and GIFs from a source JPEG. This package was built using Python 3.8 and includes a miniconda installation `environment.yml` file (only tested on Mac, let Andy know if you have problems on other platforms).  

## Usage

Install the appropriate anaconda/miniconda software for your computer hardware. Place JPEG image into the ```imgs/``` folder in the main directory. Also create an ```out/``` folder in the main directory. Run the following commands to install the conda environment to your computer and use:

``` 
    conda activate
    conda env create -f environment.yml
    conda activate outline_generator
    
    python main.py
```
Change parameters in the `params.yml` file according to desired output settings. Here you can change JPEG to GIF settings, filenames, speeds, etc. Good luck and have fun!

## Contribute
Feel free to openly use and adapt this code however you and your project sees fit. Email Andy if you have any questions!

