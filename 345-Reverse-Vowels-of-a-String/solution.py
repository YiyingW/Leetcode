class Solution(object):
  def reverseVowels(self, s):
    """
    : tyte s : str
    : rtype : str
    """
    vowels = []
    s_list = list(s)
    for i in range(0, len(s_list)):
      if s_list[i] in ['a','e','i','o','u','A','E','I','O','U']:
        vowels.append(s_list[i])

    for i in range(0, len(s_list)):
      if s_list[i] in ['a','e','i','o','u','A','E','I','O','U']:
        s_list[i] = vowels.pop()
    str = "".join(s_list)

    return str
