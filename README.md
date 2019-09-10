# Overlay for Closed Captions for Streams

![Sample](./sample.gif)

Overlay for Closed Captions for Streams는 [Closed Captions for Streams](https://www.twitch.tv/ext/xxwoffr2lnpxrgpq228mawvdgxetip)의 자막을 방송 송출 프로그램(OBS, XSplit 등)에 표시하기 위한 애드온입니다.

이 애드온을 사용하면 마이크를 통해 말한 내용을 방송 화면에 실시간으로 자막처럼 표시할 수 있습니다.

[데모 동영상](https://youtu.be/CAIVO6aMgs4)

## 사용방법

사용방법에 대한 동영상 안내를 선호하시는 분들은 아래 링크를 참조해주세요.

[사용 방법 동영상 안내](https://youtu.be/XVN0jyW6wh4)

### 1. [Closed Captions for Streams](https://www.twitch.tv/ext/xxwoffr2lnpxrgpq228mawvdgxetip) 설정

Overlay for Closed Captions for Streams는 Closed Captions for Streams의 음성 인식 데이터를 사용하여 동작합니다.

따라서 Overlay for Closed Captions for Streams를 사용하기 전에 Closed Captions for Streams의 설정을 먼저 진행해야 합니다.

설정 방법은 다음과 같습니다.

1. [음성 인식 사이트](https://cc.go.alejo47.com/recorder)에 "최신 버전 크롬"으로 접속합니다.
2. 음성 인식 사이트에 방송하고자 하는 트위치 계정으로 로그인합니다.
3. 음성 인식 사이트의 Language 항목을 사용하는 언어(한국어)로 변경합니다.
4. 음성 인식 사이트의 Start 버튼을 클릭하고 마이크 사용 권한을 허용합니다.
5. 음성 인식 사이트에서 마이크에 말한 내용을 인식한 내용이 출력되는 것을 확인합니다.

마이크에 말한 내용이 정상적으로 인식되어 사이트에 출력된다면, Closed Captions for Streams의 설정을 모두 완료한 것입니다.

### 2. Overlay for Closed Captions for Streams 설정

1. [다운로드 페이지](https://github.com/yf-dev/ClosedCaptionsOverlay/releases/latest)에서 `Source code (zip)` 파일을 다운로드하고 압축을 해제합니다.
2. "최신 버전 크롬"으로 압축 해제한 자막 오버레이 파일(`caption.html`)을 엽니다.
3. 크롬에서 연 자막 오버레이 파일 주소의 끝에 `?channel=트위치채널명` 을 덧붙여서 새로고침을 합니다. (예시: `file:///C:/data/ClosedCaptionsOverlay-1.0/caption.html?channel=sleeping_ce`)
4. 크롬에서 정상적으로 마이크에 말한 내용이 출력되는 것을 확인합니다.

### 3. 방송 송출 프로그램 설정

#### 3.1. OBS Studio

1. Overlay for Closed Captions for Streams 설정 3단계에서 확인한 주소(예시: `file:///C:/data/ClosedCaptionsOverlay-1.0/caption.html?channel=sleeping_ce`)를 OBS에 "브라우저" 소스의 URL로 등록합니다.
2. 캔버스 크기 1280x720에서 권장하는 브라우저 소스 너비와 높이는 840, 210입니다.

#### 3.1. XSplit Broadcaster

1. 웹 페이지 소스 추가 창에서 `Browese...` 버튼을 클릭하고, 압축 해제한 자막 오버레이 파일(`caption.html`)을 선택합니다.
2. 추가된 소스를 오른쪽 클릭하고, `HTML 소스` 항목의 주소 끝에 `?channel=트위치채널명` 을 덧붙이고 `적용` 버튼을 클릭합니다.
2. 캔버스 크기 1280x720에서 권장하는 브라우저 소스 너비와 높이는 840, 210입니다.

### 4. 설정 마무리

해당 설정을 완료한 후, 실제 방송에서 자막을 사용하시고자 할 때에는 [음성 인식 사이트](https://cc.go.alejo47.com/recorder)에 접속하셔서 Start 버튼을 클릭하시면 됩니다.

만약 사용을 종료하시려면 음성 인식 사이트의 Stop 버튼을 클릭하거나 창을 종료합니다.

트위치에서 자막을 지원하는 방송을 진행하신다면, 방송 태그에 [자막(Closed captions)](https://www.twitch.tv/directory/all/tags/8a01ea18-df97-4046-9cff-a9a822bb96e5)을 추가하시는 것도 추천드립니다.

## 커스터마이징

### 1. 오버레이에 표시되는 프로필 이미지 변경

다운로드한 Overlay for Closed Captions for Streams의 압축 해제 파일 중 `profile.png` 파일을 사용하시고자 하는 프로필 이미지로 변경합니다.

(방송 송출 프로그램에 변경사항을 적용하기 위해서는 캐시를 초기화해야 할 수 있습니다.)

### 2. 오버레이에 표시되는 강조 색상 변경

다운로드한 Overlay for Closed Captions for Streams의 압축 해제 파일 중 `caption.html` 파일을 열고 `#95BBDF` 문자열을 원하는 색상 코드로 변경하신 후 저장합니다.

(방송 송출 프로그램에 변경사항을 적용하기 위해서는 캐시를 초기화해야 할 수 있습니다.)

## License

본 프로젝트는 [MIT License](./LICENSE) 하에 제공됩니다.