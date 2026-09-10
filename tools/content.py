"""Reviewed research copy. Headings stay English; prose is paired EN / KO."""
from components import bi, p, h, cite, note, cards, media, table, steps
from research_details import (coaching_math, research_goal_details, approach_details,
    simulator_controls, simulator_panels, dashboard_guide, overlay_guide, driving_signals)

PROJECT = 'AI Driving Coaching for F1TENTH'
RESEARCH_AREA = 'Human–AI Interaction'
UPDATED = '11 Sep 2026'
PERIOD = ('September 2026', '2026년 9월')
TAGLINE = (
    'An AutoDRIVE-based environment for studying how AI assistance can improve independent driving skills.',
    'AI의 도움으로 익힌 운전 기술이 보조 없는 주행에서도 이어지는지 연구하는 AutoDRIVE 기반 실험 환경입니다.')
GROUPS = [
    ('Research', [('index', 'Research Overview'), ('background', 'Research Background'), ('goals', 'Research Questions & Goal'), ('approach', 'Research Approach')]),
    ('Research Environment', [('simulator', 'Simulation & PP Expert'), ('dashboard', 'Dashboard & Overlay'), ('replay', 'Replay Studio'), ('data', 'Data Collection')]),
    ('Research Outlook', [('progress', 'Current Progress'), ('future', 'Future Work'), ('references', 'References')]),
]
PAGES = {}


def page(key, title, en, ko, body):
    PAGES[key] = dict(title=title, lead=(en, ko), body=body)


page('index', 'Research Overview',
     'From assisted driving to independent skill: an environment for measuring what drivers learn.',
     'AI의 도움을 받는 동안뿐 아니라, 혼자 주행할 때도 운전 실력이 향상되는지를 연구합니다.',
     media('sim_pp_01.png',
           'F1TENTH driving with the overlay and bottom-center speed, steering and throttle panel.',
           'F1TENTH 주행 시연입니다. 오버레이와 중앙 하단 패널에서 속도·조향·스로틀을 확인할 수 있습니다.', 'sim_pp_01.gif')
     + h('1. Research at a Glance')
     + p('This project develops an instrumented F1TENTH driving environment in AutoDRIVE.\n\nIt connects human control, a Pure Pursuit (PP) reference controller, experiment sessions and offline replay, so that driver behavior can be examined before designing adaptive coaching.' + cite(2, 5),
         'AutoDRIVE를 바탕으로 수동 주행과 Pure Pursuit(PP) 주행을 기록하고 비교하는 실험 환경을 개발하고 있습니다.\n\n실험 세션 관리와 Replay Studio를 연결해, 코칭을 설계하기 전에 운전자의 조작과 차량의 반응을 살펴볼 수 있도록 했습니다.' + cite(2, 5))
     + p('The research builds on AI Coaching, which studies how assistance can improve a person’s ability to perform independently. This project explores that idea in ground-vehicle driving.' + cite(1),
         '이 연구는 사람이 AI 없이도 더 잘 수행하도록 돕는 AI Coaching 논문에서 출발했습니다. 이를 차량 운전 학습에 적용해, 필요한 순간에 도움을 주면서도 운전자가 스스로 조작하는 능력을 기르도록 하는 것이 목표입니다.' + cite(1))
     + '<div class="facts"><div class="fact"><strong>3 m/s</strong>' + bi('Configured speed ceiling', '설정된 속도 상한') + '</div><div class="fact"><strong>20 Hz</strong>' + bi('Default telemetry collection', '기본 데이터 수집 빈도') + '</div><div class="fact"><strong>5 stages</strong>' + bi('Planned study protocol', '연구 프로토콜 구성') + '</div></div>'
     + cards([
         ('Observe', 'Capture driver inputs, PP references and applied commands as distinct signals.', '사용자 입력·PP 기준값·실제 적용 명령을 구분하여 기록합니다.'),
         ('Compare', 'Use replay and segment analysis to investigate where driving behavior differs.', '리플레이와 구간 분석으로 주행 행동이 달라지는 지점을 확인합니다.'),
         ('Design', 'Develop coaching references and recommendations for steering and pedal use.', '조향과 페달 조작을 위한 코칭 기준과 추천 방식을 설계합니다.'),
         ('Evaluate', 'Plan unassisted checks to assess learning beyond assisted lap performance.', '훈련 후 보조 없이 주행하는 실험을 통해 실제로 운전 실력이 향상됐는지 평가할 계획입니다.'),
     ])
     + note('Current scope: simulation, recording and replay infrastructure. Adaptive coaching and its effect on human learning remain to be implemented and evaluated.' + cite(5),
            '현재는 시뮬레이션, 데이터 기록, 리플레이 분석 환경을 구축한 단계입니다. 학습자에게 맞춰 개입하는 코칭 기능과 학습 효과 검증은 앞으로 진행합니다.' + cite(5)))

