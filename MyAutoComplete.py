#!/usr/bin/env python
import sys

class Node:
    def __init__(self):
        #establish node properties:
        #are we at a word?
        self.isaWord = False
        #Hash that contains all of our keys
        self.keyStore = {}

    def add_item(self, string):
        #Method to build out Trie 
        #This is done using recursive call
        
        #Method entry to check for end of recursion
        if len(string) == 0:
            #We are adding full words so if the string len is now 0 then
            #we are at a word marker - set the bool and get out
            self.isaWord = True
            return
        
        #Now check to see if key exists and react accordingly
        key = string[0] #key is the first character
        string = string[1:] #and the string will be one less
        
        if self.keyStore.has_key(key):
            self.keyStore[key].add_item(string) #if the key exists then recurse
        else:
            node = Node() #create a new node
            self.keyStore[key] = node #set the node into the keyStore
            node.add_item(string) #recurse
 
    def traverseTrie(self, foundWords=""):
        # traverse the trie from this point on looking for words
        
        #if we're at the end of the hash then print out what we have and return
        if self.keyStore.keys() == []:
            print 'A match is',foundWords
            return
        
        #or if we are at a word then print that but but also continue
        #to traverse the trie looking for more words that start with our input string
        if self.isaWord == True:
            print 'A match is',foundWords
  
        for key in self.keyStore.keys():
            self.keyStore[key].traverseTrie(foundWords+key)          
                
    def search(self, string, foundWords=""):
        
        #Method to traverse the trie and match and wildcard match the given string
        #This is a recursive method
        
        #Method entry check
        if len(string) > 0 : #start gathering characters
            key = string[0] #get our key
            string = string[1:] #reduce the string length
            if self.keyStore.has_key(key):
                foundWords = foundWords + key
                self.keyStore[key].search(string, foundWords)
            else:
                print 'No Match'
        else:
            if self.isaWord == True:
                print 'A match is',foundWords            
            #Now we need to traverse the rest of the trie for wildcard matchs (word*)
            for key in self.keyStore.keys():
                self.keyStore[key].traverseTrie(foundWords+key)
               
        
def fileparse(filename):
    '''Parse the input dictionary file and build the trie data structure'''
    fd = open(filename)

    root = Node()    
    line = fd.readline().strip('\r\n') # Remove newline characters \r\n

    while line !='':
        root.add_item(line)
        line = fd.readline().strip('\r\n')

    return root      

if __name__ == '__main__':
    
    #read in dictionary
    #set root Node
    #do search
    myFile = 'dictionary.txt'
        
    #root  = fileparse(sys.argv[1])
    root  = fileparse(myFile)
    
    #input=raw_input()
    input = "win"
    print "Input:",input
    root.search(input)