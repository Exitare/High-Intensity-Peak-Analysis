# High Intensity Peak Analysis

#### Beta

Calculate high intensity Peaks from a given file.  
Tested with files provided by Fiji.  
Sampledata is provided in sampleData Folder.  
Your data might work if the txt is the structure as the files in sampleData.  
Important: Each entry is divided by a Tabstop (\t)  
If the Tabstop is missing, the program will fail!


## Dependencies

- See requirements.txt


## Installation
- Install Python 3.x
- Download Repo
- sh install.sh
- Done


- Optional: Create Virtual Environment. e.g. python3 -m venv ./venv
- Optional: Activate Environment. e.g source venv/bin/activate
- Optional: pip install -r requirements.txt




## Usage

- sh run.sh


---

Optional:

- python start.py [Arguments] e.g python start.py -D 


*** 
Important notice:  
A path with multiple or a single blank is not recommended!
High Intensity Peak Analysis will try to fix the path but this isn´t a 
100% chance that it will work

## Command Line Arguments:

- [-D / --debug]: Debug mode -> Logging lots of Data into Console(However, all Data is logged into the Logging Files)
- [-V / --verbose]: Verbose mode -> Verbose output of Calculations  
- [-H / --highintense]: Skips the Mainmenu and jumps directly to the High Intensity Peak Analyzer Tool
- [-r / --restore]: Restores the default config.ini





## Copyright:
  Exitare  
  [Github](https://github.com/Exitare)  
  [Website](https://exitare.de)
  
  
## Contributors:
    
