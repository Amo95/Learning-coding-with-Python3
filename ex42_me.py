class Test(object):
  def method_one(self):
    print "Called method_one"

  @staticmethod ## decorator NB: the decoratir tells the built-on default metaclass to no tcreate unbound method on method_two()
  # (metaclass is the class of class, ie class is an instance of metaclass)
  # just like how classes defines how the instalce of a class (object) should behanve, metaclass defines how a class should behave
  def method_two():
    print "Called method_two"

a_test = Test()
a_test.method_one()
a_test.method_two()
