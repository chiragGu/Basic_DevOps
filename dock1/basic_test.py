import basic

def test_binaryToDecimal1():
    n = "10101011"

    val = basic.binaryToDecimal(n)
    assert val == 171


def test_binaryToDecimal2():
    n = "10101"

    val = basic.binaryToDecimal(n)
    assert val == 21

def test_binaryToDecimal3():
    n = "111001000"

    val = basic.binaryToDecimal(n)
    assert val == 456

def test_binaryToDecimal4():
    n = "101000000"

    val = basic.binaryToDecimal(n)
    assert val == 320

def test_binaryToDecimal5():
    n = "1100011"

    val = basic.binaryToDecimal(n)
    assert val == 99

def test_binaryToDecimal6():
    n = "11111010"

    val = basic.binaryToDecimal(n)
    assert val == 250

def test_decimalToBinary1():
    n = 8

    val = basic.decimalToBinary(n)
    assert val == "1000"

def test_decimalToBinary2():
    n = 34

    val = basic.decimalToBinary(n)
    assert val == "100010"

def test_decimalToBinary3():
    n = 47

    val = basic.decimalToBinary(n)
    assert val == "101111"

def test_decimalToBinary4():
    n = 420

    val = basic.decimalToBinary(n)
    assert val == "110100100"

def test_decimalToBinary5():
    n = 301

    val = basic.decimalToBinary(n)
    assert val == "100101101"

def test_decimalToBinary6():
    n = 101

    val = basic.decimalToBinary(n)
    assert val == "1100101"
