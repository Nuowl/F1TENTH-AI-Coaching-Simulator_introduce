# AI Driving Coaching for F1TENTH

[English](README.md) | **한국어**

[연구 소개 페이지 바로가기](https://nuowl.github.io/F1TENTH-AI-Coaching-Simulator_introduce/?lang=ko) — 다운로드 없이 바로 볼 수 있습니다.

AutoDRIVE 기반 F1TENTH 주행 코칭 환경을 소개하는 한영 연구 웹사이트입니다.
연구 배경·목표·방법과 함께 시뮬레이터, 대시보드, 오버레이, Replay Studio,
향후 연구 방향을 설명합니다.

기본 언어는 영어입니다. 설명과 캡션은 한국어로 전환할 수 있으며,
프로젝트명과 목차 제목은 영어로 유지합니다.

## 미리보기

브라우저에서 `index.html`을 열면 됩니다. 로컬 서버를 이용하려면 다음을 실행합니다.

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

브라우저에서 http://127.0.0.1:8080/ 에 접속합니다. 정적 HTML·CSS·JavaScript로
구성되어 있어 별도 애플리케이션 프레임워크나 시뮬레이터 설치가 필요하지 않습니다.

## 파일 구조

- `*.html`: 연구와 소프트웨어 환경을 설명하는 11개 페이지.
- `assets/css/`: 레이아웃·글꼴·반응형 스타일.
- `assets/js/`: 언어 전환·메뉴·영상 조작.
- `assets/media/`: 연구 도해·스크린샷·시연 영상.
- `tools/content.py`, `tools/research_details.py`: 한영 본문.
- `tools/components.py`, `tools/build.py`: 공통 컴포넌트와 HTML 생성.
- `tools/site_chrome.py`: 연구실 배너.
- `docs/`: 출처와 기술 참고 문서.

## 내용 수정

본문 파일을 수정한 뒤 다음 명령으로 페이지에 반영합니다.

```bash
python3 tools/build.py
```

디자인은 `assets/css/research.css`에서 수정합니다. 주소에 `?lang=ko`를 붙이면
한국어로 열립니다. 이미지와 영상은 `assets/media/`에 저장되어 있습니다.

## 참고 자료

AI Coaching 논문, AutoDRIVE, Pure Pursuit의 출처는
[References & Credits](references.html)에서, 이미지·영상의 출처는
[미디어 출처](docs/ASSET_CREDITS.md)에서 확인할 수 있습니다.
