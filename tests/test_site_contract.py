from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_CHECKOUT = "https://www.paypal.com/ncp/payment/5WFCZBVANJLGA"
AUDIT_SCOPE_MAILTO = (
    "mailto:zach@zachwright.xyz?subject=Agent-Ready%20Repository%20Audit%20scope"
)
AUDIT_DELIVERY_COPY = (
    "Evidence-linked Markdown and JSON, up to five priorities, and a 30-minute "
    "handoff within three days after settlement and complete public inputs."
)


class SiteContractTests(unittest.TestCase):
    def test_human_audit_is_scope_gated_before_checkout(self) -> None:
        page = (ROOT / "index.html").read_text(encoding="utf-8")
        summary = (ROOT / "llms.txt").read_text(encoding="utf-8")

        self.assertNotIn("https://wrightops-ai.github.io/website/#offers", page)
        self.assertIn('"url": "https://zachwright.xyz/#offers"', page)
        self.assertNotIn(AUDIT_CHECKOUT, page)
        self.assertNotIn(AUDIT_CHECKOUT, summary)
        self.assertIn(AUDIT_SCOPE_MAILTO, page)
        self.assertIn("Request scope for the $750 audit", page)
        self.assertIn("written scope confirmation", page)
        self.assertIn("Requester%20authority%20to%20request%20this%20review%3A", page)
        self.assertIn(AUDIT_DELIVERY_COPY, page)
        self.assertIn("buyer-specific PayPal Goods & Services checkout", summary)
        self.assertIn("three days after settlement and complete public inputs", summary)

    def test_no_login_preflight_remains_the_primary_start(self) -> None:
        page = (ROOT / "index.html").read_text(encoding="utf-8")
        summary = (ROOT / "llms.txt").read_text(encoding="utf-8")

        self.assertGreaterEqual(page.count("https://zachwright.xyz/#preflight"), 4)
        self.assertIn("Free no-login preflight", page)
        self.assertIn("Free no-login preflight", summary)


if __name__ == "__main__":
    unittest.main()
