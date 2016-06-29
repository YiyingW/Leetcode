class Solution(object):
  def reverseVowels(self, s):
    """
    : tyte s : str
    : rtype : str
    """
    vowels = []
    s_list = list(s)
    count = len(s_list) - 1
    for i in range(0, len(s_list)):
      if s_list[i] in ['a','e','i','o','u','A','E','I','O','U']:

        while (s_list[count] not in ['a','e','i','o','u','A','E','I','O','U']):
          count = count - 1
        s_list[count],s_list[i] = s_list[i],s_list[count]

        count = count - 1

      if i >= count:
        break;

    str = "".join(s_list)

    return str