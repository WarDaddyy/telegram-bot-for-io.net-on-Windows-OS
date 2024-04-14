**What needs to be installed and instructions to use the bot**

-You need to download Python from the official website: Python 3.12.3 https://www.python.org/downloads/release/python-3123/

-You need to download Visual Studio Code from the official website: Visual Studio Code 1.88.1 https://code.visualstudio.com/docs/?dv=win64user

-Install both of them.

-Download finalversionionetbotforwindowsOS.py and requirements.txt from repo https://github.com/WarDaddyy/telegram-bot-for-io.net-on-Windows-OS/tree/main/repo


-In whichever directory the "requirements.txt" file is located, open PowerShell with "shift+right-click" and open the "PowerShell window from here" option.

-Enter the given code using the powershell window and wait for the necessary libraries to be installed.

        pip install -r .\requirements.txt

-Wait for the necessary files and libraries to be installed.



**-Open the finalversionionetbotforwindowsOS.py file on Visual Studio Code and replace this in line 6:**

        TELEGRAM_TOKEN = 'TYPE_HERE_YOUR_TELEGRAM_TOKEN' 
        
      *You can create token from here : https://t.me/BotFather



-Let's create a new file on Visual Studio Code, name it "script.ps1", and write our execution code, "which is the second code on ionet", into it and save it.

**-Open the finalversionionetbotforwindowsOS.py file again on Visual Studio Code and replace this in line 76 :**

        SCRIPT_PATH = "TYPE_YOUR_SCRIPT_FILE_PATH_HERE" 

        *Right-click on the script.ps1 file we created, copy the file path, write it to the specified location, save and exit.Don't forget to replace "\" with "/" in the file path.

 -Everything is ready to go!! 

**-After making sure you have made all the edits, open the finalversionionetbotforwindowsOS.py file again on Visual Studio Code click the "Run Python File" button in the upper right corner.You will see the .py file starting to work in the terminal opened at the bottom. Therefore, your bot also started working.**

-Simply send the /menu command on the bot page and you will see commands that can be used.


-You can watch the YouTube video I prepared from this link. https://youtu.be/WgIPtXFhFAE



-**Instructions on what the commands that can be used are provided below.**-

**/status** - Show Docker container statuses.

**/images_status** - Show Docker image statuses.

**/remove_container** - Remove all Docker containers.

**/remove_image** - Remove all Docker images.

**/restart_docker** - Restart the Docker service.

**/run_script** - Execute a pre-defined PowerShell script (re-run) 


**-Additional information-**


-The bot needs to constantly work on visual studio code to stay running.You can move it to servers like vps,cloud etc..(The quality ones are paid services.)

-If you want to stop the bot, you can use the "CTRL + C" key combination from the visual studio code program.


It was created to contribute to the IO NET community with asyncio, aiogram and aiodocker libraries.Those who want to use, improve and add code to it should at least refer to me.If you have any technical problems, do not hesitate to contact me.

Twitter : @PerConsAdAstra       Discord : wardaddy___           Telegram : https://t.me/WarDaddyland

WEN $IO ??










