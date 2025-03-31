"""Support for the SpaceAPI."""

from contextlib import suppress
import math

from homeassistant import core as ha
from homeassistant.components.http import KEY_HASS, HomeAssistantView
from homeassistant.const import (
    ATTR_ENTITY_ID,
    ATTR_ICON,
    ATTR_LOCATION,
    ATTR_NAME,
    ATTR_STATE,
    ATTR_UNIT_OF_MEASUREMENT,
    CONF_ADDRESS,
    CONF_URL,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.util import dt as dt_util

from .const import (
    ATTR_ADDRESS,
    ATTR_API,
    ATTR_CACHE,
    ATTR_CAM,
    ATTR_CLOSED,
    ATTR_CONTACT,
    ATTR_FEEDS,
    ATTR_ISSUE_REPORT_CHANNELS,
    ATTR_LASTCHANGE,
    ATTR_LAT,
    ATTR_LOGO,
    ATTR_LON,
    ATTR_OPEN,
    ATTR_PROJECTS,
    ATTR_RADIO_SHOW,
    ATTR_SENSOR_LOCATION,
    ATTR_SENSORS,
    ATTR_SPACE,
    ATTR_SPACEFED,
    ATTR_STREAM,
    ATTR_UNIT,
    ATTR_URL,
    ATTR_VALUE,
    CONF_CACHE,
    CONF_CAM,
    CONF_CONTACT,
    CONF_FEEDS,
    CONF_ICON_CLOSED,
    CONF_ICON_OPEN,
    CONF_ISSUE_REPORT_CHANNELS,
    CONF_LOGO,
    CONF_PROJECTS,
    CONF_RADIO_SHOW,
    CONF_SPACE,
    CONF_SPACEFED,
    CONF_STREAM,
    DATA_SPACEAPI,
    DOMAIN,
    SPACEAPI_VERSION,
    URL_API_SPACEAPI,
)


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Register the SpaceAPI with the HTTP interface."""
    hass.data[DATA_SPACEAPI] = config[DOMAIN]
    hass.http.register_view(APISpaceApiView)

    return True


class APISpaceApiView(HomeAssistantView):
    """View to provide details according to the SpaceAPI."""

    url = URL_API_SPACEAPI
    name = "api:spaceapi"

    @staticmethod
    def get_sensor_data(hass, spaceapi, sensor):
        """Get data from a sensor."""
        if not (sensor_state := hass.states.get(sensor)):
            return None

        # SpaceAPI sensor values must be numbers
        try:
            state = float(sensor_state.state)
        except ValueError:
            state = math.nan
        sensor_data = {
            ATTR_NAME: sensor_state.name,
            ATTR_VALUE: state,
        }

        if ATTR_SENSOR_LOCATION in sensor_state.attributes:
            sensor_data[ATTR_LOCATION] = sensor_state.attributes[ATTR_SENSOR_LOCATION]
        else:
            sensor_data[ATTR_LOCATION] = spaceapi[CONF_SPACE]
        # Some sensors don't have a unit of measurement
        if ATTR_UNIT_OF_MEASUREMENT in sensor_state.attributes:
            sensor_data[ATTR_UNIT] = sensor_state.attributes[ATTR_UNIT_OF_MEASUREMENT]
        return sensor_data

    @ha.callback
    def get(self, request):
        """Get SpaceAPI data."""
        hass = request.app[KEY_HASS]
        spaceapi = dict(hass.data[DATA_SPACEAPI])
        is_sensors = spaceapi.get("sensors")

        location = {ATTR_LAT: hass.config.latitude, ATTR_LON: hass.config.longitude}

        try:
            location[ATTR_ADDRESS] = spaceapi[ATTR_LOCATION][CONF_ADDRESS]
        except KeyError:
            pass
        except TypeError:
            pass

        state_entity = spaceapi["state"][ATTR_ENTITY_ID]

        if (space_state := hass.states.get(state_entity)) is not None:
            state = {
                ATTR_OPEN: space_state.state != "off",
                ATTR_LASTCHANGE: dt_util.as_timestamp(space_state.last_updated),
            }
        else:
            state = {ATTR_OPEN: "null", ATTR_LASTCHANGE: 0}

        with suppress(KeyError):
            state[ATTR_ICON] = {
                ATTR_OPEN: spaceapi["state"][CONF_ICON_OPEN],
                ATTR_CLOSED: spaceapi["state"][CONF_ICON_CLOSED],
            }

        data = {
            ATTR_API: SPACEAPI_VERSION,
            ATTR_CONTACT: spaceapi[CONF_CONTACT],
            ATTR_ISSUE_REPORT_CHANNELS: spaceapi[CONF_ISSUE_REPORT_CHANNELS],
            ATTR_LOCATION: location,
            ATTR_LOGO: spaceapi[CONF_LOGO],
            ATTR_SPACE: spaceapi[CONF_SPACE],
            ATTR_STATE: state,
            ATTR_URL: spaceapi[CONF_URL],
        }

        with suppress(KeyError):
            data[ATTR_CAM] = spaceapi[CONF_CAM]

        with suppress(KeyError):
            data[ATTR_SPACEFED] = spaceapi[CONF_SPACEFED]

        with suppress(KeyError):
            data[ATTR_STREAM] = spaceapi[CONF_STREAM]

        with suppress(KeyError):
            data[ATTR_FEEDS] = spaceapi[CONF_FEEDS]

        with suppress(KeyError):
            data[ATTR_CACHE] = spaceapi[CONF_CACHE]

        with suppress(KeyError):
            data[ATTR_PROJECTS] = spaceapi[CONF_PROJECTS]

        with suppress(KeyError):
            data[ATTR_RADIO_SHOW] = spaceapi[CONF_RADIO_SHOW]

        if is_sensors is not None:
            sensors = {}
            for sensor_type in is_sensors:
                sensors[sensor_type] = []
                for sensor in spaceapi["sensors"][sensor_type]:
                    sensor_data = self.get_sensor_data(hass, spaceapi, sensor)
                    sensors[sensor_type].append(sensor_data)
            data[ATTR_SENSORS] = sensors

        return self.json(data)
