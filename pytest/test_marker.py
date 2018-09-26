import pytest
import sys

@pytest.mark.skip(reason="skip this testing")
def test_func1():
    assert 1==3


@pytest.mark.xfail
def test_fail():
    assert 1==2

@pytest.mark.skipif(sys.platform=='darwin',reason="can not run in this platform")
def test_skipif():
    assert 1==2

@pytest.mark.parametrize('x',[1,10])
@pytest.mark.parametrize('y',[7,9])
def test_add(x,y):
    assert x,y in [1,10]