page('background', 'Research Background',
     'From an AI that drives for us to an AI that helps us learn to drive.',
     '대신 운전해 주는 AI에서, 스스로 운전하는 법을 익히도록 돕는 AI로.',
     h('1. What Is AI Coaching?')
     + p('AI Coaching asks a different question from conventional driving assistance: not just whether AI can improve performance now, but whether its help leaves the person more capable afterwards. Wang et al. call their reinforcement-learning framework Learning to Coach (L2C).' + cite(1),
         'AI Coaching은 AI가 당장의 수행 결과를 개선하는 데 그치지 않고, 사람이 나중에 도움 없이도 더 잘할 수 있도록 돕는 연구입니다. Wang 등의 논문은 이를 위한 강화학습 기반 프레임워크를 Learning to Coach(L2C)라고 부릅니다.' + cite(1))
     + p('Too much help can remove opportunities to practice. Withdrawing help too early can instead lead to repeated, unproductive failures. The coach therefore learns when to assist and when to leave room for the learner to act.' + cite(1),
         'AI가 모든 실수를 대신 바로잡으면 학습자가 직접 연습할 기회가 줄어듭니다. 반대로 너무 일찍 도움을 끊으면 같은 실패만 반복할 수 있습니다. 따라서 코치는 언제 도와주고, 언제 학습자가 직접 시도하도록 맡길지를 판단해야 합니다.' + cite(1))
     + media('coaching_01.png', 'AI Coaching training and deployment pipeline. Figure 1, Wang et al. (2026).' + cite(1),
             'AI Coaching의 학습 과정과 적용 구조. Wang 등(2026)의 Figure 1.' + cite(1), paper=True)
     + h('2. How Learning to Coach Works')
     + cards([
         ('Expert Policy', 'A pretrained expert provides a competent action. This separates knowing how to perform the task from deciding how much help the learner needs.',
          '미리 학습한 Expert policy가 기준 조작을 제시합니다. 과제를 잘 수행하는 능력과 학습자에게 얼마나 개입할지를 결정하는 능력을 분리한 구조입니다.'),
         ('Adaptive Shared Control', 'The coach blends learner and expert actions with an assistance weight for each control axis. The weight responds to the physical state and learner behavior.',
          'Shared control은 학습자의 입력과 전문가의 조작을 혼합하는 방식입니다. 코치는 현재 상황과 학습자의 행동에 따라 제어 축별 개입 비율을 조절합니다.'),
         ('Learner Model', 'Training combines a skill-dependent action model with probabilistic skill changes after success or failure. These are modeling assumptions, not direct measurements of human learning.',
          '학습 시에는 숙련도에 따른 행동 모델과 성공·실패 이후 숙련도가 변하는 확률 모델을 사용합니다. 사람의 학습 과정을 직접 측정한 값이 아니라, 코치 학습을 위한 모델입니다.'),
         ('Runtime Skill Inference', 'During use, skill is hidden. In the drone experiment, the system updates a skill estimate for each gate segment from its passage time, then adapts assistance.',
          '실제 사용 중에는 숙련도를 직접 알 수 없습니다. 드론 실험에서는 게이트 구간별 통과 시간을 바탕으로 숙련도를 추정하고, 그에 맞춰 도움의 정도를 조절합니다.'),
     ])
     + p('For each control axis, the executed action is a weighted blend: a = λ × a_expert + (1 − λ) × a_human. At λ = 0 the learner has full control; at λ = 1 the expert supplies that axis. Intermediate values allow shared control.' + cite(1),
         '각 제어 축의 적용값은 a = λ × a_expert + (1 − λ) × a_human으로 계산합니다. λ가 0이면 학습자의 입력만, 1이면 전문가의 조작만 적용됩니다. 그 사이에서는 두 입력을 섞어 제어합니다.' + cite(1))
     + p('The learning objective is Value of Independence: how well the learner could perform without the coach. L2C trains the assistance policy with PPO using changes in simulated skill as a practical training reward. The drone implementation also provides visual cues and spoken guidance.' + cite(1),
         '학습 목표는 코치 없이도 얼마나 잘 수행할 수 있는지를 뜻하는 Value of Independence입니다. L2C는 시뮬레이션에서의 숙련도 변화를 학습 보상으로 삼아 PPO로 개입 정책을 학습합니다. 드론 실험에서는 제어 개입과 함께 시각적 안내와 음성 피드백도 제공합니다.' + cite(1))
     + coaching_math()
     + h('3. What the Paper Evaluated')
     + p('The study used an FPV drone-racing simulator with 33 participants, split into three groups of 11. Each participant completed pre-training and post-training tests of two laps each, with up to 15 training laps in between. Participants controlled yaw and roll; pitch and thrust were automated.' + cite(1),
         '논문은 FPV 드론 레이싱 시뮬레이터에서 33명을 대상으로 실험했습니다. 참가자는 11명씩 세 그룹으로 나뉘어 사전·사후 평가를 각각 2랩씩 수행하고, 그 사이에 최대 15랩을 훈련했습니다. 참가자는 yaw와 roll을 조작했으며 pitch와 thrust는 자동 제어했습니다.' + cite(1))
     + table(['Method', 'Assistance strategy', 'Mean lap-time reduction'], [
         ('L2C', bi('Learned, skill- and context-dependent assistance', '숙련도와 상황에 따라 학습된 정책으로 개입'), '27.9%'),
         ('RBF', bi('Rule-based reduction of assistance', '정해진 규칙에 따라 보조 수준을 낮춤'), '11.3%'),
         ('MIA', bi('Minimal correction for safety and task completion', '안전과 과제 수행에 필요한 만큼만 조작을 수정'), '6.2%'),
     ])
     + p('These are the paper’s reported pre-to-post changes, not F1TENTH results. L2C showed significant within-group improvements in both lap time and failures. However, the adjusted between-group comparisons reported p-values of 0.09–0.16; the larger mean gains should not be described as statistically conclusive superiority.' + cite(1),
         '위 수치는 논문에서 보고한 훈련 전후 변화이며 F1TENTH 실험 결과가 아닙니다. L2C 그룹에서는 랩타임과 실패 횟수가 모두 통계적으로 유의하게 개선됐습니다. 다만 그룹 간 비교의 보정된 p값은 0.09~0.16이므로, 평균 개선 폭이 크다는 사실을 통계적으로 확정된 우위로 해석해서는 안 됩니다.' + cite(1))
     + media('ai-coaching-figure2.png',
             'Example drone trajectories before and after training with L2C, RBF and MIA. Crosses mark failures. Individual examples, not group averages. Figure 2, Wang et al. (2026).' + cite(1),
             'L2C·RBF·MIA 훈련 전후의 드론 주행 궤적 예시입니다. × 표시는 실패 지점이며, 그림 속 기록은 그룹 평균이 아닌 개별 예시입니다. Wang 등(2026)의 Figure 2.' + cite(1), paper=True)
     + h('4. Why AutoDRIVE?')
     + media('AutoDRIVE_01.png', 'AutoDRIVE platform identity. Credit: Tinker Twins / AutoDRIVE.' + cite(2,3), 'AutoDRIVE 플랫폼 로고. 출처: Tinker Twins / AutoDRIVE.' + cite(2,3))
     + p('AutoDRIVE Simulator runs on the Unity engine. This project extends the simulator with tools for driving-coaching research.' + cite(2,3), 'AutoDRIVE Simulator는 Unity 엔진으로 구현되어 있습니다. 본 프로젝트는 이 시뮬레이터에 주행 코칭 연구를 위한 기능을 추가합니다.' + cite(2,3))
     + '<div class="platform-diagram">' + media('AutoDRIVE Overview - Dark.png',
             'AutoDRIVE architecture: vehicle and infrastructure communicate with external software through a bridge. Supplied platform diagram; Tinker Twins / AutoDRIVE.' + cite(2,3),
             'AutoDRIVE 구성도입니다. 차량·환경과 외부 소프트웨어를 Bridge로 연결합니다. 제공된 플랫폼 도해의 출처는 Tinker Twins / AutoDRIVE입니다.' + cite(2,3)) + '</div>'
     + cards([
         ('Simulation Side', 'The left side groups the vehicle, sensors, chassis, actuators and infrastructure. Unity provides the simulation engine; these modules expose a virtual driving environment to algorithms.',
          '왼쪽은 차량, 센서, 차체, 구동기와 실험 환경으로 구성됩니다. Unity가 시뮬레이션 엔진을 제공하고, 각 요소를 외부 알고리즘에서 사용할 수 있는 가상 주행 환경으로 구성합니다.'),
         ('Bridge & Software', 'The bridge transfers observations outward and control commands back. The right side separates perception, planning and control; the wider ecosystem also includes smart-city software.',
          'Bridge는 관측 데이터를 외부 소프트웨어로 보내고, 제어 명령을 받아 시뮬레이터에 전달합니다. 오른쪽은 인지·계획·제어 소프트웨어로 나뉘며, 플랫폼 전체에는 스마트시티 관련 소프트웨어도 포함됩니다.'),
     ])
     + p('Here the external control path supplies manual or PP commands, while the telemetry path feeds recording, dashboard and replay. The diagram describes the wider AutoDRIVE ecosystem—not a claim that this project implements every module or uses every listed tool.',
         '본 프로젝트에서는 외부 제어 경로로 사용자 또는 PP 명령을 전달하고, 수신한 데이터를 기록·대시보드·리플레이에 연결합니다. 구성도는 AutoDRIVE 전체 생태계를 설명하며, 본 프로젝트가 그림의 모든 모듈과 도구를 구현·사용한다는 뜻은 아닙니다.')
     + p('AutoDRIVE is an autonomous-driving research and education platform developed by Tinker Twins and collaborators. Its three parts cover algorithm development, simulation and physical testing.' + cite(2, 3),
         'AutoDRIVE는 Tinker Twins와 공동 연구진이 개발한 자율주행 연구·교육 플랫폼입니다. 알고리즘 개발부터 시뮬레이션, 실제 하드웨어 시험까지 연결할 수 있도록 구성되어 있습니다.' + cite(2, 3))
     + table(['Component', 'Role'], [
         ('Simulator', bi('A Unity-based environment for testing vehicle behavior and control algorithms.', 'Unity 기반 가상 환경에서 차량의 움직임과 제어 알고리즘을 시험합니다.')),
         ('Devkit', bi('APIs and development tools that connect algorithms to the simulator or testbed.', '알고리즘을 Simulator 또는 Testbed와 연결하는 API와 개발 도구를 제공합니다.')),
         ('Testbed', bi('Physical vehicles and infrastructure for real-world validation.', '실제 차량과 실험 시설을 이용해 현실 환경에서 검증합니다.')),
     ])
     + p('See Simulation &amp; PP Expert for the built-in side panels and driving controls.', '기본 양측 패널과 주행 조작 방법은 Simulation &amp; PP Expert 페이지에서 자세히 설명합니다.')
     + p('This project uses the Simulator as its foundation, with vehicle control and telemetry connected to external software. The underlying simulator is AutoDRIVE; the experiment-session workflow, dashboard, overlay and Replay Studio are project additions. Physical Testbed transfer has not been evaluated here.' + cite(3, 5),
         '본 프로젝트는 Simulator를 기반으로 외부 프로그램에서 차량을 제어하고 주행 데이터를 수집합니다. 차량과 가상 환경을 제공하는 기반은 AutoDRIVE이며, 실험 세션 관리·대시보드·오버레이·Replay Studio는 본 프로젝트에서 추가한 기능입니다. 실제 Testbed로의 적용은 아직 검증하지 않았습니다.' + cite(3, 5))
     + h('5. From Drone Coaching to Driving Research')
     + p('The research direction is to adapt learning-oriented assistance to steering, speed choice and pedal timing on the ground. A corner, for example, requires a sequence of decisions: when to slow down, how much to steer and when to accelerate again.',
         '본 연구는 학습을 돕는 AI 개입이라는 관점을 차량의 조향·속도 조절·페달 조작에 적용하려 합니다. 예를 들어 코너에서는 감속 시점, 조향량, 다시 가속하는 시점을 연속적으로 판단해야 합니다.')
     + p('The first step is therefore an observable experiment environment. We record human inputs, PP references and applied commands separately, then compare speed and steering by segment. These observations will guide coaching-reference construction and future pedal recommendations.' + cite(5),
         '이를 위해 먼저 운전자의 조작을 기록하고 비교할 수 있는 실험 환경을 구축했습니다. 사용자 입력, PP 기준값, 차량에 적용한 명령을 구분해 기록하고 구간별 속도와 조향을 분석합니다. 이 데이터를 바탕으로 코칭 기준과 향후 페달 조작 추천을 설계할 계획입니다.' + cite(5))
     + note('PP Expert is currently a path-following reference, not the paper’s learned coach. Skill inference, adaptive intervention and an independent coaching safety guard remain future work. Learning must ultimately be evaluated in unassisted driving.',
            '현재 PP Expert는 경로 추종 기준 제어기이며, 논문의 학습된 코치가 구현된 상태는 아닙니다. 숙련도 추정·적응형 개입·코칭용 독립 안전 가드는 향후 개발할 부분입니다. 학습 효과는 최종적으로 보조 없는 주행에서 평가하려 합니다.'))

