"""Focused bilingual explanations for the research and application pages."""
from components import bi, p, h, cite, note, cards, media, table


def equation(expression, en, ko):
    return '<div class="equation">' + expression + '</div>' + p(en, ko)


def coaching_math():
    return (h('Core Equations & Terms')
        + equation('a = λ ⊙ π* (o<sup>C</sup>) + (1 − λ) ⊙ a<sup>L</sup>',
            'Shared-control rule (paper Eq. 2). Each control axis has its own weight: 0 preserves the learner action, 1 replaces it with the expert action. The coach learns the weight, rather than learning the entire driving command from scratch.' + cite(1),
            '논문의 공유 제어 식(Eq. 2)입니다. 제어 축마다 개입 비율을 따로 정하며, 0이면 학습자 입력을 유지하고 1이면 전문가 입력으로 대체합니다. 코치는 주행 명령 전체를 새로 만드는 대신, 전문가의 도움을 얼마나 적용할지를 학습합니다.' + cite(1))
        + table(['Symbol / term', 'Meaning', 'F1TENTH interpretation'], [
            ('aᴸ · Learner action', bi('Input chosen by the learner.', '학습자가 직접 선택한 입력입니다.'), bi('Human steering and pedal inputs, after an explicit action conversion.', '사용자 조향·페달 입력을 제어 명령으로 변환한 값입니다.')),
            ('π* · Expert policy', bi('A competent reference policy.', '과제를 능숙하게 수행하는 기준 정책입니다.'), bi('PP is the current steering/speed reference, not a learned coach.', '현재 PP는 조향·속도의 기준입니다. 학습된 코치 자체는 아닙니다.')),
            ('oᶜ · Observation', bi('State and learner behavior available to the coach.', '코치가 확인할 수 있는 환경과 학습자의 행동입니다.'), bi('Candidate inputs include speed, path position, steering error and segment history.', '속도, 경로상 위치, 조향 차이, 구간별 이력 등을 코칭 입력으로 검토합니다.')),
            ('λ ∈ [0, 1] · Assistance', bi('A separate blending weight for each action axis.', '제어 축별로 설정하는 개입 비율입니다.'), bi('Future steering and longitudinal assistance must have defined units and authority.', '향후 조향·속도 개입의 단위와 제어 권한을 먼저 정의해야 합니다.')),
            ('⊙ · Element-wise product', bi('Multiply matching components, not a matrix product.', '각 축의 대응하는 성분끼리 곱한다는 뜻입니다.'), bi('Steering is blended with steering, not with a speed or pedal value.', '조향은 조향끼리 혼합합니다. 속도나 페달값과 직접 섞지 않습니다.')),
            ('θ · Skill', bi('Latent proficiency in the learner model.', '학습자 모델의 숨겨진 숙련도입니다.'), bi('Not a recorded sensor value; inference requires calibrated driving evidence.', '센서로 직접 측정하는 값이 아닙니다. 주행 자료를 이용한 추정·보정이 필요합니다.')),
            ('b(θ) · Skill belief', bi('A probability distribution over possible skill levels.', '가능한 숙련도 수준별 확률 분포입니다.'), bi('A future segment-level estimate should retain uncertainty.', '향후 구간별 숙련도를 추정할 때 불확실성도 함께 다룹니다.')),
        ])
        + equation('b<sup>+</sup>(θ) ∝ P(o<sup>C</sup> | θ) b(θ)',
            'Bayesian observation update: combine the prior belief with how likely the new observation is at each skill level, then normalize. The paper uses gate-passage times. Driving would require its own likelihood calibration; a slow corner can reflect caution rather than poor skill.' + cite(1),
            '기존 숙련도 추정에 새 관측이 각 숙련도에서 나타날 가능성을 반영한 뒤, 전체 확률을 정규화합니다. 논문은 게이트 통과 시간을 이용합니다. 차량에서는 코너를 천천히 통과한 이유가 실력 부족인지 안전을 위한 감속인지 구분할 수 있도록 별도로 보정해야 합니다.' + cite(1))
        + equation('VoI(s, θ) = E[Σ<sub>k≥0</sub> γ<sup>k</sup> r<sup>task</sup><sub>t+k</sub> | no AI assistance]',
            'Condensed notation for paper Eq. 1: evaluate expected future task rewards without assistance. s is the physical state, γ the discount factor and rᵗᵃˢᵏ the task reward. This is a learning objective, not a lap-time formula.' + cite(1),
            '논문 Eq. 1을 간략히 표시한 식입니다. s는 환경 상태, γ는 먼 미래의 보상에 적용하는 할인율, rᵗᵃˢᵏ는 과제 수행 보상입니다. AI 없이 계속 수행할 때 기대되는 성과를 평가하므로, 단순한 랩타임 계산식과는 다릅니다.' + cite(1))
        + equation('r<sup>C</sup><sub>t</sub> = θ<sub>t</sub> − θ<sub>t−1</sub>',
            'L2C uses simulated skill improvement as a practical PPO training reward. Actual learner skill is not directly available at deployment. Transferring this idea requires a validated learner model, not simply rewarding a faster assisted lap.' + cite(1),
            'L2C는 시뮬레이션상의 숙련도 증가량을 PPO 학습 보상으로 사용합니다. 실제 학습자의 숙련도는 직접 알 수 없으므로, 이를 차량에 적용하려면 학습자 모델을 검증해야 합니다. 보조 중 랩타임이 짧아졌다는 이유만으로 이 보상을 대신할 수는 없습니다.' + cite(1))
        + note('Project design boundary: paper a is the blended action. In a future vehicle pipeline, Coached, safety-filtered and Applied commands should be recorded separately. They must not all be labeled Applied.',
            '차량 적용 시 구분할 점: 논문의 a는 혼합된 조작값입니다. 향후 시스템에서는 코칭으로 만든 명령(Coached), 안전 가드가 수정한 명령, 최종 적용 명령(Applied)을 구분해 기록할 계획입니다.'))


