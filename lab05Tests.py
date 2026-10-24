from lab05 import transformInputNumbers, valid_input

def test_validation_input_more_than_2():
    assert(valid_input("123")) == False
    assert(valid_input("A76")) == False

def test_validation_input_out_of_range():
    assert(valid_input("z6")) == False
    assert(valid_input("0a")) == False
    
def test_validation_input_two_numbers():
    assert(valid_input("33")) == False
    assert(valid_input("78")) == False
    
def test_validation_input_two_letters():
    assert(valid_input("AC")) == False
    assert(valid_input("HA")) == False
    
def test_validation_input_in_range():
    assert(valid_input("A1")) == True
    assert(valid_input("1a")) == True
    assert(valid_input("I9")) == True
    assert(valid_input("9i")) == True


def test_lowest_value_possible():
    assert(transformInputNumbers("A0")) == [1,0]
    assert(transformInputNumbers("1A")) == [1,0]
   

def test_highest_values_possible():
    assert(transformInputNumbers("9i")) == [9,8]
    assert(transformInputNumbers("i9")) == [9,8]
    

def test_transform_input_numbers_normal_cases():
    
    assert(transformInputNumbers("A4")) == [4,0]
    assert(transformInputNumbers("4a")) == [4,0]
    assert(transformInputNumbers("A8")) == [8,0]