page('goals', 'Research Questions & Goal',
     'The target is a driver who performs better after assistance is removed.',
     'AI의 도움 없이도 안정적이고 능숙하게 주행할 수 있도록 돕는 것이 목표입니다.',
     '<div class="question">' + bi('When and how should AI intervene so that a driver becomes more capable independently?',
                                   '운전자가 스스로 더 능숙해지려면 AI가 언제, 어떻게 개입해야 할까요?') + '</div>'
     + cards([
         ('RQ1 · Independent Learning', 'Does adaptive coaching improve unassisted post-training driving compared with the initial baseline?', '적응형 코칭을 받은 뒤, 보조 없는 주행 능력이 훈련 전보다 향상되는가?'),
         ('RQ2 · Intervention Timing', 'Which steering, acceleration and braking differences should trigger a recommendation or intervention?', '조향·가속·제동 중 어떤 상황에서 안내하거나 직접 개입해야 하는가?'),
         ('RQ3 · Track Generalization', 'Do improvements transfer between straight-heavy and curve-heavy courses?', '한 코스에서 익힌 기술을 직선이나 커브 비중이 다른 코스에서도 활용할 수 있는가?'),
         ('RQ4 · Visual Guidance', 'Can a reference-path overlay support learning without obstructing the driving view?', '도로 위에 주행 경로를 표시하는 안내가 시야를 가리지 않으면서 학습에 도움이 되는가?'),
     ])
     + h('Final Research Goal')
     + p('Build a reproducible environment that links coaching decisions to observed human behavior and evaluates later unassisted driving. Combine lap outcomes with segment-level speed, steering and pedal analysis to understand both performance and driving technique.',
         'AI가 언제 어떻게 개입했는지와 운전자가 실제로 어떻게 조작했는지를 함께 기록하는 실험 환경을 구축합니다. 랩타임뿐 아니라 구간별 속도·조향·페달 조작을 분석해, 코칭 이후 운전 방식이 어떻게 달라졌는지 살펴보려 합니다.')
     + research_goal_details()
     + h('Evaluation Perspective')
     + table(['Dimension', 'Proposed observation'], [
         ('Performance', bi('Unassisted lap time, completion and actual speed.', '무보조 랩타임·완주·실제 속도.')),
         ('Stability', bi('Collisions, path deviation and steering variation by segment.', '구간별 충돌·경로 이탈·조향 변동.')),
         ('Learning', bi('PRE–POST change and unassisted PROBE performance; repeated trials are needed.', 'PRE–POST 변화와 무보조 PROBE 성능. 반복 실험이 필요합니다.')),
         ('Intervention', bi('Future assistance timing and magnitude, with explicit policy and safety provenance.', '보조 시점과 개입량, 코칭 정책과 안전 장치가 개입한 이유를 기록할 예정입니다.')),
     ])
     + note('These are research questions and planned evaluation dimensions, not established learning outcomes.', '위 내용은 연구 질문과 평가 계획이며, 이미 입증된 학습 결과가 아닙니다.'))

