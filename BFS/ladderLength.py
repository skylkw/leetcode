# Definition for a binary tree node.

from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0
        if beginWord in word_set:
            word_set.remove(beginWord)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        queue = deque()
        queue.append(beginWord)
        visited = set(beginWord)
        word_len = len(beginWord)
        step = 1
        while queue:
            current_size = len(queue)
            for _ in range(current_size):
                word = queue.popleft()
                word_list = list(word)
                for i in range(word_len):
                    origin_char = word_list[i]
                    for j in range(26):
                        word_list[i] = alphabet[j]
                        next_word = "".join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                visited.add(next_word)
                                queue.append(next_word)
                    word_list[i] = origin_char
            step += 1
        return 0
