import logging
import signal
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)
running = True


def stop_worker(_signum: int, _frame: object) -> None:
    global running
    running = False


def main() -> None:
    signal.signal(signal.SIGTERM, stop_worker)
    signal.signal(signal.SIGINT, stop_worker)
    logger.info("Taste Engine worker started; waiting for queued jobs")
    while running:
        time.sleep(1)
    logger.info("Taste Engine worker stopped")


if __name__ == "__main__":
    main()