page('approach', 'Research Approach',
     'Drive under controlled conditions, record inputs and responses, then compare the results.',
     '같은 조건에서 주행하고, 입력과 차량의 반응을 기록한 뒤, 결과를 다시 비교합니다.',
     h('1. System Pipeline')
     + '<figure><div class="media-frame diagram"><img src="assets/media/system-pipeline.svg" alt="Human inputs and PP references feed the control and telemetry path; sessions feed dashboard and replay. Future coaching is marked separately."></div><figcaption>'
     + bi('Project architecture schematic. Solid paths represent the existing foundation; the dashed coaching block represents planned work.',
          '시스템 구성도입니다. 실선은 현재 구현된 흐름, 점선은 향후 추가할 코칭 기능을 나타냅니다.') + '</figcaption></figure>'
     + h('2. Experimental Stages') + steps()
     + p('PRE records initial manual performance. EXPERT is an added calibration stage for the PP reference. COACHING, PROBE and POST organize assisted training and unassisted evaluation. \n\nThe five-stage sequence is this project’s adaptation, not a claim that the source paper used this exact protocol.' + cite(1, 5),
         'PRE에서 훈련 전 수동 주행을 기록하고, EXPERT에서 PP의 기준 주행을 확인합니다. 이후 COACHING에서 보조 훈련을, PROBE와 POST에서 훈련 중·후의 보조 없는 주행을 평가하도록 설계했습니다. \n\n다섯 단계는 차량 실험에 맞춰 확장한 절차로, 논문의 실험 순서와는 다릅니다.' + cite(1, 5))
     + note('Stage orchestration is implemented. PRE and EXPERT departure/recording have live validation evidence. Adaptive COACHING and a complete participant study remain pending.',
            '실험 단계를 관리하는 기능은 구현했습니다. PRE와 EXPERT는 시뮬레이터에서 출발·기록 동작을 확인했으며, 적응형 코칭과 전체 참가자 실험은 아직 진행하지 않았습니다.')
     + h('3. Separate the Signals')
     + table(['Signal', 'Meaning'], [
         ('Human', bi('The steering or pedal input requested by the driver.', '운전자가 입력한 조향값과 페달 조작값.')),
         ('PP Expert', bi('Reference steering and speed from the path-following controller.', 'PP 경로 추종 제어기가 계산한 기준 조향값과 속도.')),
         ('Applied', bi('The final command sent to the vehicle, not measured physical wheel-angle feedback.', '차량에 전달한 최종 제어 명령입니다. 실제 바퀴의 조향각을 측정한 값과는 다릅니다.')),
     ])
     + p('Recorded differences support reference design. They are not automatically interpreted as learner skill or proof of coaching intervention.' + cite(5),
         '사용자와 PP의 차이는 코칭 기준을 마련하는 참고 자료입니다. 차이가 크다는 이유만으로 운전 실력이 부족하다거나 코칭이 개입했다고 판단하지 않습니다.' + cite(5))
     + approach_details())

page('simulator', 'Simulation & PP Expert',
     'Compare manual driving and PP reference driving in the same simulator.',
     '같은 시뮬레이터에서 사람의 수동 주행과 PP의 기준 주행을 비교합니다.',
     media('sim_pre_01.png', 'Manual driving with the overlay and central driving-data panel.',
           '수동 주행 시연입니다. 운전 화면 위에 오버레이와 중앙 주행 데이터 패널을 함께 표시합니다.', 'sim_pre_01.gif')
     + h('1. Simulation Foundation')
     + p('Manual and autonomous-reference driving share the same AutoDRIVE simulation, built on Unity. The autonomous component supports the wider AI Coaching research goal.' + cite(2,3,5),
         'Unity 기반 AutoDRIVE 안에서 수동 주행과 자율 기준 주행을 비교합니다. 자율주행 기능은 AI Coaching 연구에 필요한 기준을 마련하기 위한 것입니다.' + cite(2,3,5))
     + simulator_controls()
     + h('2. Pure Pursuit Reference')
     + p('Pure Pursuit steers toward a look-ahead point on a reference path. This project combines that steering method with speed planning in the PP Expert controller.\n\nThe configured reference speed range is 1–3 m/s, with a 3 m/s ceiling; actual speed depends on vehicle dynamics and control.' + cite(4, 5),
         'Pure Pursuit는 기준 경로의 전방 목표점을 향해 조향하는 경로 추종 방식입니다. 본 프로젝트의 PP Expert는 이 조향 방식에 속도 계획을 결합해 비교용 기준값을 제공합니다.\n\n기준 속도 범위는 1~3 m/s, 상한은 3 m/s이며 실제 속도는 차량 동역학과 제어의 영향을 받습니다.' + cite(4, 5))
     + media('sim_pp_01.png', 'PP-controlled driving demonstration in AutoDRIVE. Autonomous reference driving is distinct from human coaching.',
             'PP Expert의 자율주행 시연입니다. 사람에게 개입하는 코칭이 아니라, 비교 기준을 만들기 위한 주행입니다.', 'sim_pp_01.gif')
     + h('3. Reference Path & Track View')
     + media('map_pp.png', 'Track position and reference path during PP driving.', 'PP 주행 중 차량 위치와 기준 경로를 확인하는 맵 화면입니다.', 'map_pp_01.gif', compact=True)
     + p('Track identity and reference-path versions matter when comparing recordings. New straight-heavy and curve-heavy maps are planned for broader data collection; the current demonstrations do not establish transfer across tracks.',
         '기록을 비교할 때 같은 트랙과 기준 경로 버전인지 확인해야 합니다. 직선 중심·커브 중심 맵을 추가해 데이터를 확장할 예정이며, 현재 시연만으로 트랙 간 일반화가 입증된 것은 아닙니다.')
     + simulator_panels())

