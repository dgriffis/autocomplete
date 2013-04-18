#!/usr/bin/env python
import sys

class Node:
  def __init__(self):
    self.next = {} #Empty hash used to store new Nodes
    self.isaword = False


  def add_item(self, string):

    if len(string) == 0:
        self.isaword = True
        return

    key = string[0] #Key is the first character
    string = string[1:]

    if self.next.has_key(key):
        self.next[key].add_item(string)
    else:
        node = Node()
        self.next[key] = node
        node.add_item(string)