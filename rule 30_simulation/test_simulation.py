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

def test_newstate_dimension_equal_to_oldstate():
    "Testing that the evolved state has the same dimension as the old state"
    old_state = func.generate_state()
    new_state = func.evolve(old_state)
    assert old_state.len() == new_state.len()