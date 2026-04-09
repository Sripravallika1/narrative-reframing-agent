"""Basic tests for narrative reframing logic."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from narrative_reframing_agent.core import reframe_narrative


def test_reframe_narrative_returns_structured_fields() -> None:
    text = "I always mess up big pitches, but I learned to persist and ship anyway."
    result = reframe_narrative(text)
    assert "founder" in result.reframed_identity.lower()
    assert len(result.strength_based_narrative) > 10
    assert len(result.decision_framing) > 10
    assert len(result.detected_limitations) >= 1
