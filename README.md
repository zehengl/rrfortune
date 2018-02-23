# rrfortune

## Why

Believe it or not, my wife is still obsessed with the login streak on [RenRen](http://renren.com/).
She will be unhappy if I forget to login and collect RenRen fortune.
Most of the time, let alone when you travel, it's hard to remember.
So I have to improvise.

## Solution

- Consider logging in and clicking the button a UI test
- Have Travis CI run a daily build to trigger that test

## Install
1. Download the driver (I'm using Chrome)
    - [mac](https://chromedriver.storage.googleapis.com/2.35/chromedriver_mac64.zipi)
    - [linux](https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip)

2. Put the driver in the **PATH**

3. Clone this repo
    - ```git clone git@github.com:zehengl/rrfortune.git```

4. Install dependencies (I'm using pipenv)
    - ```pipenv install --dev```

5. Export your login credentials
    - ```export email='xxx@yyy.zzz'```
    - ```export password='a1b2c3d4'```

6. Run test
    - ```pipenv run py.test```

My environment is as follow. Feel free to modify driver/test to fit your needs.
- Chrome: 64.0.3282.167
- Chrome Driver: 2.35
- macOS: 10.13.3

## Travis CI Setup
1. Fork this repo

2. Enable build on Travis CI

3. Set the environment variables (*email*/*password*) on Travis CI

4. Set a daily cron job
