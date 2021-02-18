# unsorted site data for templates.
from collections import namedtuple
Skill = namedtuple("Skill", "filename title")

SKILL_INFO = {
    "definitely": [
        Skill("python", "Python"),
        Skill("terminal", "unix Shell"),
        Skill("debian", "Debian"),
        Skill("git", "Git"),
        Skill("javascript", "JavaScript"),
        Skill("typescript", "TypeScript"),
        Skill("css3", "CSS 3"),
        Skill("html5", "HTML 5"),
        Skill("sass", "Sass/SCSS"),
    ],

    "probably": [
        Skill("docker", "Docker"),
        Skill("java", "Java"),
        Skill("psql", "PostGreSQL"),
        Skill("LaTeX", "LaTeX"),
        Skill("go", "Golang"),
    ],

    "maybe": [
        Skill("rust", "Rust"),
        Skill("apple", "Objective-C"),
        Skill("perl", "Perl"),
        Skill("prolog", "Prolog"),
        Skill("ruby", "Ruby"),
        Skill("racket", "Racket"),
        Skill("c", "C"),
        Skill("c++", "C++"),
        Skill("scala", "Scala"),
        Skill("haskell", "Haskell"),
    ],
}
