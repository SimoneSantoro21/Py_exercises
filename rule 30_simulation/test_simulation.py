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