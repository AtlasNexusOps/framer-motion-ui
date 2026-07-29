from pathlib import Path


HTML = (Path(__file__).resolve().parents[1] / "index.html").read_text()


def test_atlas_header_uses_brand_logo_instead_of_crescent():
    header = HTML.split("</nav>", 1)[0]
    assert '<img src="/atlas-logo.png?v=20260527"' in header
    assert '<svg width="28" height="28"' not in header


def test_motion_scene_has_halo_and_orchestrated_motion_hooks():
    required = [
        'class="motion-scene',
        'class="fm-core',
        "@keyframes dotHalo",
        "@keyframes fmCoreMotion",
        ".motion-dot::after",
        ".timeline-step::after",
        ".timeline-step:nth-child(2)",
    ]
    for marker in required:
        assert marker in HTML


def test_reduced_motion_disables_new_ambient_animations():
    reduced = HTML.split("@media (prefers-reduced-motion: reduce)", 1)[1]
    assert ".motion-dot" in reduced
    assert ".fm-core" in reduced
    assert ".orbit" in reduced
    assert "animation: none" in reduced
