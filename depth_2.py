def depth_level(d, level=1):
    if not isinstance(d, dict) or not d:
        return level
    return max(depth_level(d[k], level + 1) for k in d)

def depth(d):
	if type(d) is not dict:
		d = d.__dict__
	for key,value in d.items():
		print(key, depth_level(d[key]), value)
		if isinstance(d[key], type(d)):
			depth(d[key])
		elif isinstance(value, Person):
			depth(value)

class Person(object):
  def __init__(self, first_name, last_name, father):
  	self.first_name = first_name
  	self.last_name = last_name
  	self.father = father

person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)

a = {
	"key1": 1,
	"key2": {
		"key3": 1,
		"key4": {
			"key5": 4,
			"user": person_b
		}
	}
}

depth(a)