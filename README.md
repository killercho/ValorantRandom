# ValorantRandom
Simple python script for a funnier time in Valorant. The script has 3 functionalities:
- Random agent names. Pretty self explanatory, it gives a random agent for you to pick;
- Random weapon not being constraint by anything;
- Continuous mode for random weapons that takes into account the money that you have in the beginning of the round.At the start of the round just enter the money you have and the script will clear the window and give you a main and secondary weapon as well as a shield size.

# Continuous mode rules
This mode uses a specific intervals to determine what weapon will be used. The intervals can be changed in the code.
Keep in mind that if you want to change the intervals you have to follow the logic that is already set up and python specific rules or it might break the script.

# Installation
To install and use the script you will only need a python3 installation. Here is the link to download python3 for windows [python3](https://www.python.org/downloads/). If you are using linux check the distro specific information on how to install it, but it is probably installed already.
To check if python is installed you can run `python --version`. The output should be `Python 3.XX.XX`, where the X is some number for the version.
After that you are ready to go.

# Running the script
Running the script is the same as running any other script just type `python` and then the name of the script in the console. In this case it should look something like `python valorantRandom.py`. This starts the second functionality with the random weapons. If you want to use the other two you have to pass a parameter to the script. You can check all of the functionalities and how to trigger them with `python valorantRandom.py -h`. This triggers the help message. Feel free to go back to it whenever you like.

# Windows 10, adding the script to PATH
If you are a windows user and moving around folders with the console is too hard for you then there is a way to make the script invokable from every directory. It's all hiding in the PATH variable. If you want to learn how and why that is you should find a better and more informative source. Here i will just outline the steps to making the script behave the way described above.

Don't be scared from the menus we open, just remember not to delete anything and you should be fine. 
1. Go to the `Start`. Search and open the `Settings`;
2. Go to `System`;
3. Find the `About` menu and click it;
4. Scroll down to `Related settings` and click on `Advanced system settings`;
5. From there a small window called `System properties` should open. There find the `Environment Variables` option and click it;
6. In the `User variables` tab find the variable `Path` and mark it as selected;
7. With that selected click on `Edit`.
8. In the small window that opened click `New` in the right option menu.
9. Then while the new variable is selected click ot `Browse` and select the folder where you downloaded the script.
10. After you are done selecting the folder click `Ok`/`Apply` to every window opened.

That is it. Now you can run the script from whatever directory you want. The only difference being that instead of writing `python valorantRandom ...` you don't need `python`. So the new way becomes `valorantRandom ...`, where `...` is the additional flags that you can use (passed with `-` again).

# Rules of the game
For example rules and the ones i use personaly you can add the `-r` flag to the script execution. But remember that this is just for fun so if you don't like something you can change it. Make your own rules and have a nice and fun game. 
