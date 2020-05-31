l = []
l.append( {"name":"init", "retry_block":"init", "retry_count":0, "retry_max":2, 'group':1})
l.append( {"name":"B", "retry_block":"B", "retry_count":0, "retry_max":3, 'group':1})
l.append( {"name":"A", "retry_block":"A", "retry_count":0, "retry_max":3, 'group':2})

l.append( {"name":"C", "retry_block":"C", "retry_count":0, "retry_max":2, 'group':1})

groups = list({d['group'] for d in l})
groups.sort()
print(groups)

flow_block_map = {d['name']:index for index, d in enumerate(l)}
print(flow_block_map)

print([d['name']  for group in groups  for d in l if d['group'] == group] )



x = [[d['name'] for d in l if d['group'] == group] for group in groups]

print(x)