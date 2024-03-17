# How to run client-weather-app

STEP 1: Download the repo:
```
git clone https://github.com/antonVosc/client-weather-app.git
```

STEP 2: Navigate to client-weather-app directory:
```
cd client-weather-app
```

STEP 3: Create the virtual environment:
```
python3 -m venv venv
```

STEP 4: Activate the virtual environment:
```
. venv/bin/activate
```

STEP 5: Install the required libraries:
```
pip install -r requirements.txt
```

STEP 6: To run the program:

```
flet run main.py
```

NOTE: If you want to deploy this web app to cloud service provider, please look into [CloudFlare](https://python.plainenglish.io/deploying-a-flet-app-for-free-on-cloudflare-pages-e56ecc6ce450) and [FlyIO](https://flet.dev/docs/guides/python/deploying-web-app/hosting-providers/fly-io/).