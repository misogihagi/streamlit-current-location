# streamlit-current-location

Streamlit component to tell the current coordinaate

## Installation instructions

```sh
pip install streamlit-current-location
```

## Usage instructions

```python
import streamlit as st

from streamlit_current_location import current_position

# it returns dict of GeolocationCoordinates
# see https://developer.mozilla.org/ja/docs/Web/API/GeolocationCoordinates
position = current_position()

if position is not None:
  st.write("latitude: " + str(position["latitude"]))
  st.write("longitude: " + str(position["longitude"]))
```