page('dashboard', 'Dashboard & Overlay',
     'The experimenter monitors the dashboard; the driver sees the same data in the overlay.',
     '같은 주행 데이터를 실험자는 대시보드에서, 운전자는 오버레이에서 확인합니다.',
     media('dashboard_pre_01.png', 'Full dashboard: session controls, speed/steering traces and sensor status. Session-supervisor connectivity and live telemetry are separate status indicators.',
           '대시보드에서 실험 설정, 속도·조향 그래프, 센서 상태를 확인합니다. 세션 관리 프로그램과 주행 데이터의 연결 상태는 각각 표시합니다.', 'dashboard_pre_01.gif')
     + p('The dashboard and overlay update from the simulator’s live telemetry. Their values follow the current run, but sensor arrival times can differ; live synchronization does not mean every sensor was sampled at exactly the same instant.', '대시보드와 오버레이는 시뮬레이터의 주행 데이터를 실시간으로 수신해 갱신합니다. 현재 주행과 연동되지만 센서별 수신 시각에는 차이가 있으므로, 모든 값이 정확히 같은 순간에 측정됐다는 뜻은 아닙니다.')
     + dashboard_guide()
     + h('1. Experiment Dashboard')
     + cards([
         ('Session Control', 'Set participant ID, stage, trial, target laps and departure delay. Configure, preflight, start and finish the recording.', '참가자 ID, 실험 단계, Trial(시도 번호), 목표 랩, 출발 대기 시간을 설정합니다. 사전 점검 후 기록을 시작하거나 종료할 수 있습니다.'),
         ('Live Monitoring', 'Inspect actual/target speed, Human/PP/Applied steering, lap/collision counters and source freshness.', '실제·목표 속도와 Human/PP/Applied 조향값을 확인합니다. 랩·충돌 횟수와 데이터가 정상적으로 갱신되는지도 살펴볼 수 있습니다.'),
     ])
     + h('2. Overlay & Driving Panel')
     + media('overlay_pre_01.png', 'Compact overlay for session, lap and vehicle status during driving.', '시뮬레이터 위에 표시되는 오버레이입니다. 주행 화면을 벗어나지 않고 세션·랩·차량 상태를 확인합니다.', 'overlay_pre_01.gif', compact=True)
     + overlay_guide()
     + media('panel_pre_01-poster.png', 'Bottom-center panel with speed, steering and throttle. PP reference values exist for speed and steering; there is no PP pedal recommendation in the current interface.',
             '운전 화면 중앙 하단에 배치한 속도·조향·스로틀 패널입니다. 현재 PP는 속도와 조향의 기준값을 제공하며, 페달을 얼마나 밟을지에 대한 추천은 아직 제공하지 않습니다.', 'panel_pre_01.gif', compact=True)
     + driving_signals()
     + h('3. Reproducible Departure')
     + steps()
     + p('PRE records initial manual driving; EXPERT records the autonomous reference. COACHING is planned assisted training, PROBE an unassisted check during training, and POST the final unassisted evaluation. Stage names define the study workflow; selecting COACHING does not activate an unimplemented policy.', 'PRE는 초기 수동 주행, EXPERT는 자율 기준 주행을 기록합니다. COACHING은 보조 훈련, PROBE는 훈련 중 보조 없는 점검, POST는 훈련 후 최종 평가로 계획했습니다. 단계 이름은 실험 절차를 구분하며, COACHING 선택만으로 아직 구현되지 않은 정책이 동작하지는 않습니다.')
     + p('A consistent reset and countdown give the driver time to move to the wheel before the vehicle is released. Readiness and release events are recorded so the start sequence can be checked separately from lap performance.', '차량을 초기화한 뒤 카운트다운 동안 기다리도록 해, 운전자가 휠 자리로 이동하고 출발을 준비할 시간을 확보합니다. 준비 완료와 출발 이벤트도 기록하므로 시작 절차와 랩 성능을 따로 확인할 수 있습니다.')
     + p('Departure delay is configurable from 1 to 120 seconds (15 seconds by default).\n\nThe start workflow resets the vehicle and run counters, holds motion during the countdown, and releases driving after readiness checks. The separate overlay session dialog hides after START is acknowledged.' + cite(5),
         '출발 대기 시간은 1~120초로 설정할 수 있으며 기본값은 15초입니다.\n\n기록 시작을 요청하면 차량과 주행 수치를 초기화하고, 카운트다운 동안 차량을 정지시킵니다. 준비 상태를 확인한 뒤 주행을 시작하며, 오버레이의 별도 세션 창은 시작 요청이 승인되면 자동으로 닫힙니다.' + cite(5))
     + '<div class="session-image-grid">'
     + media('dashboard_exp_01.png', 'Set the participant, trial, lap target and departure delay in the experiment session panel.',
             '실험 세션 패널에서 참가자, Trial, 목표 랩과 출발 대기 시간을 설정합니다.')
     + media('dashboard_exp_02.png', 'Open Stage to select PRE, EXPERT, COACHING, PROBE or POST. Selecting a stage does not activate an unimplemented coaching policy.',
             'Stage 목록을 열어 PRE, EXPERT, COACHING, PROBE, POST 중 실험 단계를 선택합니다. 단계 선택만으로 아직 구현되지 않은 코칭 정책이 활성화되지는 않습니다.')
     + '</div>')

