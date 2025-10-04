import importlib

def test_agent_main_returns_ready():
    agent = importlib.import_module("agent")
    assert agent.main() == "ready"
