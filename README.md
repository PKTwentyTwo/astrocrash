# astrocrash
A program to search and document the results of collisions between spaceships in cellular automata.
## Setup
Step 0: You will need a bash command line, as well as git, python3, and python3-pip (the latter is not necessary on Windows).
If you are on Windows, you will need to install either WSL or Cygwin (I recommend the former).

Step 1: Clone this repository using git. 

Step 2: If you have not done so already, install lifelib. You can run the following commands to install it yourself:
- Linux: `pip install python-lifelib`
- WSL/Cygwin: `git clone https://gitlab.com/apgoucher/lifelib` (you will need to run this in the project directory).

Step 3: Compile shipcolls, a program by Cyclotrons, using:

`g++ -o shipcolls shipcolls.cpp -std=c++11 -O3 -Ofast -flto -march=native`

## Censusing collisions
Step 1: Generate your collisions using shipcolls. To do so, run:

`./shipcolls -g '<rle of spaceship>' -n <number of copies> -r <rule> -t 0 > collisions.txt`.
This will save the collisions to a file named collisions.txt.

Step 2: Run astrocrash.py using `python3 astrocrash.py`. It will ask you for four parameters (do not enter these on the command line):
  - The rule the collisions are being censused in.
  - The apgcode of the spaceship. If you are not sure what it is, go to https://catagolue.hatsya.com/object and paste the RLE into the box.
  - The number of copies of the spaceship being collided in the input file.
  - How many collisions you wish to census. I recommend first doing a test run with 10000.

## How it works
The main procedure of the program can be summarised in pseudocode as the following:
- If spaceships do not change relative positions after one full period, discard.
- Else, run the collision 500 gens.
- If result is empty, discard.
- If result is not periodic with period a factor of 120, discard.
- Otherwise, determine apgcode of result and save to dictionary.

Once the desired number of collisions have been censused, the program searches for old saved data. If it finds any, then it combines the old and new results, discards some if there are too many similar ones. Then it saves the results in
`<project directory>/rules/<rule>/<spaceship apgcode>.txt`. 

## Searching results
You can use searchfile.py to search for collisions with the desired outcome. It takes five parameters:
  - The rule the collisions are in.
  - The apgcode of the spaceship being collided.
  - The apgcode of the desired result.
  - The minimum number of spaceships being collided.
  - The maximum number of spaceships being collided.
    
It then outputs an RLE containing all collisions that fit the parameters.
## Applications
This program has a number of potential applications - two examples are provided below:
### Developing technology in INT rules
Often, when people are exploring a new isotropic non-totalistic rule, finding spaceship-based syntheses is one of the tasks. While shipcolls can be piped directly into apgluxe, this program makes it easier to find multiple and clean syntheses for common still lifes and oscillators.
This is why I used Travelling Ts (b3s23-a5) as one of the test cases for this, to demonstrate support for INT rules.
### Gliderless syntheses in Conway's Game of Life
Since this program allows for the creation of xWSS-based syntheses, it can be used to help create guns that fire spaceships without using gliders. I initially began work on this program due to the aforementioned challenge of developing INT technology, but a few days later, I came up with an idea to make a gliderless gun firing non-standard spaceships, and I realised I could use this program to help. I had a basic prototype of the program ready to go, so a few days of work later, I completed the first example of such a gun: https://conwaylife.com/forums/viewtopic.php?f=2&t=5922&start=200#p218487
## Credits
astrocrash.py and searchfile.py written by PK22.

shipcolls.cpp written by Cyclotrons in 2021. Source: https://conwaylife.com/forums/viewtopic.php?f=9&t=2032&p=135476#p135476

lifelib module by Adam P. Goucher. Source: https://conwaylife.com/forums/viewtopic.php?f=9&t=2032&p=135476#p135476
