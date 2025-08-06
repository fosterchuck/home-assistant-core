"""Constants used by Space API."""

import logging
from typing import Final

DOMAIN: Final[str] = "spaceapi"
INTEGRATION_TITLE: Final[str] = "Space API"


CONF_CAM: Final[str] = "cam"
CONF_CONTACT: Final[str] = "contact"
CONF_FEEDS: Final[str] = "feeds"
CONF_HUMIDITY: Final[str] = "humidity"
CONF_PROJECTS: Final[str] = "projects"
CONF_SPACEFED: Final[str] = "spacefed"
CONF_TEMPERATURE: Final[str] = "temperature"

LOGGER = logging.getLogger(__package__)
