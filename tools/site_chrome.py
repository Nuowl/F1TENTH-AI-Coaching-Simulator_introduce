"""Optional lab banner. Disable SHOW_LAB_HEADER before merging into a host site."""
SHOW_LAB_HEADER = True


def header():
    if not SHOW_LAB_HEADER:
        return ''
    return '''<header class="masthead"><div class="wrap masthead-inner">
<a class="brand" href="https://aix.gnu.ac.kr/" aria-label="AiX Lab home"><span class="logo"><img src="assets/media/aix_lab_logo.png" width="112" height="49" alt="AiX Lab"><img class="logo-lettering" src="assets/media/aix_lab_logo.png" width="112" height="49" alt="" aria-hidden="true"></span><span class="brand-label">GYEONGSANG NATIONAL UNIVERSITY<br>RESEARCH PROJECTS</span></a>
<nav class="lab-links" aria-label="AiX Lab"><a href="https://aix.gnu.ac.kr/about.html">About Us</a><a href="https://aix.gnu.ac.kr/research/">Research ↗</a><a href="https://aix.gnu.ac.kr/projects/">Projects ↗</a></nav>
</div></header>'''
