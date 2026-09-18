# Kidsnote Relay

A privacy-first optional [Hermes Agent](https://github.com/NousResearch/hermes-agent) skill for checking an already logged-in PC parent portal—including Kidsnote—and producing a short brief of actions a parent needs to take.

## What it does

- Checks that the intended portal context is visibly logged in.
- Reviews notices posted today and the previous calendar day by default.
- Separates **post time**, **event date**, and **deadline**.
- Reads notice bodies plus relevant image/PDF/table attachments.
- Extracts supplies, forms, deadlines, pickup changes, events, health/safety requests, and fee notices.
- Reports only source-grounded actions, not invented generic advice.

## What it never does

- Requests or stores passwords, OTPs, cookies, or tokens.
- Bypasses a login, CAPTCHA, MFA, rate limit, or portal access control.
- Submits forms, sends replies, makes payments, or shares a child’s information without a separate explicit request.
- Treats notification previews or old summaries as proof of current notices.

## Install locally

Copy the skill directory into your Hermes profile:

```text
~/.hermes/skills/productivity/parent-portal-notice-brief/
```

Start a new Hermes session after installing so its skill index is refreshed.

## Example request

> Check today’s school portal notices and tell me only what I need to do.

## Example output

```markdown
## Parent Portal Notice Brief

Basis:
- Checked: 2026-09-18 16:05 KST
- Included post dates: 2026-09-18, 2026-09-17

Actions:
- [2026-09-20] Submit the field-trip consent form — Source: Autumn Field Trip (posted 2026-09-18 14:12)

Supplies and clothing:
- [2026-09-24] Water bottle, hat, and white sneakers

Schedule and transport:
- [2026-09-24 09:00] Field-trip departure

Health, safety, and fees:
- No verified items
```

All dates, names, and notice content in this example are synthetic.

## Repository layout

```text
optional-skills/productivity/parent-portal-notice-brief/SKILL.md
references/freshness-and-date-rules.md
templates/parent-brief-template.md
tests/fixtures/synthetic-school-notice.md
tests/test_skill_structure.py
```

## License

MIT. See [LICENSE](LICENSE).
