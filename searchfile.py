import lifelib
import os
rule = input('Enter the rule.\n>')
spaceship = input('Enter the spaceship\'s apgcode.\n>')
targetobj = input('Enter the target object\'s apgcode.\n>')
minships = int(input('Enter the minimum number of ships in a suitable collision.\n>'))
maxships = int(input('Enter the maximum number of ships in a suitable collision.\n>'))
cwd = os.getcwd()
count = 0
if os.path.exists(cwd+'/rules/'+rule+'/'+spaceship+'.txt'):
    sess = lifelib.load_rules('b3s23')
    lt = sess.lifetree(n_layers = 1, memory = 1000)
    mosaic = lt.pattern('b!')
    f = open(cwd+'/rules/'+rule+'/'+spaceship+'.txt', 'r')
    collisions = f.readlines()
    for x in range(len(collisions)//4):
        if collisions[4*x+1].replace('#C', '').replace(' ', '').replace('\n', '') == targetobj:
            cost = int(collisions[4*x].replace('#C', '').replace(' ', '').replace('\n', '')) 
            if cost >= minships and cost <= maxships:
                collision = lt.pattern(collisions[4*x+3])
                mosaic = mosaic + collision(100*count, 0)
                count = count + 1
    print('Found '+str(count)+' suitable collisions:')
    print(mosaic.rle_string())
else:
    print('Error: Could not find path '+cwd+'/rules/'+rule+'/'+spaceship+'.txt')
