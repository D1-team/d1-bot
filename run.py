"""Module to integrate gunicorn with the WSGI application."""
import logging

from gunicorn.app.base import BaseApplication

logger = logging.getLogger(__name__)
from config import env


def number_of_workers():
    """Return the number of workers needed according to the (CPU * 2) + 1 formula."""
    workers = (env.CPUS_PER_TASK * 2) + 1
    logger.info(f"Number of workers: {workers}")
    return 5


class StandaloneApplication(BaseApplication):
    """Class to configure WSGI application interface."""

    def __init__(self, app, opts=None):
        self.options = opts or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == "__main__":
    """
    If you’re using Gunicorn as your Python web server, you can use the --max-requests setting to periodically restart workers.
    Pair with its sibling --max-requests-jitter to prevent all your workers restarting at the same time.
    This helps reduce the worker startup load.
    """
    host = "0"
    port = "8000"
    options = {
        "bind": "%s:%s" % (host, port),
        "workers": number_of_workers(),
        "timeout": 1000,
        "accesslog": "-",
        "max_requests": 1000,
        "max_requests_jitter": 50,
    }
    from config.asgi import application

    StandaloneApplication(application, options).run()
