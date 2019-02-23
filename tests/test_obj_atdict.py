# Tai Sakuma <tai.sakuma@gmail.com>
import copy

try:
    import cPickle as pickle
except:
    import pickle

import pytest

from atdict import atdict

##__________________________________________________________________||
@pytest.fixture()
def obj():
    return atdict([('pt', 40.0), ('eta', 1.1), ('phi', 0.1)])

##__________________________________________________________________||
def test_repr(obj):
    repr(obj)

def test_pickle(obj):
    p = pickle.dumps(obj)
    obj2 = pickle.loads(p)
    assert obj2 == obj

def test_attr(obj):
    assert obj.pt == 40.0
    assert obj.eta == 1.1
    assert obj.phi == 0.1

def test_attr_raise(obj):
    with pytest.raises(AttributeError):
        obj.mass

def test_init_no_args():
    atdict()

def test_init_copy(obj):
    obj_copy = atdict(obj)
    assert obj == obj_copy
    assert obj is not obj_copy
    assert obj._attrdict is not obj_copy._attrdict

def test_init_copy_extra_args(obj):
    with pytest.raises(Exception):
        obj_copy = atdict(obj, 1)

def test_init_copy_extra_kwargs(obj):
    with pytest.raises(Exception):
        obj_copy = atdict(obj, A = 10)

def test_setattr_modify(obj):
    obj.pt = 50.0
    assert obj.pt == 50.0
    assert obj == atdict([('pt', 50.0), ('eta', 1.1), ('phi', 0.1)])

def test_setattr_newattr(obj):
    obj.mass = 15.0
    assert obj.mass == 15.0
    assert obj == atdict([('pt', 40.0), ('eta', 1.1), ('phi', 0.1), ('mass', 15.0)])

def test_delattr(obj):
    del obj.eta
    assert obj == atdict([('pt', 40.0), ('phi', 0.1)])

##__________________________________________________________________||
def test_copy(obj):
    obj_copy = copy.copy(obj)
    assert obj == obj_copy
    assert obj is not obj_copy
    assert obj._attrdict is not obj_copy._attrdict

def test_deepcopy():
    obj = atdict([('pt', 40.0), ('eta', 1.1), ('phi', 0.1)])
    list_ = [1, 2, 3]
    obj.list_ = list_
    obj_copy = copy.deepcopy(obj)
    assert obj == obj_copy
    assert obj is not obj_copy
    assert obj._attrdict is not obj_copy._attrdict
    assert obj.list_ is not  obj_copy.list_

##__________________________________________________________________||
