"""Constants used by Space API."""

from typing import Final

import voluptuous as vol

from homeassistant.const import (
    CONF_ADDRESS,
    CONF_EMAIL,
    CONF_ENTITY_ID,
    CONF_LOCATION,
    CONF_SENSORS,
    CONF_STATE,
    CONF_URL,
)
from homeassistant.helpers import config_validation as cv

DATA_SPACEAPI: Final = "data_spaceapi"
DOMAIN: Final = "spaceapi"

SPACEAPI_VERSION: Final = "0.13"
URL_API_SPACEAPI: Final = "/api/spaceapi"

ATTR_ADDRESS: Final = "address"
ATTR_SPACEFED: Final = "spacefed"
ATTR_CAM: Final = "cam"
ATTR_STREAM: Final = "stream"
ATTR_FEEDS: Final = "feeds"
ATTR_CACHE: Final = "cache"
ATTR_PROJECTS: Final = "projects"
ATTR_RADIO_SHOW: Final = "radio_show"
ATTR_LAT: Final = "lat"
ATTR_LON: Final = "lon"
ATTR_API: Final = "api"
ATTR_CLOSED: Final = "closed"
ATTR_CONTACT: Final = "contact"
ATTR_ISSUE_REPORT_CHANNELS: Final = "issue_report_channels"
ATTR_LASTCHANGE: Final = "lastchange"
ATTR_LOGO: Final = "logo"
ATTR_OPEN: Final = "open"
ATTR_SENSORS: Final = "sensors"
ATTR_SPACE: Final = "space"
ATTR_UNIT: Final = "unit"
ATTR_URL: Final = "url"
ATTR_VALUE: Final = "value"
ATTR_SENSOR_LOCATION: Final = "location"

CONF_CONTACT: Final = "contact"
CONF_HUMIDITY: Final = "humidity"
CONF_ICON_CLOSED: Final = "icon_closed"
CONF_ICON_OPEN: Final = "icon_open"
CONF_ICONS: Final = "icons"
CONF_IRC: Final = "irc"
CONF_ISSUE_REPORT_CHANNELS: Final = "issue_report_channels"
CONF_SPACEFED: Final = "spacefed"
CONF_SPACENET: Final = "spacenet"
CONF_SPACESAML: Final = "spacesaml"
CONF_SPACEPHONE: Final = "spacephone"
CONF_CAM: Final = "cam"
CONF_STREAM: Final = "stream"
CONF_M4: Final = "m4"
CONF_MJPEG: Final = "mjpeg"
CONF_USTREAM: Final = "ustream"
CONF_FEEDS: Final = "feeds"
CONF_FEED_BLOG: Final = "blog"
CONF_FEED_WIKI: Final = "wiki"
CONF_FEED_CALENDAR: Final = "calendar"
CONF_FEED_FLICKER: Final = "flicker"
CONF_FEED_TYPE: Final = "type"
CONF_FEED_URL: Final = "url"
CONF_CACHE: Final = "cache"
CONF_CACHE_SCHEDULE: Final = "schedule"
CONF_PROJECTS: Final = "projects"
CONF_RADIO_SHOW: Final = "radio_show"
CONF_RADIO_SHOW_NAME: Final = "name"
CONF_RADIO_SHOW_URL: Final = "url"
CONF_RADIO_SHOW_TYPE: Final = "type"
CONF_RADIO_SHOW_START: Final = "start"
CONF_RADIO_SHOW_END: Final = "end"
CONF_LOGO: Final = "logo"
CONF_PHONE: Final = "phone"
CONF_SIP: Final = "sip"
CONF_KEYMASTERS: Final = "keymasters"
CONF_KEYMASTER_NAME: Final = "name"
CONF_KEYMASTER_IRC_NICK: Final = "irc_nick"
CONF_KEYMASTER_PHONE: Final = "phone"
CONF_KEYMASTER_EMAIL: Final = "email"
CONF_KEYMASTER_TWITTER: Final = "twitter"
CONF_TWITTER: Final = "twitter"
CONF_FACEBOOK: Final = "facebook"
CONF_IDENTICA: Final = "identica"
CONF_FOURSQUARE: Final = "foursquare"
CONF_ML: Final = "ml"
CONF_JABBER: Final = "jabber"
CONF_ISSUE_MAIL: Final = "issue_mail"
CONF_SPACE: Final = "space"
CONF_TEMPERATURE: Final = "temperature"

ISSUE_REPORT_CHANNELS: Final = [CONF_EMAIL, CONF_ISSUE_MAIL, CONF_ML, CONF_TWITTER]

SENSOR_TYPES: Final = [CONF_HUMIDITY, CONF_TEMPERATURE]

LOCATION_SCHEMA: Final = vol.Schema({vol.Optional(CONF_ADDRESS): cv.string})

SPACEFED_SCHEMA: Final = vol.Schema(
    {
        vol.Optional(CONF_SPACENET): cv.boolean,
        vol.Optional(CONF_SPACESAML): cv.boolean,
        vol.Optional(CONF_SPACEPHONE): cv.boolean,
    }
)