page('replay', 'Replay Studio',
     'Inspect recorded driving, from the full trajectory to a single control signal.',
     '전체 궤적부터 개별 제어 신호까지, 기록된 주행을 살펴봅니다.',
     media('replay_02.png', 'Replay map view: the two recorded trajectories and their current observed positions.',
           'Replay Studio의 맵 화면입니다. 두 기록의 주행 궤적과 현재 재생 시점에 해당하는 차량 위치를 보여 줍니다.', 'replay_02.gif')
     + h('1. Select, Import & Compare')
     + p('Select the recorded map first, then choose A/B sessions and import them. A/B designate the two selected recordings, not fixed Human/Expert roles.\n\nPRE–PRE and EXPERT–EXPERT comparisons are supported; before/after order is selected by the researcher.' + cite(5),
         '기록된 맵을 먼저 선택한 뒤 A/B 세션을 골라 불러옵니다. A/B는 선택한 두 기록이며 Human/Expert 역할로 고정되지 않습니다.\n\nPRE–PRE와 EXPERT–EXPERT도 비교할 수 있고, 전후 순서는 연구자가 지정합니다.' + cite(5))
     + media('replay_01.png', 'Selecting a map filters the available sessions.', '첫 화면에서 맵을 선택하면 해당 맵에서 기록한 세션을 불러올 수 있습니다.')
     + media('replay_06.png', 'Select one recording in A and one in B, then press Import.', 'A와 B에 비교할 세션을 각각 선택한 뒤 Import를 누릅니다.')
     + cards([
         ('01 · Select A', 'Choose the first recording from the map-filtered list. Stage, date/time and trial help identify the intended run; the folder button can select a session directly.', '선택한 맵의 목록에서 첫 번째 기록을 고릅니다. 단계·기록 시각·Trial로 원하는 주행을 확인하고, 폴더 버튼으로 세션을 직접 지정할 수도 있습니다.'),
         ('02 · Select B & Import', 'Choose the comparison recording in B, then click Import. Both selections are required. A/B can be two manual runs or two expert runs, not only human versus autonomous.', 'B에서 비교할 기록을 고른 다음 Import를 누릅니다. 두 기록을 모두 선택해야 합니다. 수동 주행끼리, 자율 기준 주행끼리도 비교할 수 있습니다.'),
     ])
     + h('2. Signal Analysis')
     + cards([
         ('Speed', 'Compare Actual, Target and PP speed to locate deceleration onset, minimum corner speed, acceleration recovery and lag behind the target. Check the pedal traces to distinguish braking from other causes of slowing.', 'Actual·Target·PP 속도로 감속 시작점, 코너 최저 속도, 가속 재개 시점과 목표 속도에 대한 응답 지연을 확인합니다. 브레이크로 감속한 것인지 구분하려면 페달 기록도 함께 살펴봐야 합니다.'),
         ('Steering', 'Human, PP and Applied traces reveal turn-in timing, peak steering and repeated left/right corrections. A deviation from PP is a comparison signal, not automatically a driving error.', 'Human·PP·Applied로 코너 진입 조향 시점, 최대 조향량, 좌우 반복 수정을 확인합니다. PP와 다르다는 이유만으로 잘못된 조작이라고 판단하지는 않습니다.'),
         ('Pedals / Throttle', 'Compare accelerator and brake use with throttle output to inspect pedal-release timing, braking duration and re-acceleration. Throttle is the control output, not the pedal position.', '가속·브레이크 입력과 스로틀 출력으로 페달을 놓는 시점, 제동 지속 시간, 재가속 시점을 확인합니다. 스로틀은 제어 출력이며 페달을 밟은 깊이와 같은 값이 아닙니다.'),
         ('Events & Windows', 'Seek recorded events and compare selected passages. Missing values remain unavailable rather than becoming zero.', '기록된 이벤트 시점으로 이동하거나 원하는 구간을 골라 비교합니다. 수집되지 않은 값은 0으로 채우지 않고 데이터 없음으로 처리합니다.'),
     ])
     + media('replay_04.png', 'Switching between graph modes in Replay Studio.', 'Replay Studio의 그래프 모드를 전환하며 각 데이터를 확인하는 영상입니다.', 'replay_04.mp4')
     + h('3. Playback & Alignment')
     + media('replay_03.png', 'Playback controls, alignment and segment navigation.', '재생 조작, 비교 기준과 구간 이동을 확인하는 영상입니다.', 'replay_03.mp4')
     + p('Time alignment compares the runs at the same elapsed time. Position alignment compares observations at similar progress along the reference path, which helps when lap speeds differ.\n\nDetailed plots still use the selected window’s elapsed time; their vertical cursors show the currently observed sample.', 'Time alignment는 같은 경과 시간끼리, Position alignment는 기준 경로상의 비슷한 진행 위치끼리 비교합니다. 주행 속도가 다른 기록을 같은 코스 구간에서 살펴볼 때 위치 기준이 유용합니다.\n\n상세 그래프의 가로축은 선택 구간의 경과 시간이며, 세로선이 현재 관측 시점을 가리킵니다.')
     + p('Restart, skip −5/+5 seconds, play/pause and change playback rate. The replay ends at the later recording endpoint; an earlier-ended recording holds its last observed position. \n\nTime/position alignment and segment navigation support inspection, while detailed plots use elapsed time in their selected windows.' + cite(5),
         '처음으로 이동, 5초 앞뒤 이동, 재생·일시정지, 배속 조절을 지원합니다. 두 기록이 모두 끝날 때까지 재생하며, 먼저 끝난 차량은 마지막으로 기록된 위치에 머뭅니다. \n\n시간 또는 경로상의 위치를 기준으로 비교할 수 있고, 상세 그래프는 선택한 구간의 경과 시간을 기준으로 표시합니다.' + cite(5))
     + note('Replay is an offline, read-only analysis tool. The supplied screen recordings illustrate functions; one A/B comparison does not demonstrate coaching effectiveness.',
            'Replay Studio는 저장된 기록을 읽어 분석하는 오프라인 도구로, 차량을 제어하거나 원본 기록을 수정하지 않습니다. 한 쌍의 주행 비교만으로 코칭의 학습 효과를 판단하지는 않습니다.'))

