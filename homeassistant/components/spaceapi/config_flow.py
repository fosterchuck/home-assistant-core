"""Config flow for Space API integration."""

from typing import Any, Final

import voluptuous as vol

from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.config_entries import (
    SOURCE_RECONFIGURE,
    ConfigEntry,
    ConfigFlow,
    ConfigFlowResult,
    OptionsFlow,
)
from homeassistant.const import CONF_SENSORS
from homeassistant.core import callback
from homeassistant.exceptions import ConfigEntryError
from homeassistant.helpers.selector import (
    EntityFilterSelectorConfig,
    EntitySelector,
    EntitySelectorConfig,
    TextSelector,
    TextSelectorConfig,
    TextSelectorType,
)

from .const import CONF_CONTACT, CONF_HUMIDITY, CONF_TEMPERATURE, DOMAIN

# Labels for the ConfigEntry
CONF_SPACE_NAME: Final[str] = "space"
CONF_LOGO_URL: Final[str] = "logo"
CONF_SPACE_URL: Final[str] = "url"
CONF_CONTACT_PHONE: Final[str] = "phone"
CONF_CONTACT_SIP: Final[str] = "sip"
CONF_CONTACT_IRC: Final[str] = "irc"
CONF_CONTACT_TWITTER: Final[str] = "twitter"
CONF_CONTACT_MASTODON: Final[str] = "mastodon"
CONF_CONTACT_FACEBOOK: Final[str] = "facebook"
CONF_CONTACT_IDENTICA: Final[str] = "identica"
CONF_CONTACT_FOURSQUARE: Final[str] = "foursquare"
CONF_CONTACT_EMAIL: Final[str] = "email"
CONF_CONTACT_ML: Final[str] = "ml"
CONF_CONTACT_XMPP: Final[str] = "xmpp"
CONF_CONTACT_ISSUE_MAIL: Final[str] = "issue_mail"
CONF_CONTACT_GOPHER: Final[str] = "gopher"
CONF_CONTACT_MATRIX: Final[str] = "matrix"
CONF_CONTACT_MUMBLE: Final[str] = "mumble"

# Figure out how to make at least one entry mandatory
BASIC_CONTACT_SCHEMA: Final = vol.Schema(
    schema={
        vol.Optional(CONF_CONTACT_PHONE): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.TEL,
            )
        ),
        vol.Optional(CONF_CONTACT_SIP): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.TEXT,
            )
        ),
        vol.Optional(CONF_CONTACT_IRC): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.URL,
            )
        ),
        vol.Optional(CONF_CONTACT_TWITTER): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.TEXT,
            )
        ),
        vol.Optional(CONF_CONTACT_MASTODON): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.TEXT,
            )
        ),
        vol.Optional(CONF_CONTACT_FACEBOOK): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.TEXT,
            )
        ),
        vol.Optional(CONF_CONTACT_IDENTICA): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.TEXT,
            )
        ),
        vol.Optional(CONF_CONTACT_FOURSQUARE): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.TEXT,
            )
        ),
        vol.Optional(CONF_CONTACT_EMAIL): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.EMAIL,
            )
        ),
        vol.Optional(CONF_CONTACT_ML): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.EMAIL,
            )
        ),
        vol.Optional(CONF_CONTACT_XMPP): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.TEXT,
            )
        ),
        vol.Optional(CONF_CONTACT_ISSUE_MAIL): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.EMAIL,
            )
        ),
        vol.Optional(CONF_CONTACT_GOPHER): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.URL,
            )
        ),
        vol.Optional(CONF_CONTACT_MATRIX): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.TEXT,
            )
        ),
        vol.Optional(CONF_CONTACT_MUMBLE): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.URL,
            )
        ),
    },
    required=True,
    extra=vol.PREVENT_EXTRA,
)

# Figure out if this can prevent incorrectly formatted input
BASIC_INITIAL_SCHEMA: Final = vol.Schema(
    {
        vol.Required(CONF_SPACE_NAME): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.TEXT,
            )
        ),
        vol.Required(CONF_LOGO_URL): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.URL,
            )
        ),
        vol.Required(CONF_SPACE_URL): TextSelector(
            TextSelectorConfig(
                type=TextSelectorType.URL,
            )
        ),
    },
    extra=vol.PREVENT_EXTRA,
)


class SpaceApiConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Space API."""

    VERSION: int = 1
    staged_config_entry: dict[str, Any]
    _existing_entry_data: ConfigEntry

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle a config flow initialized by the user."""
        errors: dict[str, str] = {}
        if user_input is not None:
            self.staged_config_entry = user_input
            if not errors:
                return await self.async_step_contact()
            raise ConfigEntryError
        if self.source == SOURCE_RECONFIGURE:
            suggested_values = {
                CONF_SPACE_NAME: self._existing_entry_data.data[CONF_SPACE_NAME],
                CONF_LOGO_URL: self._existing_entry_data.data[CONF_LOGO_URL],
                CONF_SPACE_URL: self._existing_entry_data.data[CONF_SPACE_URL],
            }
            return self.async_show_form(
                step_id="user",
                data_schema=self.add_suggested_values_to_schema(
                    data_schema=BASIC_INITIAL_SCHEMA,
                    suggested_values=suggested_values,
                ),
                errors=errors,
            )
        return self.async_show_form(
            step_id="user",
            data_schema=BASIC_INITIAL_SCHEMA,
            errors=errors,
        )

    async def async_step_contact(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Second page of the initial config to get contact info."""
        errors: dict[str, str] = {}
        if user_input is not None:
            self.staged_config_entry[CONF_CONTACT] = user_input
            if self.source == SOURCE_RECONFIGURE:
                return self.async_update_reload_and_abort(
                    entry=self._existing_entry_data,
                    title=DOMAIN,
                    data=self.staged_config_entry,
                )
            return self.async_create_entry(title=DOMAIN, data=self.staged_config_entry)
        if self.source == SOURCE_RECONFIGURE:
            suggested_values: dict[str, str] = self._existing_entry_data.data[
                CONF_CONTACT
            ]
            return self.async_show_form(
                step_id="contact",
                data_schema=self.add_suggested_values_to_schema(
                    data_schema=BASIC_CONTACT_SCHEMA,
                    suggested_values=suggested_values,
                ),
                errors=errors,
            )
        return self.async_show_form(
            step_id="contact",
            data_schema=BASIC_CONTACT_SCHEMA,
            errors=errors,
            last_step=True,
        )

    async def async_step_reconfigure(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Add reconfigure step to allow to reconfigure a config entry."""
        if user_input is not None:
            pass
        self._existing_entry_data: ConfigEntry = self._get_reconfigure_entry()
        return await self.async_step_user()

    # async def async_step_import(self, import_data: dict[str, Any]) -> ConfigFlowResult:
    #     """Import legacy config from configuration.yaml."""
    #     # Import the required fields into data
    #     # Import the options into options

    #     async_create_issue(
    #         hass=self.hass,
    #         domain=DOMAIN,
    #         issue_id=f"deprecated_yaml_{DOMAIN}",
    #         is_fixable=False,
    #         is_persistent=False,
    #         issue_domain=DOMAIN,
    #         severity=IssueSeverity.WARNING,
    #         translation_key="deprecated_yaml_import_issue",
    #         translation_placeholders={
    #             "domain": DOMAIN,
    #             "integration_title": INTEGRATION_TITLE,
    #         },
    #     )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow:
        """Get the options flow for this handler."""
        return SpaceApiOptionsFlowHandler()


class SpaceApiOptionsFlowHandler(OptionsFlow):
    """Handles options flow for the Space API."""

    staged_config_entry: dict[str, Any]

    # def __init__(self, config_entry: ConfigEntry) -> None:
    #     """Initialize OptionsFlowHandler for the Space API."""

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Manage the options for the Space API."""
        self.staged_config_entry = dict(self.config_entry.options)
        if user_input is not None:
            # Abort config flow
            pass
        return self.async_show_menu(
            step_id="init",
            menu_options={
                "temperature": "Select Temp Sensors",
                "humidity": "Select Humidity Sensors",
            },
        )

    async def async_step_temperature(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Config Options step to obtain the temperature sensors."""
        errors: dict[str, str] = {}
        if user_input is not None:
            if self.staged_config_entry.get(CONF_SENSORS) is None:
                self.staged_config_entry[CONF_SENSORS] = {}
            self.staged_config_entry[CONF_SENSORS][CONF_TEMPERATURE] = user_input.get(
                CONF_TEMPERATURE
            )
            # if self.hass.config_entries.async_update_entry(
            #     entry=self.config_entry, title=DOMAIN, data=self.staged_config_entry
            # ):
            #     return ConfigFlowResult()
            # FlowResultType.CREATE_ENTRY
            # return FlowResultType.ABORT
            return self.async_create_entry(title=DOMAIN, data=self.staged_config_entry)
        TEMP_SENSOR_SCHEMA = vol.Schema(
            {
                vol.Required(CONF_TEMPERATURE): EntitySelector(
                    EntitySelectorConfig(
                        multiple=True,
                        filter=EntityFilterSelectorConfig(
                            device_class=SensorDeviceClass.TEMPERATURE
                        ),
                    )
                ),
            }
        )
        existing_sensors: dict[str, list[str]] | None = self.staged_config_entry.get(
            CONF_SENSORS
        )
        if existing_sensors and existing_sensors.get(CONF_TEMPERATURE):
            existing_temp_sensor_ids: list[str] | None = existing_sensors.get(
                CONF_TEMPERATURE
            )
            return self.async_show_form(
                step_id="temperature",
                data_schema=self.add_suggested_values_to_schema(
                    data_schema=TEMP_SENSOR_SCHEMA,
                    suggested_values={CONF_TEMPERATURE: existing_temp_sensor_ids},
                ),
                errors=errors,
            )
        return self.async_show_form(
            step_id="temperature",
            data_schema=TEMP_SENSOR_SCHEMA,
            errors=errors,
        )

    async def async_step_humidity(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Config Options step to obtain the humidity sensors."""
        errors: dict[str, str] = {}
        if user_input is not None:
            if self.staged_config_entry.get(CONF_SENSORS) is None:
                self.staged_config_entry[CONF_SENSORS] = {}
            self.staged_config_entry[CONF_SENSORS][CONF_HUMIDITY] = user_input.get(
                "user_input_humidity"
            )
            return self.async_create_entry(title=DOMAIN, data=self.staged_config_entry)
        return self.async_show_form(
            step_id="humidity",
            data_schema=vol.Schema(
                {
                    vol.Required("user_input_humidity"): EntitySelector(
                        EntitySelectorConfig(
                            multiple=True,
                            filter=EntityFilterSelectorConfig(
                                device_class=SensorDeviceClass.HUMIDITY
                            ),
                        )
                    ),
                }
            ),
            errors=errors,
        )
