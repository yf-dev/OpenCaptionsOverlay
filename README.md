# Overlay for Closed Captions for Streams

![Sample](./sample.gif)

Overlay for Closed Captions for Streams는 [Closed Captions for Streams](https://www.twitch.tv/ext/xxwoffr2lnpxrgpq228mawvdgxetip)의 자막을 방송 송출 프로그램(OBS, Xsplit 등)에 표시하기 위한 애드온입니다.

이 애드온을 사용하면 마이크를 통해 말한 내용을 방송 화면에 실시간으로 자막처럼 표시할 수 있습니다.

[데모 동영상](https://youtu.be/CAIVO6aMgs4)

## 사용방법

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
2. "최신 버전 크롬"으로 압축 해제한 자막 오버레이 파일(caption.html)을 엽니다.
3. 크롬에서 연 자막 오버레이 파일 주소의 끝에 "?channel=트위치채널명" 을 덧붙여서 새로고침을 합니다. (예시: `file:///C:/data/ClosedCaptionsOverlay-1.0/caption.html?channel=sleeping_ce`)
4. 크롬에서 정상적으로 마이크에 말한 내용이 출력되는 것을 확인합니다.

### 3. 설정 마무리

1. Overlay for Closed Captions for Streams 설정 3단계에서 확인한 주소(예시: `file:///C:/data/ClosedCaptionsOverlay-1.0/caption.html?channel=sleeping_ce`)를 방송 송출 프로그램에 브라우저 소스로 등록합니다.
2. 권장하는 브라우저 소스 너비와 높이는 840px, 210px입니다.

해당 설정을 완료한 후, 실제 방송에서 자막을 사용하시고자 할 때에는 [음성 인식 사이트](https://cc.go.alejo47.com/recorder)에 접속하셔서 Start 버튼을 클릭하시면 됩니다.

만약 사용을 종료하시려면 음성 인식 사이트의 Stop 버튼을 클릭하거나 창을 종료합니다.

## 커스터마이징

### 1. 오버레이에 표시되는 프로필 이미지 변경

다운로드한 Overlay for Closed Captions for Streams의 압축 해제 파일 중 `profile.png` 파일을 사용하시고자 하는 프로필 이미지로 변경합니다.

(방송 송출 프로그램에 변경사항을 적용하기 위해서는 캐시를 초기화해야 할 수 있습니다.)

### 2. 오버레이에 표시되는 강조 색상 변경

다운로드한 Overlay for Closed Captions for Streams의 압축 해제 파일 중 `caption.html` 파일을 열고 `#95BBDF` 문자열을 원하는 색상 코드로 변경하신 후 저장합니다.

(방송 송출 프로그램에 변경사항을 적용하기 위해서는 캐시를 초기화해야 할 수 있습니다.)

## License

본 프로젝트는 [MIT License](./LICENSE) 하에 제공됩니다.