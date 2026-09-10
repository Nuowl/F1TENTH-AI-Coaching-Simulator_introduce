# AI Driving Coaching for F1TENTH — 연구 소개 웹사이트

[English](README.md) | **한국어**

AiX Lab 연구 소개용 독립 정적 웹사이트입니다. 영어가 기본이며 설명·캡션은
한국어로 전환할 수 있습니다. 프로젝트명과 목차 제목은 두 언어에서 영어로 유지합니다.

## 미리보기

`index.html`을 직접 열거나 이 폴더에서 다음을 실행합니다.

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

브라우저에서 http://127.0.0.1:8080/ 에 접속합니다. 실행을 위한 별도 설치는 필요 없습니다.
JavaScript가 꺼져 있어도 영어 본문과 페이지 이동은 사용할 수 있습니다.

## 파일 구조와 편집

- `*.html`: 각각 주소를 갖는 11개 정적 페이지.
- `assets/css/research.css`: 디자인 규격과 반응형 레이아웃.
- `assets/js/research.js`: 한영 전환·모바일 메뉴·영상 재생 및 확대.
- `assets/media/`: 페이지에 사용하는 이미지·원본 MP4와 GIF 대체 자료.
- `tools/content.py`: 한영 본문과 페이지 구성.
- `tools/research_details.py`: 코칭 식·용어, 프로그램 사용 안내, 화면 번호별 설명.
- `tools/components.py`: 그림·표·카드 등 작은 공통 컴포넌트.
- `tools/build.py`: 공통 페이지 구조와 HTML 생성기.
- `tools/site_chrome.py`: 독립된 연구실 배너. `SHOW_LAB_HEADER = False`로 제외 가능.
- `docs/`: 설계·출처·구현 근거·검증·게시 안내.

본문을 수정한 뒤 `python3 tools/build.py`로 HTML을 다시 생성합니다.
`?lang=ko`는 한국어 직접 링크이며 페이지 이동 후에도 선택 언어를 유지합니다.
[게시 안내](docs/PUBLISHING.md)와 [구현 근거](docs/EVIDENCE.md)를 참고하세요.

## 영상과 이미지

영상 원본은 수정하지 않고, 확인된 검은 여백만 웹 표시 영역에서 잘라냅니다.
좁은 패널의 수치를 가리지 않도록 조작 버튼은 잘린 화면 바로 아래에 둡니다.
설정과 검증 범위는 [영상 여백 처리](docs/VIDEO_CROPS.md)를 참고하세요.

원본 MP4 영상을 무음 자동 반복 재생합니다. 좌측 하단의 투명 아이콘으로
재생/정지 전환과 확대를 조작합니다. 정지하면 현재 프레임에서 멈추고 재생하면
이어집니다. 확대해도 같은 플레이어와 재생 위치를 유지합니다.
탭을 숨기면 재생을 중단하고 돌아오면 이전에 재생 중이던 영상만 다시 재생합니다.
정적 이미지에는 조작 버튼이 없으며 자료 설명과 출처 캡션은 유지합니다.
영상은 `assets/media/`에 포함되므로 임시 원본 폴더가 필요하지 않습니다.
빌더는 GIF와 이름이 같은 MP4를 우선 사용하며 GIF/포스터 대체 경로도 유지합니다.
`python3 tools/import_videos.py 원본폴더`로 재인코딩 없이 가져온 뒤
`python3 tools/build.py`로 반영합니다. 원본 해시는 `docs/video-manifest.json`에 기록합니다.

## GitHub 업로드

`f1tenth-ai-coaching` 안의 내용만 새 저장소의 루트에 올리면 됩니다.
HTML·`assets/`·`tools/`·`docs/`와 두 README를 포함하세요.
`.gitignore`에 따라 검증용 스크린샷, 캐시, 로컬 실행 환경과 사용하지 않는
예비 이미지는 제외합니다. `ftenth_sim`이나 별도 디자인 키트는 포함하지 않습니다.
GitHub 기본 README는 영어이며 맨 위 링크로 한글 문서로 이동할 수 있습니다.

실제로 게시하지 않고 검증된 업로드 후보를 만들려면 다음을 실행합니다.

```bash
python3 tools/build.py
python3 tools/verify_links.py
python3 tools/package_public.py ../downloads/f1tenth-ai-coaching-public.zip
```

ZIP 안의 파일이 곧 저장소 루트에 들어갈 내용입니다. 공개 전에는
[게시 확인 사항](docs/PUBLISHING.md)을 확인하세요. 공개 저장소로 올려도
외부 자료의 권리가 바뀌는 것은 아닙니다. 현재 웹사이트나 외부 자료에
일괄 적용하는 라이선스는 지정하지 않았습니다.

연구실 홈페이지에 합칠 때 배너는 `tools/site_chrome.py`에서 수정하거나 표시
설정을 끄고 재생성합니다. 프로젝트명·메뉴·본문과 독립되어 있습니다.
`?embed=1`로 기존 헤더·푸터를 숨긴 형태를 미리 확인할 수도 있습니다.

## 디자인 재사용

별도 `aix-research-design-kit` 패키지에 규격서·참고 이미지·일반 연구 예제와
Codex 입력 프롬프트가 있습니다. 이 사이트는 해당 폴더를 실행 중 참조하지 않습니다.

`tools/package_delivery.py`는 사이트와 키트 두 폴더를 함께 묶는 작업용 도구입니다.
일반 본문 빌드·링크 검사·미리보기에는 사이트 폴더 하나만 있으면 됩니다.

기준일: 2026-09-11. 학습 효과와 적응형 페달·코칭 제어는 연구 목표이며,
구현을 완료했다는 주장이 아닙니다. 자세한 출처는 사이트의 References에서 확인합니다.