def research_goal_details():
    return (h('From Questions to Testable Comparisons')
        + table(['Question', 'Proposed comparison', 'What must be controlled'], [
            ('Learning', bi('Compare unassisted PRE and POST, with PROBE checks during training.', '훈련 전 PRE와 훈련 후 POST를 비교하고, 훈련 중 PROBE로 확인합니다.'), bi('Track, starting conditions, speed ceiling and exposure to practice.', '트랙, 출발 조건, 속도 상한, 연습량을 맞춰야 합니다.')),
            ('Intervention', bi('Compare guidance strategies and measure when and how strongly each intervenes.', '안내 전략별로 개입 시점·빈도·크기와 이후 조작 변화를 비교합니다.'), bi('Same reference controller and a separately logged safety layer.', '기준 제어기를 통일하고 안전 개입은 별도로 기록합니다.')),
            ('Transfer', bi('Evaluate on a held-out course with a different straight/corner mix.', '직선·커브 구성이 다른 미학습 코스에서 평가합니다.'), bi('Do not confuse memorizing a route with learning a driving skill.', '특정 경로를 외운 효과와 운전 기술의 향상을 구분합니다.')),
        ])
        + p('Repeated PRE–PRE and EXPERT–EXPERT runs also matter: they characterize normal driver variation and reference repeatability before attributing a change to coaching. A practice-only comparison condition and an adequate participant sample are proposed to separate coaching from ordinary practice effects.',
            'PRE–PRE와 EXPERT–EXPERT 반복 주행도 필요합니다. 평소 운전자의 기록 변동과 기준 제어기의 반복성을 먼저 확인해야 코칭으로 생긴 변화를 해석할 수 있습니다. 일반적인 연습 효과와 구분하기 위해 보조 없는 연습 조건과 충분한 참가자 수를 갖춘 비교 실험을 계획합니다.'))


def approach_details():
    return (h('4. Translating Coaching into Vehicle Control')
        + cards([
            ('Observe & Calibrate', 'Use valid repeated runs to establish segment-level speed, steering and pedal patterns. Treat the PP trajectory as a reference, not the only correct human driving style.', '품질 검사를 통과한 반복 기록으로 구간별 속도·조향·페달 패턴을 정리합니다. PP 경로는 비교 기준이며, 사람의 유일한 정답 주행으로 가정하지 않습니다.'),
            ('Define the Action Space', 'Choose whether longitudinal coaching recommends target speed, acceleration or pedal use. Convert Human and Expert signals to compatible units before blending.', '종방향 코칭을 목표속도, 가속도, 페달 조작 중 무엇으로 표현할지 정합니다. 사용자 입력과 기준값을 같은 단위의 명령으로 변환한 뒤 혼합해야 합니다.'),
            ('Separate Help from Protection', 'Design learner-dependent assistance and an independent safety guard. Log intervention reason, magnitude and the final applied command.', '학습자에게 맞춘 도움과 위험을 막는 안전 가드를 분리해 설계합니다. 개입 이유·크기와 최종 적용 명령을 함께 기록합니다.'),
            ('Evaluate without Help', 'After a pilot validates the protocol, examine unassisted driving rather than only the human–AI team result.', '예비 실험으로 절차를 점검한 뒤, 사람과 AI의 공동 성과뿐 아니라 보조 없는 주행 능력을 평가합니다.'),
        ])
        + note('This is the implementation roadmap. The current program supplies recording, PP references and replay; it does not yet run the paper’s skill inference or learned assistance policy.',
            '위 내용은 코칭 구현을 위한 설계 방향입니다. 현재 프로그램은 기록·PP 기준값·리플레이를 제공하며, 논문의 숙련도 추정이나 학습된 개입 정책이 동작하는 상태는 아닙니다.'))


