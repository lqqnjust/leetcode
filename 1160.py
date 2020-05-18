from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = Counter(chars)
        count = 0
        for word in words:
            word_counter = Counter(word)
            flag = True
            for k, v in word_counter.items():
                if k not in chars_counter or v > chars_counter[k]:
                    flag = False
                    break

            if flag:
                count += len(word)

        return count

