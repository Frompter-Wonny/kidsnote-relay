# Kidsnote Relay

> **한국어 안내** · [English](#english)

로그인된 PC의 키즈노트·유치원·학교·학원 부모 포털에서 최신 공지를 확인하고, 보호자가 실제로 해야 할 일만 짧게 정리하는 [Hermes Agent](https://github.com/NousResearch/hermes-agent)용 선택형 스킬입니다.

## 무엇을 해주나요?

- 화면에서 **로그인된 기관·자녀·반 또는 공지 영역**을 확인한 뒤 공지를 읽습니다.
- 기본적으로 **확인 당일과 전날에 게시된 공지**를 확인합니다.
- 공지의 **게시 시각**, 실제 **행사일**, **제출·회신 마감일**을 혼동하지 않도록 분리합니다.
- 제목이나 알림 미리보기만 보지 않고, 본문과 필요한 이미지·PDF·표를 확인합니다.
- 아래처럼 보호자가 행동할 항목만 추립니다.
  - 준비물·복장
  - 동의서·설문·신청·제출과 기한
  - 등원·하원·픽업·시간 변경
  - 행사·체험·휴원 일정
  - 건강·안전 요청과 비용 안내

## 하지 않는 일

- 비밀번호, OTP, 쿠키, 토큰을 요청하거나 저장하지 않습니다.
- 로그인·CAPTCHA·MFA·접근 제한을 우회하지 않습니다.
- 별도 요청 없이 동의서 제출, 회신, 결제, 예약, 외부 공유를 실행하지 않습니다.
- 예전 요약이나 알림 미리보기를 최신 공지의 근거로 사용하지 않습니다.
- 공지에 없는 일반적 준비물·복장 조언을 추측해서 덧붙이지 않습니다.

## 설치

이 저장소의 아래 디렉터리를 Hermes 프로필의 스킬 폴더에 복사합니다.

```text
optional-skills/productivity/parent-portal-notice-brief/
```

대상 위치는 다음과 같습니다.

```text
~/.hermes/skills/productivity/parent-portal-notice-brief/
```

복사한 뒤에는 새 Hermes 세션을 시작해야 스킬 목록에 반영됩니다.

## 사용 예시

다음처럼 요청합니다.

> 오늘 키즈노트 공지를 확인해서 부모가 해야 할 것만 알려줘.

> 어제와 오늘 공지에서 준비물·제출 기한·등하원 변경만 정리해줘.

출력은 이런 형태입니다.

```markdown
## 부모 포털 공지 요약

기준:
- 확인 시각: 2026-09-18 16:05 KST
- 포함 게시일: 2026-09-18, 2026-09-17

해야 할 일:
- [2026-09-20] 현장체험 동의서 제출
  — 근거: 가을 현장체험 안내 (게시 2026-09-18 14:12)

준비물·복장:
- [2026-09-24] 물병·모자·흰 운동화

일정·등하원:
- [2026-09-24 09:00] 현장체험 출발

건강·안전·비용:
- 확인된 항목 없음
```

예시에 포함된 날짜·이름·공지 내용은 모두 가공된 예시입니다.

## 개인정보과 안전

이 스킬은 아이의 사진, 이름, 반, 연락처, 공지 원문을 불필요하게 외부로 옮기지 않도록 설계되었습니다. 다른 사람에게 공유하거나 전송하는 일은 보호자가 명시적으로 요청한 경우에만, 필요한 내용만 최소한으로 다룹니다.

## 저장소 구성

```text
optional-skills/productivity/parent-portal-notice-brief/SKILL.md
references/freshness-and-date-rules.md
templates/parent-brief-template.md
tests/fixtures/synthetic-school-notice.md
tests/test_skill_structure.py
```

## 라이선스

[MIT License](LICENSE)

---

<a id="english"></a>

## English

A privacy-first optional [Hermes Agent](https://github.com/NousResearch/hermes-agent) skill that checks an already logged-in PC parent portal—including Kidsnote—and produces a compact brief of actions a parent needs to take.

### What it does

- Verifies the visible logged-in portal context before reading notices.
- Reviews notices posted today and the previous calendar day by default.
- Separates post time, event date, and deadline.
- Reads notice bodies and relevant image/PDF/table attachments.
- Extracts supplies, forms, deadlines, pickup changes, events, health/safety requests, and fee notices.
- Reports only source-grounded actions, never generic invented advice.

### What it never does

- Requests or stores passwords, OTPs, cookies, or tokens.
- Bypasses a login, CAPTCHA, MFA, rate limit, or portal access control.
- Submits forms, sends replies, makes payments, or shares child information without a separate explicit request.
- Treats notification previews or prior summaries as proof of current notices.

### Install

Copy `optional-skills/productivity/parent-portal-notice-brief/` to:

```text
~/.hermes/skills/productivity/parent-portal-notice-brief/
```

Start a new Hermes session after installation so the skill index refreshes.
