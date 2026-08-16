import re
from urllib.parse import urlparse
from sqlalchemy import Column, Integer, String, Date, DateTime, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


# Association Table for DSAProblem <-> DSATopic many-to-many relationship
dsa_problem_topics = Table(
    "dsa_problem_topics",
    Base.metadata,
    Column("problem_id", Integer, ForeignKey("dsa_problems.id", ondelete="CASCADE"), primary_key=True),
    Column("topic_id", Integer, ForeignKey("dsa_topics.id", ondelete="CASCADE"), primary_key=True),
)


def clean_title_from_url(url: str) -> str:
    if not url or not (url.startswith("http://") or url.startswith("https://")):
        return url
    try:
        parsed = urlparse(url)
        path = parsed.path.strip("/")
        parts = [p for p in path.split("/") if p]
        slug = ""
        if "problems" in parts:
            idx = parts.index("problems")
            if idx + 1 < len(parts):
                slug = parts[idx + 1]
        elif "challenges" in parts:
            idx = parts.index("challenges")
            if idx + 1 < len(parts):
                slug = parts[idx + 1]
        elif "problemset" in parts:
            idx = parts.index("problemset")
            if idx + 2 < len(parts):
                slug = f"Problem {parts[idx + 2]} {parts[idx + 3]}" if idx + 3 < len(parts) else parts[idx + 2]
        else:
            for part in reversed(parts):
                if not part.isdigit():
                    slug = part
                    break
            if not slug and parts:
                slug = parts[-1]
        if not slug:
            return url
        slug = re.sub(r"-\d{6,}$", "", slug)
        slug = re.sub(r"-\d+$", "", slug)
        words = slug.replace("-", " ").replace("_", " ").split()
        title = " ".join(word.capitalize() for word in words)
        return title or url
    except Exception:
        return url


class DSATopic(Base):
    __tablename__ = "dsa_topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    order_index = Column(Integer, default=0)
    description = Column(Text, default="")
    problems = relationship("DSAProblem", secondary=dsa_problem_topics, back_populates="topics")


class DSAProblem(Base):
    __tablename__ = "dsa_problems"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(100), nullable=False, default="Arrays and Strings")
    title = Column(String(300), nullable=False)
    difficulty = Column(String(10), nullable=False, default="Medium")  # Easy / Medium / Hard
    topics = relationship("DSATopic", secondary=dsa_problem_topics, back_populates="problems")
    status = Column(String(20), default="Not Started")  # Not Started / In Progress / Solved / Needs Review
    pattern = Column(Text, default="")
    mistake = Column(Text, default="")
    time_complexity = Column(String(50), default="")
    space_complexity = Column(String(50), default="")
    solution_snippet = Column(Text, default="")
    confidence = Column(Integer, default=3)  # 1-5
    problem_url = Column(String(300), default="")
    alternate_title = Column(String(300), default="")
    alternate_url = Column(String(300), default="")
    solved_date = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    @property
    def clean_title(self) -> str:
        if self.title.startswith("http://") or self.title.startswith("https://"):
            return clean_title_from_url(self.title)
        return self.title

    @property
    def clean_alternate_title(self) -> str:
        if not self.alternate_title:
            return ""
        if self.alternate_title.startswith("http://") or self.alternate_title.startswith("https://"):
            return clean_title_from_url(self.alternate_title)
        return self.alternate_title

    @property
    def category_js_escaped(self) -> str:
        cat = self.category or "Arrays and Strings"
        return cat.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")

    @property
    def clean_title_js_escaped(self) -> str:
        title = self.clean_title
        return title.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")

    @property
    def clean_alternate_title_js_escaped(self) -> str:
        title = self.clean_alternate_title
        return title.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")

    @property
    def solution_snippet_js_escaped(self) -> str:
        if not self.solution_snippet:
            return ""
        return self.solution_snippet.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")

    @property
    def source_site(self) -> str:
        if not self.problem_url:
            return "Other"
        
        url_lower = self.problem_url.lower()
        if "leetcode.com" in url_lower:
            return "LeetCode"
        elif "geeksforgeeks.org" in url_lower:
            return "GeeksforGeeks"
        elif "hackerrank.com" in url_lower:
            return "HackerRank"
        elif "codeforces.com" in url_lower:
            return "Codeforces"
        elif "codechef.com" in url_lower:
            return "CodeChef"
        elif "lintcode.com" in url_lower:
            return "LintCode"
        elif "interviewbit.com" in url_lower:
            return "InterviewBit"
        else:
            try:
                parsed = urlparse(self.problem_url)
                netloc = parsed.netloc.lower()
                if netloc.startswith("www."):
                    netloc = netloc[4:]
                domain = netloc.split(".")[0]
                return domain.capitalize() if domain else "Other"
            except Exception:
                return "Other"

    @property
    def source_site_badge_class(self) -> str:
        site = self.source_site.lower()
        if site == "leetcode":
            return "badge-leetcode"
        elif site == "geeksforgeeks":
            return "badge-gfg"
        elif site == "hackerrank":
            return "badge-hackerrank"
        elif site == "codeforces":
            return "badge-codeforces"
        elif site == "codechef":
            return "badge-codechef"
        else:
            return "badge-other-site"

    @property
    def alternate_source_site(self) -> str:
        if not self.alternate_url:
            return "Other"
        
        url_lower = self.alternate_url.lower()
        if "leetcode.com" in url_lower:
            return "LeetCode"
        elif "geeksforgeeks.org" in url_lower:
            return "GeeksforGeeks"
        elif "hackerrank.com" in url_lower:
            return "HackerRank"
        elif "codeforces.com" in url_lower:
            return "Codeforces"
        elif "codechef.com" in url_lower:
            return "CodeChef"
        elif "lintcode.com" in url_lower:
            return "LintCode"
        elif "interviewbit.com" in url_lower:
            return "InterviewBit"
        else:
            try:
                parsed = urlparse(self.alternate_url)
                netloc = parsed.netloc.lower()
                if netloc.startswith("www."):
                    netloc = netloc[4:]
                domain = netloc.split(".")[0]
                return domain.capitalize() if domain else "Other"
            except Exception:
                return "Other"

    @property
    def alternate_source_site_badge_class(self) -> str:
        site = self.alternate_source_site.lower()
        if site == "leetcode":
            return "badge-leetcode"
        elif site == "geeksforgeeks":
            return "badge-gfg"
        elif site == "hackerrank":
            return "badge-hackerrank"
        elif site == "codeforces":
            return "badge-codeforces"
        elif site == "codechef":
            return "badge-codechef"
        else:
            return "badge-other-site"