def simulator_controls():
    return (cards([
        ('Manual Driving', 'The driver chooses steering and acceleration/braking through a racing wheel with pedals or a joystick/gamepad.', '레이싱 휠·페달 또는 조이스틱으로 조향과 가속·제동을 직접 조작합니다.'),
        ('Autonomous Reference', 'The implemented autonomous controller uses Pure Pursuit path tracking (PP). It provides a reproducible expert reference for future AI Coaching; autonomy is a supporting component, not the final research goal.', '현재 자율주행에는 Pure Pursuit 경로 추종 방식(이하 PP)을 사용합니다. 향후 AI Coaching에 필요한 전문가 기준을 마련하기 위한 구성 요소이며, 자율주행 자체만을 최종 목표로 삼지는 않습니다.'),
    ])
    + '<div class="device-grid">'
    + media('moza_r5.jpg', 'Racing wheel and pedals: steer with the wheel; accelerate and brake with the pedals.', '레이싱 휠과 페달: 휠로 조향하고 페달로 가속·제동합니다.')
    + media('F710.jpg', 'Joystick / gamepad: use the configured axes and buttons for steering, speed and mode selection.', '조이스틱: 설정된 축과 버튼으로 조향·속도·주행 모드를 조작합니다.') + '</div>'
    + h('Driving Limits & Collision Response')
    + table(['Item', 'Current configuration'], [
        ('Speed', bi('The wheel profile uses a 1 m/s cruise target and accelerator input up to 3 m/s. Braking can bring the target to zero. Actual speed is the vehicle response, not the target itself.', '레이싱 휠 설정에서는 기본 목표속도 1 m/s에서 가속 페달로 최대 3 m/s까지 높입니다. 제동하면 정지할 수 있습니다. 실제 속도는 차량의 반응이므로 목표속도와 다를 수 있습니다.')),
        ('Steering', bi('Normalized command: −1 to +1. The current PP/vehicle configuration uses a 30° (about 0.524 rad) limit in either direction; this is the vehicle steering range, not steering-wheel rotation.', '조향 명령은 −1~+1로 정규화합니다. 현재 PP·차량 설정의 조향 한계는 좌우 각각 30°(약 0.524 rad)입니다. 레이싱 휠의 회전 범위가 아니라 차량의 조향 범위입니다.')),
        ('Collision', bi('A new collision during active control latches a stop: throttle/steering commands remain zero. Check the situation, release mode selection, then explicitly reselect one mode. This does not automatically reset the vehicle or resume a session.', '주행 중 새 충돌이 감지되면 정지 상태를 유지하며 스로틀·조향 명령을 0으로 보냅니다. 상황을 확인하고 모드 선택을 해제한 뒤, 한 가지 모드를 다시 선택해야 합니다. 차량 초기화나 세션 재시작이 자동으로 되는 것은 아닙니다.')),
    ]) + p('Limits and recovery behavior are configuration-specific; these descriptions follow the current research setup.' + cite(5), '위 수치와 복구 동작은 현재 연구용 설정을 기준으로 설명했습니다.' + cite(5)))


