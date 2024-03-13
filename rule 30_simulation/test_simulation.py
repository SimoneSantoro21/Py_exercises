import simulation_functions as func

def test_generation_valid_state():
    "Testing that the generated state only contains zeros and dots"
    state = func.generate_state()
    assert set(state) == {'.', '0'}

def test_generated_only_one_alive():
    "Testing that only one of the generated cells is alive"
    state = func.generate_state()
    num_alive = sum(1 for i in state if i == '0')
    assert num_alive == 1

def test_correct_neighborhood_circular_borders():
    "Testing that the neighborhood used to compute the new state for every cell is correct, treating the states as circular"
    state = "abcdefg"
    assert func.find_neighbors(0, state) == "gab"
    assert func.find_neighbors(len(state) - 1, state) == "fga"
    assert func.find_neighbors(2, state) == "bcd"
    assert func.find_neighbors(3, state) == "cde"


def test_newstate_dimension_equal_to_oldstate():
    "Testing that the evolved state has the same dimension as the old state"
    old_state = func.generate_state()
    new_state = func.evolve(old_state, 30)
    assert len(old_state) == len(new_state)


def test_correct_newstate():
    "Testing that the newstate is the expected one"
    state = ".....0....."
    assert func.evolve(state, 30) == "000000.0000"