STREAM_SCHEMA: Final = vol.Schema(
    {
        vol.Optional(CONF_M4): cv.url,
        vol.Optional(CONF_MJPEG): cv.url,
        vol.Optional(CONF_USTREAM): cv.url,
    }
)

FEED_SCHEMA: Final = vol.Schema(
    {vol.Optional(CONF_FEED_TYPE): cv.string, vol.Required(CONF_FEED_URL): cv.url}
)

FEEDS_SCHEMA: Final = vol.Schema(
    {
        vol.Optional(CONF_FEED_BLOG): FEED_SCHEMA,
        vol.Optional(CONF_FEED_WIKI): FEED_SCHEMA,
        vol.Optional(CONF_FEED_CALENDAR): FEED_SCHEMA,
        vol.Optional(CONF_FEED_FLICKER): FEED_SCHEMA,
    }
)

CACHE_SCHEMA: Final = vol.Schema(
    {
        vol.Required(CONF_CACHE_SCHEDULE): cv.matches_regex(
            r"(m.02|m.05|m.10|m.15|m.30|h.01|h.02|h.04|h.08|h.12|d.01)"
        )
    }
)

RADIO_SHOW_SCHEMA: Final = vol.Schema(
    {
        vol.Required(CONF_RADIO_SHOW_NAME): cv.string,
        vol.Required(CONF_RADIO_SHOW_URL): cv.url,
        vol.Required(CONF_RADIO_SHOW_TYPE): cv.matches_regex(r"(mp3|ogg)"),
        vol.Required(CONF_RADIO_SHOW_START): cv.string,
        vol.Required(CONF_RADIO_SHOW_END): cv.string,
    }
)

KEYMASTER_SCHEMA: Final = vol.Schema(
    {
        vol.Optional(CONF_KEYMASTER_NAME): cv.string,
        vol.Optional(CONF_KEYMASTER_IRC_NICK): cv.string,
        vol.Optional(CONF_KEYMASTER_PHONE): cv.string,
        vol.Optional(CONF_KEYMASTER_EMAIL): cv.string,
        vol.Optional(CONF_KEYMASTER_TWITTER): cv.string,
    }
)

CONTACT_SCHEMA: Final = vol.Schema(
    {
        vol.Optional(CONF_EMAIL): cv.string,
        vol.Optional(CONF_IRC): cv.string,
        vol.Optional(CONF_ML): cv.string,
        vol.Optional(CONF_PHONE): cv.string,
        vol.Optional(CONF_TWITTER): cv.string,
        vol.Optional(CONF_SIP): cv.string,
        vol.Optional(CONF_FACEBOOK): cv.string,
        vol.Optional(CONF_IDENTICA): cv.string,
        vol.Optional(CONF_FOURSQUARE): cv.string,
        vol.Optional(CONF_JABBER): cv.string,
        vol.Optional(CONF_ISSUE_MAIL): cv.string,
        vol.Optional(CONF_KEYMASTERS): vol.All(
            cv.ensure_list, [KEYMASTER_SCHEMA], vol.Length(min=1)
        ),
    },
    required=False,
)

STATE_SCHEMA: Final = vol.Schema(
    {
        vol.Required(CONF_ENTITY_ID): cv.entity_id,
        vol.Inclusive(CONF_ICON_CLOSED, CONF_ICONS): cv.url,
        vol.Inclusive(CONF_ICON_OPEN, CONF_ICONS): cv.url,
    },
    required=False,
)

SENSOR_SCHEMA: Final = vol.Schema(
    {vol.In(SENSOR_TYPES): [cv.entity_id], cv.string: [cv.entity_id]}
)

CONFIG_SCHEMA: Final = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_CONTACT): CONTACT_SCHEMA,
                vol.Required(CONF_ISSUE_REPORT_CHANNELS): vol.All(
                    cv.ensure_list, [vol.In(ISSUE_REPORT_CHANNELS)]
                ),
                vol.Optional(CONF_LOCATION): LOCATION_SCHEMA,
                vol.Required(CONF_LOGO): cv.url,
                vol.Required(CONF_SPACE): cv.string,
                vol.Required(CONF_STATE): STATE_SCHEMA,
                vol.Required(CONF_URL): cv.string,
                vol.Optional(CONF_SENSORS): SENSOR_SCHEMA,
                vol.Optional(CONF_SPACEFED): SPACEFED_SCHEMA,
                vol.Optional(CONF_CAM): vol.All(
                    cv.ensure_list, [cv.url], vol.Length(min=1)
                ),
                vol.Optional(CONF_STREAM): STREAM_SCHEMA,
                vol.Optional(CONF_FEEDS): FEEDS_SCHEMA,
                vol.Optional(CONF_CACHE): CACHE_SCHEMA,
                vol.Optional(CONF_PROJECTS): vol.All(cv.ensure_list, [cv.url]),
                vol.Optional(CONF_RADIO_SHOW): vol.All(
                    cv.ensure_list, [RADIO_SHOW_SCHEMA]
                ),
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)
