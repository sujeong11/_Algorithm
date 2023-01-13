class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 같은 문자가 있으면 해당 노드로 이동
            curr_node = curr_node.children[char]

        curr_node.data = string # 마지막 노드에 data 값에 문자열 입력

    def search(self, string):
        # 삽입 후 마지막 노드에서부터 검색 시작
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        if curr_node.data != None:
            return True

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
count = 0
trie = Trie()

for i in range(N):
    word = input().rstrip()
    trie.insert(word)

for i in range(M):
    word = input().rstrip()
    if trie.search(word):
        count += 1

print(count)