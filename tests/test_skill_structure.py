from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "optional-skills/productivity/parent-portal-notice-brief/SKILL.md"
README = ROOT / "README.md"
TEMPLATE = ROOT / "optional-skills/productivity/parent-portal-notice-brief/templates/parent-brief-template.md"
REFERENCE = ROOT / "optional-skills/productivity/parent-portal-notice-brief/references/freshness-and-date-rules.md"
FIXTURE = ROOT / "tests/fixtures/synthetic-school-notice.md"


class SkillStructureTests(unittest.TestCase):
    def test_required_artifacts_exist(self):
        for path in (SKILL, README, TEMPLATE, REFERENCE, FIXTURE):
            self.assertTrue(path.is_file(), path)

    def test_frontmatter_is_valid_shape(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        frontmatter, body = text[4:].split("\n---\n", 1)
        fields = dict(
            line.split(":", 1)
            for line in frontmatter.splitlines()
            if ":" in line and not line.startswith(" ")
        )
        for field in ("name", "description", "version", "author", "license", "platforms"):
            self.assertIn(field, fields)
        description = fields["description"].strip()
        self.assertLessEqual(len(description), 60)
        self.assertTrue(description.endswith("."))
        self.assertGreater(len(body.strip()), 0)

    def test_skill_has_safety_and_freshness_rules(self):
        text = SKILL.read_text(encoding="utf-8")
        for phrase in ("posted/upload", "OTP", "CAPTCHA", "What to do", "Could not verify"):
            self.assertIn(phrase, text)

    def test_no_machine_local_paths_or_credentials(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertNotRegex(text, re.compile(r"/(Users|home)/"))
        self.assertNotIn("cookie value", text.lower())


if __name__ == "__main__":
    unittest.main()