page('data', 'Data Collection',
     'Record driver inputs, PP references and applied commands as separate signals.',
     '운전자의 입력, PP의 기준값, 차량에 적용한 명령을 따로 기록합니다.',
     h('1. Observable Data')
     + table(['Data group', 'Recorded / derived meaning'], [
         ('Driving', bi('Actual and target speed, pose, lap progress, collisions and resets.', '실제·목표 속도, 위치, 랩 진행, 충돌과 초기화.')),
         ('Control', bi('Human/PP/Applied steering, accelerator, brake and throttle command.', 'Human/PP/Applied 조향, 가속 페달, 브레이크와 스로틀 명령.')),
         ('Reference & Context', bi('Track and path identifiers, projected progress and segment passages where valid.', '트랙·경로 식별자, 기준 경로상 진행 위치와 구간 통과 기록. 계산 조건을 만족한 경우에만 기록합니다.')),
         ('Session & Quality', bi('Protocol stage, timestamps, source freshness, missing fields and events.', '실험 단계, 기록 시각, 데이터 갱신 상태, 누락 항목과 이벤트.')),
         ('Future Coaching', bi('Nullable assistance and safety fields await actual policy/guard producers.', '향후 보조·안전 개입을 기록할 항목입니다. 해당 기능이 실제로 값을 보내기 전에는 비워 둡니다.')),
     ])
     + p('The collector defaults to 20 Hz sampling of the latest received values. This is not synchronized acquisition of every sensor.\n\nSource ages and timestamps help interpret freshness; a missing value is not a measured zero.' + cite(5),
         '기본 설정에서는 초당 20회, 가장 최근에 받은 값을 기록합니다.\n\n모든 센서를 같은 순간에 측정하는 방식은 아니므로, 각 값이 언제 갱신됐는지도 함께 확인해야 합니다. 데이터가 없는 상태와 실제 측정값이 0인 상태는 구분합니다.' + cite(5))
     + h('2. From Sessions to Segments')
     + cards([
         ('Whole Recording', 'Review lap time, mean/maximum actual speed, mean target speed, collisions and completion state.', '랩타임, 실제 속도 평균·최댓값, 목표 속도 평균, 충돌과 종료 상태를 확인합니다.'),
         ('Segment Passages', 'Examine local speed, steering variation, path deviation and Human–PP differences. Match passages explicitly.', '구간별 속도, 조향 변화, 기준 경로와의 거리, 사용자와 PP의 차이를 살펴봅니다. 서로 대응하는 구간을 선택해 비교합니다.'),
     ])
     + h('3. Quality Before Interpretation')
     + p('Before analysis, checks flag altered or missing files, missing data, stale readings, recording gaps and stage/mode mismatches. These checks assess whether a recording is suitable for analysis; they do not certify driving safety or prove a coaching effect.' + cite(5),
         '분석 전에 파일이 변경되거나 누락되지 않았는지, 필요한 항목이 수집됐는지, 기록 간격과 실험 단계·주행 모드가 일치하는지 점검합니다. 이 품질 검사는 기록을 분석에 사용할 수 있는지 확인하는 절차이며, 주행 안전이나 코칭 효과를 보장하는 검사는 아닙니다.' + cite(5))
     + note('The contract does not currently add raw camera streams, full LiDAR scans or physical actuator feedback to each telemetry sample. IMU is optional and needs live frame/coverage verification. Historical provenance mismatches remain visible.',
            '현재 기록 형식에는 원본 카메라 영상, 전체 LiDAR 스캔, 구동기의 실제 움직임을 측정한 값이 포함되지 않습니다. IMU는 선택적으로 수집하며 좌표계와 수집 상태를 추가 확인해야 합니다. 과거 기준 주행의 파일·버전 정보가 맞지 않는 문제도 별도로 남겨 둡니다.'))

page('progress', 'Current Progress',
     'Driving can now be recorded and reviewed. The next step is to use these observations to design coaching.',
     '주행 데이터를 수집하고 분석하는 환경을 마련했습니다. 다음 단계는 이 데이터를 활용한 코칭 설계입니다.',
     p('Implementation snapshot: 11 September 2026. The status below combines current project documentation, source checks and recorded development validation. It is not a participant-study result.' + cite(5),
       '2026년 9월 11일 기준 개발 현황입니다. 프로젝트 문서와 소스 코드, 시뮬레이터 구동 기록을 대조해 정리했으며, 참가자 대상 코칭 실험의 결과는 아닙니다.' + cite(5))
     + table(['Component', 'Status', 'Evidence / boundary'], [
         ('Simulator & PP', '<span class="status">Implemented</span>', bi('Manual and PP driving; latest PRE/EXPERT live evidence exists. Historical baseline hashes still need reconciliation.', '수동·PP 주행과 PRE/EXPERT 기록을 확인했습니다. 과거 기준 주행의 파일 해시·버전 정보는 추가 확인이 필요합니다.')),
         ('Dashboard & Overlay', '<span class="status">Implemented</span>', bi('Live views, bottom-center panel and experiment session controls.', '실시간 화면, 중앙 하단 패널과 실험 세션 제어.')),
         ('Departure Workflow', '<span class="status">Checked in simulator</span>', bi('Reset, configurable countdown and PRE/EXPERT recording checked in the simulator.', '시뮬레이터에서 초기화, 대기 시간 설정, PRE/EXPERT 기록 동작을 확인했습니다.')),
         ('Replay Studio', '<span class="status">Implemented</span>', bi('Map selection, session import, A/B comparison, detailed signals and playback.', '맵 선택 후 세션 불러오기, A/B 비교, 상세 데이터 확인과 재생을 지원합니다.')),
         ('Research Data', '<span class="status">Under validation</span>', bi('The data contract and quality checks are implemented; optional sensors and future coaching outputs still require integration and validation.', '수집 항목·형식과 품질 검사를 구현했습니다. 선택 센서와 향후 코칭 데이터는 추가 연결·검증이 필요합니다.')),
         ('Adaptive Coaching', '<span class="status planned">Planned</span>', bi('Policy, pedal recommendations and independent safety guard remain future work.', '학습자에게 맞춘 개입 정책, 페달 조작 추천, 코칭용 독립 안전 가드는 개발 예정입니다.')),
         ('Human Learning Study', '<span class="status planned">Planned</span>', bi('No project-level coaching efficacy result is claimed.', '본 프로젝트의 코칭 학습 효과 결과는 아직 제시하지 않습니다.')),
     ])
     + h('What the Current Environment Enables')
     + p('A researcher can inspect a manual or reference run, examine the corresponding live signals, record a controlled departure, and reopen the resulting sessions for comparison. This closes the engineering loop from driving to review, which will support coaching-reference construction.',
         '현재는 동일한 출발 절차로 수동·PP 주행을 기록하고, 실시간 데이터를 확인한 뒤 Replay Studio에서 다시 비교할 수 있습니다. 앞으로 이 과정을 반복해 코칭 설계에 필요한 기준 데이터를 쌓을 계획입니다.')
     + media('replay_01.png', 'Replay Studio in use: review a recorded drive without reconnecting to the simulator.', '시뮬레이터에 다시 연결하지 않고 저장된 주행을 확인하는 Replay Studio입니다.', 'replay_01.mp4'))

