[한국어](https://github.com/yf-dev/OpenCaptionsOverlay)

# Open Captions Overlay

![Sample](./sample.gif)

`Open Captions Overlay` is a service to display subtitles on broadcast programs such as `OBS` and `XSplit`.

If you use this service, the voice spoken through the microphone can be displayed as subtitles in real time on the broadcast screen.

This project was inspired by [Closed Captions for Streams](https://www.twitch.tv/ext/xxwoffr2lnpxrgpq228mawvdgxetip).

[Demo Video](https://youtu.be/CAIVO6aMgs4)

## Usage

### 1. Setting the speech recognition

1. Access [Voice Recognition Site] (https://cc-overlay.update.sh/recognition) using __"latest version of Chrome"__.
2. Log in to the `Voice Recognition Site` with the Twitch account you want to broadcast.
3. Click the `Start Recognition` button and allow the microphone permission.
4. Make sure that what you say on the microphone is printed out.

If what you said on your microphone is successfully printed, you have completed all of the voice recognition settings.

### 2. Setting the broadcast transmission program

#### 3.1. OBS Studio

1. Register the'overlay address' displayed in [Voice Recognition Site](https://cc-overlay.update.sh/recognition) as the browser source URL of OBS Studio.
2. When your canvas size is `1280x720`, the recommended browser size is `840x210`.

#### 3.1. XSplit Broadcaster

1. Register the'overlay address' displayed in [Voice Recognition Site](https://cc-overlay.update.sh/recognition) in the URL field of the Add Web Page Source window.
2. When your canvas size is `1280x720`, the recommended browser size is `840x210`.

### 4. Finish settings

After completing the settings, if you want to use subtitles in the actual broadcast, access the [Voice Recognition Site](https://cc-overlay.update.sh/recognition) and click the `Start Recognition` button.

If you want to end the use, click the `End Recognition` button on the `Voice Recognition Site` or close the window.

## Customizing

### 1. Change your profile image displayed on the overlay

Add the following content to the CSS of the browser source `Open Captions Overlay` of the broadcast program.

```css
:root {
    --profile-url: url(https://i.postimg.cc/Qtsn3rc7/profile.png);
}
```

Change (`https://i.postimg.cc/Qtsn3rc7/profile.png`) to the profile image URL you want to change.

(Image URLs can be created through image hosting services such as [postimages.org](https://postimages.org/).)

### 2. Change the highlight color displayed on the overlay

Add the following content to the CSS of the browser source `Open Captions Overlay` of the broadcast program.

```css
:root {
    --accent-color: #95BBDF;
}
```

Change the `#95BBDF` value to the highlight color code you want to change.

### 3. When the overlay background is not transparent

Add the following content to the CSS of the browser source `Open Captions Overlay` of the broadcast program.

```css
body {
    background-color: rgba(0, 0, 0, 0);
    margin: 0px auto;
    overflow: hidden;
}
```

## Development

Below for developers

### Init project

```
docker-compose run --rm backend python manage.py db upgrade
```

### Reinstall dependencies

```
docker-compose run --rm backend pipenv lock --pre
docker-compose build --force-rm
```

## License

This project is available under [MIT License](./LICENSE).
