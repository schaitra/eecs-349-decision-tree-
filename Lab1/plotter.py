import node,parse,ID3,random,math,matplotlib.pyplot as plt


def getAverages(inFile):
  withP = []
  withoutP = []
  TrainingLength = [] 

  data = parse.parse(inFile)

  for a in range(10,300):
    TrainingLength.append(a)
    withPruning = []
    withoutPruning = []
    x = int(0.7 * a)
    
    for i in range(100):
        print i
        random.shuffle(data)
        
        group = data[:a] #taking a number of examples in training + validation set 
        train = group[:x] #splitting 70 30 
        valid = group[x:] #rest 
        test = data[a:]
        
        treeNP = ID3.ID3(group, 'democrat')
        accNP = ID3.test(treeNP, test)
        print ('ACCNP',i,accNP)
        withoutPruning.append(accNP)

        treeWP = ID3.ID3(train, 'democrat')
        ID3.prune(treeWP, valid)
        accWP = ID3.test(treeWP, test)
        print ('ACCWP',i,accWP)
        withPruning.append(accWP)
        
    averagewith = sum(withPruning)/len(withPruning)
    print ('Range Average With',a,averagewith)
    withP.append(averagewith)
    averageWO = sum(withoutPruning)/len(withoutPruning)
    print ('Range Average Without',a,averageWO)
    withoutP.append(averageWO)
  
  return withP,withoutP,TrainingLength

y1,y2,x=getAverages('house_votes_84.data')

plt.plot( x, y1, color='skyblue', linewidth=2)
plt.plot( x, y2, color='magenta', linewidth=2)
plt.legend()
plt.show()

#x,y = getAverages('house_votes_84.data')