def simulator_panels():
    return (h('4. Simulator Side Panels')
        + media('sim_basic_01.png', 'The built-in interface separates environment controls on the left from vehicle and sensor readouts on the right.', '기본 인터페이스는 왼쪽의 환경 조작부와 오른쪽의 차량·센서 표시부로 나뉩니다.')
        + media('sim_01.png', 'Simulator menus and display options.', '시뮬레이터 메뉴와 표시 옵션을 확인하는 영상입니다.', 'sim_01.mp4')
        + cards([
            ('Left · Connection & View', 'IP/port and connection state identify the external control link. The mode, camera, graphics-quality and lighting controls adjust operation and visibility. Reset returns the simulation to its initial state; Quit closes the simulator.', 'IP·포트와 연결 상태로 외부 제어 연결을 확인합니다. 주행 모드, 카메라 시점, 그래픽 품질, 조명 옵션으로 동작과 시야를 조정합니다. Reset은 시뮬레이션을 초기화하고 Quit은 종료합니다.'),
            ('Right · Vehicle & Sensors', 'Time, frame rate, driving mode, gear, speed, throttle and steering expose the current simulated state. Position, IMU/LiDAR readouts and camera preview help inspect the scene and sensor behavior.', '시간·프레임률·주행 모드·기어·속도·스로틀·조향으로 시뮬레이션 상태를 확인합니다. 위치, IMU·LiDAR 표시와 카메라 미리보기는 환경과 센서 동작을 확인하는 데 사용합니다.'),
        ])
        + media('sim_02.png', 'The right-side vehicle and sensor panel updates during driving.', '주행 중 오른쪽 차량·센서 패널의 수치가 갱신되는 모습입니다.', 'sim_02.mp4')
        + p('Lap/collision readouts provide immediate feedback. The built-in Record Data control belongs to the simulator interface; the project’s canonical experiment logs are managed through Experiment Session. Sensor values visible here do not imply that every raw sensor stream is stored in those logs.',
            '랩·충돌 표시는 주행 결과를 바로 확인하는 용도입니다. 기본 화면의 Record Data와 본 프로젝트의 Experiment Session 기록은 구분합니다. 연구용 세션은 Experiment Session에서 관리하며, 기본 화면에 센서가 보인다고 모든 원본 센서 데이터가 세션에 저장되는 것은 아닙니다.'))


def annotated(file, key, en, ko, items):
    """Numbered HTML anchors over an unchanged screenshot, linked to note cards."""
    marks, notes = '', ''
    for i, (x, y, title, english, korean) in enumerate(items, 1):
        marks += f'<a class="annotation-pin" id="{key}-pin-{i}" href="#{key}-note-{i}" style="left:{x}%;top:{y}%" aria-label="{i}: {title}">{i}</a>'
        notes += f'<section class="annotation-note" id="{key}-note-{i}"><h4><a href="#{key}-pin-{i}">{i:02d}</a> · {title}</h4>{p(english,korean)}</section>'
    return f'<figure><div class="annotated-frame"><img src="assets/media/{file}" alt="{en}" data-alt-en="{en}" data-alt-ko="{ko}" loading="lazy">{marks}</div><figcaption>{bi(en,ko)}</figcaption></figure><div class="annotation-notes">{notes}</div>'


def dashboard_guide():
    return annotated('dashboard_pre_01.png','dashboard',
        'Dashboard guide: select a numbered marker to read the matching note. The screenshot has live telemetry but reports a separate session-supervisor connection error.',
        '번호를 선택하면 해당 영역 설명으로 이동합니다. 이 화면은 주행 데이터를 수신하지만 세션 관리 프로그램에는 연결 오류가 표시된 상태입니다.', [
        (57,7,'Toolbar', 'Language and window controls change presentation. Joystick/Racing Wheel select the input stack, Stop stops it, and MAP opens the track view. Live data, session state and recording duration are distinct indicators.', '언어·창 버튼으로 표시 방식을 바꾸고, Joystick/Racing Wheel로 입력 프로그램을 선택합니다. Stop은 입력 프로그램을 중지하고 MAP은 트랙 화면을 엽니다. 실시간 데이터·세션 상태·기록 시간은 서로 다른 상태를 표시합니다.'),
        (3,14,'Experiment Session', 'Configure participant and stage, preflight, start or finish; Abort interrupts the session. This keeps experiment conditions attached to the recorded data.', '참가자·단계를 설정하고 사전 점검 후 기록을 시작·종료합니다. Abort는 세션을 중단합니다. 어떤 조건에서 수집한 기록인지 남기기 위해 마련한 영역입니다.'),
        (24,16,'Connection & Storage', 'Messages, file locations and quality status explain recording readiness. Live telemetry alone does not prove that session recording is ready.', '상태 메시지, 저장 위치, 품질 정보를 통해 기록 준비 상태를 확인합니다. 주행 데이터가 표시된다고 세션 기록까지 준비된 것은 아닙니다.'),
        (49,37,'Driving Readouts', 'Actual/target speed, Human/PP/Applied steering, collisions, laps and clearance show the immediate state before looking at trends.', '실제·목표 속도, Human/PP/Applied 조향, 충돌·랩·전방 거리를 한눈에 확인합니다. 그래프를 자세히 보기 전에 현재 상태를 파악하는 용도입니다.'),
        (24,55,'Time-Series Graphs', 'The speed plot reveals response lag and braking. Steering traces separate intended input, PP reference and applied command, exposing overshoot and repeated corrections.', '속도 그래프는 응답 지연과 감속 과정을, 조향 그래프는 사용자 입력·PP 기준·적용 명령의 차이를 보여 줍니다. 과도한 조향과 반복적인 수정도 확인할 수 있습니다.'),
        (56,90,'Input & Data Quality', 'Input/control details and packet/source ages help distinguish a driving issue from delayed or missing telemetry.', '입력·제어 상세 정보와 패킷·센서 수신 경과 시간으로 주행 문제인지 데이터 지연·누락인지 구분합니다.'),
    ])


