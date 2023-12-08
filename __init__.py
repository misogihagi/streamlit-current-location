import os

import streamlit.components.v1 as components

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "dist")


def current_position():
    component = components.declare_component("current_position", path=build_dir)
    value = component(name="current_position")
    return value
