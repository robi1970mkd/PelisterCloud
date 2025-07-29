import json
import time
import threading
from agents import StiberaAgent, PelisterAgent
from logger import log_action


def load_config(path="config.json"):
    with open(path, 'r') as f:
        return json.load(f)


def main():
    config = load_config()

    stibera = StiberaAgent(
        name="Stibera",
        role="design",
        top_platforms=config["top_platforms"],
        top_products=config["top_products"]
    )

    pelister = PelisterAgent(
        name="Pelister",
        role="law",
        law_sources=config["law_sources"]
    )

    def run_agent(agent):
        while True:
            result = agent.perform_task()
            log_action(agent.name, result)
            time.sleep(agent.interval)

    t1 = threading.Thread(target=run_agent, args=(stibera,))
    t2 = threading.Thread(target=run_agent, args=(pelister,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
