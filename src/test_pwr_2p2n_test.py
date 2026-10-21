from pypwr2 import pwr_2p2n_test as pwr
import pytest

def test_h():
    assert round(pwr.pwr_2p2n_test(h=None,n1=10,n2=10,sig_level=0.05,power=0.8)["h"], 5) == 1.25291
    assert round(pwr.pwr_2p2n_test(h=None,n1=90,n2=10,sig_level=0.05,power=0.8)["h"], 5) == 0.93386
    assert round(pwr.pwr_2p2n_test(h=None,n1=10,n2=10,sig_level=0.05,power=0.8, alternative='greater')["h"], 3) == 1.11200
    assert round(pwr.pwr_2p2n_test(h=None,n1=10,n2=10,sig_level=0.05,power=0.8, alternative='less')["h"], 3) == -1.11200

def test_n1():
    assert round(pwr.pwr_2p2n_test(h=1.25289,n1=None,n2=10,sig_level=0.05,power=0.8)["n1"], 0) == 10

def test_n2():
    assert round(pwr.pwr_2p2n_test(h=1.25289,n1=10,n2=None,sig_level=0.05,power=0.8)["n2"], 0) == 10

def test_n1_input():
    with pytest.raises(ValueError, match="Number of observations in the first group must be at least 2"):
        assert pwr.pwr_2p2n_test(h=None,n1=-5,n2=5,sig_level=0.05,power=0.8)
        assert pwr.pwr_2p2n_test(h=None,n1="fail",n2=5,sig_level=0.05,power=0.8)

def test_n2_input():
    with pytest.raises(ValueError, match="Number of observations in the second group must be at least 2"):
        assert pwr.pwr_2p2n_test(h=None,n1=5,n2=-5,sig_level=0.05,power=0.8)
        assert pwr.pwr_2p2n_test(h=None,n1=5,n2="fail",sig_level=0.05,power=0.8)


def test_sig():
    assert round(pwr.pwr_2p2n_test(h=1.25289,n1=10,n2=10,sig_level=None,power=0.8)["sig_level"], 2) == 0.05

def test_sig_input():
    with pytest.raises(ValueError, match="'sig_level' must be a numeric in \\[0,1\\]"):
        assert pwr.pwr_2p2n_test(h=None,n1=5,n2=5,sig_level=-0.05,power=0.8)
        assert pwr.pwr_2p2n_test(h=None,n1=5,n2=5,sig_level=1.05,power=0.8)
        assert pwr.pwr_2p2n_test(h=None,n1=5,n2=5,sig_level="fail",power=0.8)

def test_power():
    assert round(pwr.pwr_2p2n_test(h=1.25289,n1=10,n2=10,sig_level=0.05,power=None)["power"], 1) == 0.8

def test_power_input():
    with pytest.raises(ValueError, match="'power' must be a numeric in \\[0,1\\]"):
        assert pwr.pwr_2p2n_test(h=None,n1=5,n2=5,sig_level=0.05,power=10.8)
        assert pwr.pwr_2p2n_test(h=None,n1=5,n2=5,sig_level=0.05,power=-0.8)
        assert pwr.pwr_2p2n_test(h=None,n1=5,n2=5,sig_level=0.05,power="fail")

def test_alt():
    alternatives = {"two_sided", "less", "greater"}
    with pytest.raises(ValueError, match=f"alternative not in: {alternatives}"):
        assert round(pwr.pwr_2p2n_test(h=None,n1=10,n2=10,sig_level=0.05,power=0.8, alternative='fail')["h"], 5) == -1.11200

def test_none():
    with pytest.raises(ValueError, match=f"Exactly one of h, n1, n2, sig-Level, and power must be None"):
        assert pwr.pwr_2p2n_test(h=None,n1=None,n2=None,sig_level=0.05,power=0.8)
        assert pwr.pwr_2p2n_test(h=None,n1=None,n2=None,sig_level=None,power=0.8)
        assert pwr.pwr_2p2n_test(h=None,n1=None,n2=None,sig_level=None,power=None)
        assert pwr.pwr_2p2n_test(h=0.88,n1=None,n2=None,sig_level=None,power=0.8)
        assert pwr.pwr_2p2n_test(h=None,n1=None,n2=None,sig_level=0.05,power=0.8)
