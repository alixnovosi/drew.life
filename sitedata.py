# unsorted site data for templates.
from collections import namedtuple
Skill = namedtuple("Skill", "filename title")

SKILL_INFO = {
    "definitely": [
        Skill("python", "Python"),
        Skill("java", "Java"),
        Skill("terminal", "unix Shell"),
        Skill("javascript", "JavaScript"),
        Skill("typescript", "TypeScript"),
        Skill("css3", "CSS 3"),
        Skill("html5", "HTML 5"),
        Skill("sass", "Sass/SCSS"),
    ],

    "probably": [
        Skill("psql", "PostGreSQL"),
        Skill("LaTeX", "LaTeX"),
        Skill("go", "Golang"),
        Skill("rust", "Rust"),
    ],

    "maybe": [
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
