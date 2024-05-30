import streamlit as st

# Add the manifest and register service worker
st.markdown("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="manifest" href="manifest.json">
  <title>Streamlit PWA</title>
</head>
<body>
  <div id="root"></div>
  <script>
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('service-worker.js')
      .then(function() {
        console.log('Service Worker Registered');
      });
    }
  </script>
</body>
</html>
""", unsafe_allow_html=True)

# Your Streamlit app code
st.title('Streamlit PWA')
st.write('This is a sample Streamlit app with PWA features.')
