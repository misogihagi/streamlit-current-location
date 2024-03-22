import { Streamlit } from "streamlit-component-lib";

const coordsToObject = ({
  accuracy,
  altitude,
  altitudeAccuracy,
  heading,
  latitude,
  longitude,
  speed,
}: GeolocationCoordinates) => ({
  accuracy,
  altitude,
  altitudeAccuracy,
  heading,
  latitude,
  longitude,
  speed,
});

window.onload = () => {
  navigator.geolocation.getCurrentPosition(({ coords }) => {
    Streamlit.setComponentValue(coordsToObject(coords));
  }, console.log);

  Streamlit.setComponentReady();
};
