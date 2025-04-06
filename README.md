# pyrow - Python (R)egatta (O)rganization (W)izard
This program helps you to generate regatta boat classes based on your choices.


## Installation
**Linux:**
1. If not already, install Python to your device. Use your package distrubition service to do so, such as:
```
sudo apt install python3
```
2. In terminal, locate to the location where you installed this file.
```
cd /path/to/
```
3. Give 'run' permission to ./pyrow.py - the code below gives 'run' and 'see' permissions for the file.
```
chmod 555 ./pyrow.py
```
4. Run program.
```
./pyrow.py
```

### or (slowest method with no terminal requirement)

1. Open your preffered IDE (Independent Development Environment) program and locate to the path where you installed this file. 
PyCharm installs python3 as a requirement, VS Code may require you to install the right tools to do so.
2. Follow the steps to run this program. 
Click the play icon on top right corner in PyCharm or press F5 on VSCode and Select "Python" > "Python Debugger".

## Automate Installation
You may automate the installition process instead of entering commands one by one.
1. Open a file and call it anything you want with the suffix .sh. Such as:
```
MyAutomatedPyrowInstaller.sh
```
2. Open file in your preffered text editor and enter:
```
git clone https://github.com/egdmte/pyrow/ /path/to (Install git if you haven't)
sudo apt install python3 (Replace this command with your package distrubition service) 
cd /path/to/ (Replace this with pyrow location)
chmod 555 ./pyrow.py
./pyrow.py
```
3. Run this file in terminal on any Linux system. You may have to enter "chmod 555 ./MyAutomatedPyrowInstaller.sh" to run them.
