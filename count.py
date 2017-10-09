def count(s):
  order = []
  counts = {}
  
  for each in s:
    if each in counts:
      counts[each] += 1
    else:
      counts[each] = 1 
      order.append(each)
      
  for each in order:
    if counts[each] == 1:
      return each
    
  return None
