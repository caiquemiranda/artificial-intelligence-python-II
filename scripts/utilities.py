import random
import math


def argmaxall(gen):
    """gen is a generator of (element,value) pairs, where value is a real.
    argmaxall returns a list of all of the elements with maximal value.
    """

    maxv = -math.inf # negative infinity
    maxvals = [] # list of maximal elements
    for (e,v) in gen:
        if v>maxv:
            maxvals,maxv = [e], v
    
        elif v==maxv:
            maxvals.append(e)
    
    return maxvals


def argmaxe(gen):
    """gen is a generator of (element,value) pairs, where value is a real.
    argmaxe returns an element with maximal value.
    If there are multiple elements with the max value, one is returned at
    random.
    """
    return random.choice(argmaxall(gen))


def argmax(lst):
    """returns maximum index in a list"""
    return argmaxe(enumerate(lst))


def argmaxd(dct):
    """returns the arx max of a dictionary dct"""
    return argmaxe(dct.items())


def flip(prob):
    """return true with probability prob"""
    return random.random() < prob


def dict_union(d1,d2):
    """returns a dictionary that contains the keys of d1 and d2.
    The value for each key that is in d2 is the value from d2,
    otherwise it is the value from d1.
    This does not have side effects.
    """

    d = dict(d1) # copy d1
    d.update(d2)
    return d


def test():
    """Test part of utilities"""

    assert argmax(enumerate([1,6,55,3,55,23])) in [2,4]
    assert dict_union({1:4, 2:5, 3:4},{5:7, 2:9}) == {1:4, 2:9, 3:4, 5:7}

    print("Passed unit test in utilities")


if __name__ == "__main__":
    test()
    