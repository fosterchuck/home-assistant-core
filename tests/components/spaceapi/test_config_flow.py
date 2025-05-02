"""Tests for the Space API config flow."""

from unittest.mock import ANY

from homeassistant import config_entries
from homeassistant.components.spaceapi import DOMAIN
from homeassistant.components.spaceapi.config_flow import BASIC_INITIAL_SCHEMA
from homeassistant.core import HomeAssistant

# async def test_import_legacy_yaml_config(hass: HomeAssistant) -> None:
#     """Test that legacy YAML is imported successfully."""


# async def test_cant_user_config_after_import(hass: HomeAssistant) -> None:
#     """Test that a UI config doesn't work following a YAML import."""


# async def test_can_configure_options_after_legacy_yaml(hass: HomeAssistant) -> None:
#     """Test that Options Flow can be used after a YAML import has successfully created a ConfigEntry."""


async def test_step_user_form(hass: HomeAssistant) -> None:
    """Test the initialization of the form in the first step of the config flow."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    expected = {
        "data_schema": BASIC_INITIAL_SCHEMA,
        "description_placeholders": None,
        "errors": {},
        "flow_id": ANY,
        "handler": "spaceapi",
        "last_step": None,
        "step_id": "user",
        "type": "form",
        "preview": None,
    }
    assert expected == result


# async def test_step_user_store_staged(hass: HomeAssistant) -> None:
#     """Test that the config entered by the user is persisted when an error occurs."""


# async def test_step_user_cancel(hass: HomeAssistant) -> None:
#     """Test the the normal user config cancels with expected results."""


# async def test_step_user_success(hass: HomeAssistant) -> None:
#     """Test that the normal user config flow works."""


# async def test_can_configure_options_after_user(hass: HomeAssistant) -> None:
#     """Test that Options Flow works ."""