def overlay_guide():
    return annotated('overlay_pre_01.png','overlay',
        'Overlay guide: compact live monitoring without leaving the driving view.', '주행 화면에서 바로 확인하는 오버레이입니다. 번호와 아래 설명을 연결해 볼 수 있습니다.', [
        (27,9,'Visibility & Windows', 'Opacity adjusts how much of the driving scene remains visible. MAP toggles the map view; the corner controls manage the overlay window.', '투명도로 주행 화면이 보이는 정도를 조절합니다. MAP으로 맵을 열고 닫으며, 모서리 버튼으로 오버레이 창을 조작합니다.'),
        (5,22,'Session & Control', 'Session opens the separate experiment dialog. Environment, authority and device indicators identify which setup is currently driving.', 'Session으로 별도 실험 설정 창을 엽니다. 환경·제어 모드·입력 장치 표시로 현재 어떤 설정이 차량을 제어하는지 확인합니다.'),
        (50,42,'Speed & Steering', 'Speed and Target compare response with demand. Human/PP/Applied steering distinguishes driver intention, reference and executed command.', 'Speed와 Target으로 실제 속도와 목표속도를 비교합니다. Human/PP/Applied 조향으로 운전자의 의도, 기준 조작, 최종 명령을 구분합니다.'),
        (49,65,'Lap & Clearance', 'Collision and lap counters track the run. Distance helps monitor forward clearance without opening the full dashboard.', '충돌·랩 수치로 주행 상태를 확인합니다. Distance는 전체 대시보드를 열지 않고 전방 여유 거리를 살펴보기 위한 표시입니다.'),
        (5,85,'Reference & Freshness', 'PP state and reference values show whether a reference is available. Packet/odometry ages and drops expose stale data; a visible number alone is not proof of a fresh reading.', 'PP 상태와 기준값으로 비교 기준이 제공되는지 확인합니다. 패킷·위치 데이터 경과 시간과 누락 수는 오래된 데이터를 구분하는 데 사용합니다.'),
    ])


def driving_signals():
    return (h('Why Separate the Driving Signals?')
        + table(['Display', 'Signals', 'What it explains'], [
            ('Speed', 'Actual / Target / PP', bi('Vehicle response, final speed demand and reference speed differ because of acceleration, braking and dynamics.', '실제 반응, 최종 목표속도, PP 기준속도를 비교합니다. 가속·제동·차량 동역학 때문에 세 값이 달라질 수 있습니다.')),
            ('Steering', 'Human / PP / Applied', bi('Driver intention, expert reference and final command need separate traces to identify who caused a correction.', '사용자 입력, PP 기준, 최종 명령을 분리해 어떤 입력이 조향 변화를 만들었는지 확인합니다.')),
            ('Pedals / Throttle', 'Accelerator / Brake / Throttle', bi('Pedal demand and vehicle throttle are not identical. The speed controller translates the demand into an applied throttle command.', '가속·브레이크 페달 입력과 차량의 스로틀 명령은 같은 값이 아닙니다. 속도 제어기가 사용자 요구를 차량 명령으로 변환합니다.')),
        ])
        + p('The central panel groups speed, steering and throttle so the driver can read motion, direction and propulsion separately. Keeping source roles distinct also makes future coaching interventions auditable. PP currently supplies steering/speed references, not a measured pedal input.' + cite(5),
            '중앙 패널은 속도·조향·스로틀을 나눠 차량의 빠르기, 진행 방향, 구동 명령을 따로 읽도록 구성했습니다. 각 값의 출처를 구분해 두면 향후 코칭이 어디에 개입했는지도 확인할 수 있습니다. 현재 PP가 제공하는 것은 조향·속도의 기준값이며, 측정된 페달 입력은 아닙니다.' + cite(5)))