page('future', 'Future Work',
     'Build coaching references, broaden the driving tasks and investigate intuitive guidance.',
     '코칭 기준을 구축하고, 주행 과제를 다양화하며, 직관적인 안내 방식을 검토합니다.',
     cards([
         ('01 · Coaching Reference & Control', 'Build a coaching reference dataset. Design recommendations for speed, steering and pedal timing, and decide when guidance should become direct intervention.', '코칭 기준 데이터를 구축하고 적절한 속도, 조향량, 가속·제동 시점을 추천하는 방식을 설계합니다. 안내만 할 때와 직접 개입할 때의 기준도 정할 계획입니다.'),
         ('02 · Maps & Data Collection', 'Create curve-heavy, straight-heavy and mixed courses. Collect repeated driving records under documented conditions and compare behavior by segment.', '커브 중심·직선 중심·혼합 코스를 제작합니다. 같은 실험 조건에서 반복 주행을 기록하고 구간별 조작을 비교합니다.'),
         ('03 · Visual Driving Guidance', 'Explore a reference trajectory drawn on the road. Examine visibility, distraction and whether guidance supports independent learning.', '시뮬레이터의 도로 위에 따라갈 경로를 표시하는 방식을 검토합니다. 안내가 잘 보이는지, 운전에 방해가 되지 않는지, 보조 없는 주행에도 도움이 되는지 확인할 계획입니다.'),
         ('04 · Coaching Evaluation', 'Connect actual policy and safety outputs to the data contract, then pilot the protocol and evaluate later unassisted driving.', '코칭 정책과 안전 가드의 실제 출력을 기록하도록 연결합니다. 이후 예비 실험으로 절차를 점검하고, 훈련 후 보조 없는 주행 능력을 평가할 계획입니다.'),
     ])
     + p('First curate repeated manual and reference recordings and verify their path and controller versions. Then define compatible steering and longitudinal actions, prototype recommendations, and connect direct intervention with a separate safety guard.\n\nNew maps and visual guidance should be tested under the same documented protocol.', '먼저 수동 주행과 기준 주행의 반복 기록을 정리하고 경로·제어기 버전을 확인합니다. 이후 조향과 종방향(가속·제동) 명령의 단위를 정의하고 추천 기능을 시험한 뒤, 직접 개입과 별도 안전 가드를 연결할 계획입니다.\n\n새 맵과 경로 안내도 같은 실험 절차에 따라 검증합니다.')
     + h('Next Research Sequence')
     + '<div class="steps">' + ''.join(f'<div class="step future"><strong>{t}</strong>{p(e,k)}</div>' for t,e,k in [
         ('Reference','Curate valid observations','분석 가능한 주행 기록 정리'),('Recommend','Speed / steering / pedals','속도·조향·페달 추천'),('Diversify','Collect across tracks','다양한 트랙에서 수집'),('Pilot','Test the protocol','프로토콜 예비 검증'),('Evaluate','Measure independent skill','보조 없는 주행 능력 평가')]) + '</div>'
     + note('The trajectory overlay is a design direction under consideration. Existing PP path/minimap displays should not be mistaken for the proposed on-road guidance overlay.',
            '주행 궤적 오버레이는 검토 중인 설계 방향입니다. 현재 PP 경로·미니맵 표시와 향후 도로 위 안내 오버레이는 구분합니다.'))

references = [
    (1, 'AI Coaching · Source Paper',
     'Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, and Rahul Mangharam. “AI Coaching for Accelerating Human Skill Development with Reinforcement Learning.” arXiv:2606.25337v1, 24 June 2026.',
     'https://arxiv.org/abs/2606.25337v1',
     'Source for the coaching approach and reproduced Figures 1 and 2. This is a preprint; its drone-racing results are not results of this project.',
     '코칭 접근 방식과 Figure 1·2의 출처입니다. arXiv에 공개된 사전 공개 논문(preprint)이며, 논문의 드론 실험 결과와 본 프로젝트의 결과는 구분합니다.'),
    (2, 'AutoDRIVE · Ecosystem', 'Tinker Twins. AutoDRIVE Ecosystem: official research and education platform.',
     'https://autodrive-ecosystem.github.io/', 'Source for Simulator / Devkit / Testbed roles and platform imagery.', 'Simulator·Devkit·Testbed 역할과 플랫폼 이미지의 출처입니다.'),
    (3, 'AutoDRIVE · Software & Publication',
     'Tinker-Twins/AutoDRIVE. See also T. Samak, C. Samak, S. Kandhasamy, V. Krovi, and M. Xie, Robotics 12(3), 77 (2023), doi:10.3390/robotics12030077.',
     'https://github.com/Tinker-Twins/AutoDRIVE', 'Original software repository, attribution and upstream license information.', 'AutoDRIVE 원본 저장소입니다. 개발자 정보와 원본 라이선스를 확인할 수 있습니다.'),
    (4, 'Pure Pursuit · Algorithm', 'R. Craig Coulter. “Implementation of the Pure Pursuit Path Tracking Algorithm.” CMU-RI-TR-92-01, 1992.',
     'https://www.ri.cmu.edu/publications/implementation-of-the-pure-pursuit-path-tracking-algorithm/', 'Source for the path-following algorithm, not evidence for this project’s performance.', '경로 추종 알고리즘의 출처이며 본 프로젝트 성능의 실험 증거는 아닙니다.'),
    (5, 'Project · Implementation Snapshot', 'F1TENTH AI Coaching development evidence, reviewed 11 September 2026.',
     'docs/EVIDENCE.md', 'Local source and documentation register. Unpublished engineering evidence; raw participant records are not distributed with this website.', '웹페이지 작성 시 확인한 프로젝트 문서와 소스 코드 목록입니다. 개발 과정의 확인 자료이며, 참가자의 원본 주행 기록은 사이트에 포함하지 않습니다.'),
    (6, 'AiX Lab · Design Reference', 'AiX Lab, Gyeongsang National University. Formal Methods for AI and CPS research page.',
     'https://aix.gnu.ac.kr/research/formal-methods/', 'Reference for the black background, sidebar, language tabs and English heading convention. Lab logo: AiX Lab.', '검정 배경·사이드바·언어 탭·영문 제목 유지 규칙의 디자인 참고입니다. 연구실 로고의 출처는 AiX Lab입니다.'),
]
page('references', 'References & Credits',
     'External research, platform contributions and local implementation evidence are identified separately.',
     '참고 논문, 기반 플랫폼, 프로젝트 구현 자료의 출처를 구분해 정리했습니다.',
     ''.join(f'<section class="reference" id="ref-{n}"><h3 data-heading>[{n}] {title}</h3><p>{desc}</p><p><a href="{url}">{"Open evidence register" if n==5 else "Open source ↗"}</a></p>{p(en,ko)}</section>' for n,title,desc,url,en,ko in references)
     + h('Media & Attribution')
     + p('Simulator, dashboard and replay captures were supplied for this research page and show the project’s AutoDRIVE-based workflow. AutoDRIVE illustrations belong to their respective creators; the paper figures are credited to Wang et al. Lab branding retains the supplied artwork. Captions identify the demonstration context.',
         '시뮬레이터·대시보드·리플레이 캡처는 이 페이지용으로 제공되었으며 AutoDRIVE 위에서 동작하는 프로젝트 인터페이스를 보여줍니다. AutoDRIVE 도해는 원 제작자, 논문 그림은 Wang 등의 연구진에게 출처를 표기합니다. 연구실 로고는 원본을 유지하며 캡션에 시연 맥락을 명시합니다.')
     + '<p><a href="docs/ASSET_CREDITS.md">Asset credits &amp; source mapping</a> · <a href="docs/EVIDENCE.md">Implementation evidence</a></p>')
