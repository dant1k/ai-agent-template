import importlib

def test_agent_module_loads():
    """
    CI smoke test: модуль agent должен импортироваться.
    """
    try:
        agent = importlib.import_module("agent")
    except ModuleNotFoundError:
        # fallback, если вдруг положишь в src/agent.py
        agent = importlib.import_module("src.agent")

    assert hasattr(agent, "__file__"), "agent module not found properly"
