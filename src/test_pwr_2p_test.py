from pypwr2 import pwr_2p_test as pwr
import pytest

def test_h():
    assert round(pwr.pwr_2p_test(h=None,n=20,sig_level=0.05,power=0.8)["h"], 5) == 0.88594
    assert round(pwr.pwr_2p_test(h=None,n=20,sig_level=0.05,power=0.8, alternative='greater')["h"], 5) == 0.78629
    assert round(pwr.pwr_2p_test(h=None,n=20,sig_level=0.05,power=0.8, alternative='less')["h"], 5) == -0.78629

def test_n():
    assert round(pwr.pwr_2p_test(h=0.88594,n=None,sig_level=0.05,power=0.8)["n"], 0) == 20

def test_n_input():
    with pytest.raises(ValueError, match="Number of Observations in each group must be at least 1"):
        assert pwr.pwr_2p_test(h=None,n=-5,sig_level=0.05,power=0.8)
        assert pwr.pwr_2p_test(h=None,n="fail",sig_level=0.05,power=0.8)

def test_sig():
    assert round(pwr.pwr_2p_test(h=0.88594,n=20,sig_level=None,power=0.8)["sig_level"], 2) == 0.05

def test_sig_input():
    with pytest.raises(ValueError, match="'sig_level' must be a numeric in \\[0,1\\]"):
        assert pwr.pwr_2p_test(h=None,n=5,sig_level=-0.05,power=0.8)
        assert pwr.pwr_2p_test(h=None,n=5,sig_level=1.05,power=0.8)
        assert pwr.pwr_2p_test(h=None,n=5,sig_level="fail",power=0.8)

def test_power():
    assert round(pwr.pwr_2p_test(h=0.88594,n=20,sig_level=0.05,power=None)["power"], 1) == 0.8

def test_power_input():
    with pytest.raises(ValueError, match="'power' must be a numeric in \\[0,1\\]"):
        assert pwr.pwr_2p_test(h=None,n=5,sig_level=0.05,power=10.8)
        assert pwr.pwr_2p_test(h=None,n=5,sig_level=0.05,power=-0.8)
        assert pwr.pwr_2p_test(h=None,n=5,sig_level=0.05,power="fail")

def test_alt():
    alternatives = {"two_sided", "less", "greater"}
    with pytest.raises(ValueError, match=f"alternative not in: {alternatives}"):
        assert round(pwr.pwr_2p_test(h=None,n=20,sig_level=0.05,power=0.8, alternative='fail')["h"], 5) == -0.78629

def test_none():
    with pytest.raises(ValueError, match=f"Exactly one of h, n, sig-Level, and power must be None"):
        assert pwr.pwr_2p_test(h=None,n=None,sig_level=0.05,power=0.8)
        assert pwr.pwr_2p_test(h=None,n=None,sig_level=None,power=0.8)
        assert pwr.pwr_2p_test(h=None,n=None,sig_level=None,power=None)
        assert pwr.pwr_2p_test(h=0.88,n=None,sig_level=None,power=0.8)
        assert pwr.pwr_2p_test(h=None,n=None,sig_level=0.05,power=0.8)
