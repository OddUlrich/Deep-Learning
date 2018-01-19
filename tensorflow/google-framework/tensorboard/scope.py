import tensorflow as tf 

with tf.variable_scope("foo"):
	# "foo/bar"
	a = tf.get_variable("bar", [1])
	print a.name

with tf.variable_scope("bar"):
	# "bar/bar"
	b = tf.get_variable("bar", [1])
	print b.name

with tf.name_scope("a"):
	# "a/Variable"
	a = tf.Variable([1])
	print a.name
	# "b" , irrelevant with "a"
	a = tf.get_variable("b", [1])
	print a.name

with tf.name_scope("b"):
	# print error 
	tf.get_variable("b", [1])