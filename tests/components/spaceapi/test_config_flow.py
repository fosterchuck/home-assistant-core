"""Tests for the Space API config flow."""

from unittest.mock import ANY

from homeassistant.components.spaceapi import DOMAIN
from homeassistant.components.spaceapi.config_flow import (
    BASIC_CONTACT_SCHEMA,
    BASIC_INITIAL_SCHEMA,
    CONF_LOGO_URL,
    CONF_SPACE_NAME,
    CONF_SPACE_URL,
)
from homeassistant.config_entries import SOURCE_USER, ConfigFlowContext
from homeassistant.core import HomeAssistant

# async def test_import_legacy_yaml_config(hass: HomeAssistant) -> None:
#     """Test that legacy YAML is imported successfully."""


# async def test_import_legacy_yaml_fails_required(hass: HomeAssistant) -> None:
#     """Test that legacy YAML import fails when required keys are missing."""


# async def test_import_legacy_yaml_fails_invalid(hass: HomeAssistant) -> None:
#     """Test that legacy YAML import fails when invalid values are provided."""


# async def test_cant_user_config_after_import(hass: HomeAssistant) -> None:
#     """Test that a UI config doesn't work following a YAML import."""


# async def test_can_configure_options_after_legacy_yaml(hass: HomeAssistant) -> None:
#     """Test that Options Flow can be used after a YAML import has successfully created a ConfigEntry."""


# @pytest.mark.parametrize(
#     ("contact_key", "contact_value"),
#     [
#         ("192.618.178.1", "192.618.178.1"),
#         (" 192.618.178.1 ", "192.618.178.1"),
#         (" demo.host ", "demo.host"),
#     ],
# )
async def test_full_config_flow(
    hass: HomeAssistant,  # , contact_key, contact_value
) -> None:
    """Test the entire Config Flow with succeeding values."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context=ConfigFlowContext(source=SOURCE_USER)
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
    result = await hass.config_entries.flow.async_configure(
        flow_id=result["flow_id"],
        user_input={
            CONF_SPACE_NAME: "Any test string",
            CONF_LOGO_URL: "http://test.test",
            CONF_SPACE_URL: "http://test2.test2",
        },
    )
    await hass.async_block_till_done()
    expected = {
        "data_schema": BASIC_CONTACT_SCHEMA,
        "description_placeholders": None,
        "errors": {},
        "flow_id": ANY,
        "handler": "spaceapi",
        "last_step": True,
        "step_id": "contact",
        "type": "form",
        "preview": None,
    }
    assert expected == result
    # Put in the contact keys and parametrize vars.
    # result = await hass.config_entries.flow.async_configure(
    #     flow_id=result["flow_id"],
    #     user_input={
    #         CONF_SPACE_NAME: "Any test string",
    #         CONF_LOGO_URL: "http://test.test",
    #         CONF_SPACE_URL: "http://test2.test2",
    #     },
    # )


# async def test_fail_for_no_contacts(
#     hass: HomeAssistant, contact_key, contact_value
# ) -> None:
#     """Test that the Config Flow fails when there are no contact options provided."""


# async def test_full_reconfigure(
#     hass: HomeAssistant
# ) -> None:
#     """Test that the Config Flow reconfigure works."""


# async def test_step_user_store_staged(hass: HomeAssistant) -> None:
#     """Test that the config entered by the user is persisted when an error occurs."""


# async def test_step_user_cancel(hass: HomeAssistant) -> None:
#     """Test the the normal user config cancels with expected results."""


# async def test_step_user_success(hass: HomeAssistant) -> None:
#     """Test that the normal user config flow works."""


# async def test_can_configure_options_after_user(hass: HomeAssistant) -> None:
#     """Test that Options Flow works ."""
