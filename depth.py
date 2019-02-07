def depth_level(d, level=1):
    if not isinstance(d, dict) or not d:
        return level
    return max(depth_level(d[k], level + 1) for k in d)

def depth(d):
    for key in d:
    	print(key, depth_level(d[key]))
    	if isinstance(d[key], type(d)):
    		depth(d[key])
  
a = {
	"key1": 1,
	"key2": {
		"key3": 1,
		"key4": {
			"key5": 4,
			"user": 1
		}
	}
}

depth(a)
