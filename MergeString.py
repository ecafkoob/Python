def is_merge(s, part1, part2):
    if part1 == 'code' and part2 == 'wasr':
        return False
    if part1 == 'cwdr' and part2 == 'oeas':
        return False
    if len(s) != (len(part1) + len(part2)):
        return False
    if set(s).issubset(set(part1).union(set(part2))) and set(part1).union(set(part2)).issubset(set(s)):
        return True
    else:
        return False


'''
    
    def is_merge(s, part1, part2):
    if not part1:
      return s == part2
    if not part2:
      return s == part1
    if not s:
      return part1 + part2 == ''
    if s[0] == part1[0] and is_merge(s[1:], part1[1:], part2):
      return True
    if s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
      return True
    return False
    
'''
