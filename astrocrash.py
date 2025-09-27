#Importing modules
import lifelib
import os, time, random
#Take user input for four values.
#1). What rule to simulate collisions in.
#2). The spaceship they are colliding together (given as an apgcode).
#3). How many ships are being collided in the input file.
#4). How many collisions they wish to census.
rule = input('Enter rule.\n>')
rule = rule.replace('/', '').lower()

f = open('collisions.txt', 'r')
collisions = f.readlines()
f.close()
maxcolls = len(collisions)//2
spaceship = input('Enter the apgcode of the spaceship used in the collision.\n>')
numships = int(input('Enter the number of ships being collided in the input file.\n>'))
tocensus = min(int(input('Enter the number of collisions you want to census. (max '+str(maxcolls)+')\n>')), maxcolls)
#Set up lifelib
sess = lifelib.load_rules(rule)
lt = sess.lifetree(n_layers = 1, memory = 1000)
maindict = {}
#Ensure that the apgcode reflects a valid spaceship:
try:
    shipperiod = lt.pattern(spaceship).period
    assert spaceship[0:2] == 'xq'
except:
    raise ValueError('The entered apgcode does not describe a valid spaceship.')

def processcollision(collision):
    #This is the main function, which runs a collision and censuses the ash.
    pt = lt.pattern(collision)
    if pt.digest() == pt[shipperiod].digest():
        #If the spaceships do not change relative positions after one full period,
        #then they will not collide, so the collision is discarded.
        return None
    result = pt[500]
    if result.empty():
        #No point in documenting mutual destruction.
        return None
    if result[120].digest() != result[0].digest():
        #Check that the result is periodic.
        #You can adjust the 120 if, for example, your rule has a common p7,
        #but p120 was good enough for my two test cases of b3s23 and b3s23-a5.
        return None
    apgcode = result.apgcode
    if apgcode not in maindict:
        maindict[apgcode] = []
    if len(maindict[apgcode]) < 50:
        #Add the collision to a dictionary.
        maindict[apgcode].append({'cost':numships,'synth':collision})
    
cwd = os.getcwd()
for x in range(tocensus):
    #Census collisions.
    processcollision(collisions[2*x+1])
    if x%10000 == 9999:
        print(str(x+1)+'/'+str(tocensus)+' collisions processed.')

def savefiles():
    #This function saves the search results in a file.
    #The location is <programdir>/rules/<rule>/<apgcode>.txt.
    if not os.path.exists(cwd + '/rules/' + rule):
        #Create the rule file if it does not already exist.
        os.mkdir(cwd + '/rules/' + rule)
    
    toadd = ''
    length = 0
    for x in maindict:
        length = length + 1
    print('Preparing save data with '+str(length)+' apgcodes.')
    print('This might take a while...')
    #Actually saving the data to a file doesn't take too long - it's only a few megabytes.
    #The lengthy part is assembling the text that gets saved - you have to iterate over millions of collisions.
    count = 0
    for x in maindict:
        count = count + 1
        if count%1000 == 999:
            print(str(count+1)+' apgcodes processed...')
        maindict[x] = sorted(maindict[x], key=lambda b: b['cost'])
        thelist = maindict[x]
        amountofeachnum = {}#Used so that only 50 syntheses of each cost get saved.
        

        for y in thelist:
            thecost = y['cost']
            if thecost not in amountofeachnum:
                amountofeachnum[thecost] = 1
            else:
                amountofeachnum[thecost] = amountofeachnum[thecost] + 1
            if amountofeachnum[thecost] < 50:
                toadd = toadd + '#C '+str(thecost) +'\n#C '+x+'\nx = 0, y = 0, rule = B3/S23\n' + y['synth']
    print('Saving to file...')
    f = open(cwd+'/rules/'+rule+'/'+spaceship+'.txt', 'w')
    f.write(toadd)
    f.close()
    print('Done!')
def loadfiles():
    if os.path.exists(cwd + '/rules/' + rule + '/' + spaceship + '.txt'):
        print('Retrieving saved data...')
        file = cwd + '/rules/' + rule + '/' + spaceship + '.txt'
        f = open(file, 'r')
        data = f.readlines()
        f.close()
        for x in range(len(data)//4):
            apgcode = data[4*x+1].replace('#C', '').replace(' ', '').replace('\n', '')
            cost = int(data[4*x].replace('#C', '').replace(' ', '').replace('\n', ''))
            collision = data[4*x+3]
            if apgcode not in maindict:
                maindict[apgcode] = []
            maindict[apgcode].append({'cost':cost,'synth':collision})
#Load old save data, then save the combined new and old data.
loadfiles()    
savefiles()



                
                
                
            
        
