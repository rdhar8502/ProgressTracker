from app.models.user import UserProfile, SalaryTarget, WeeklySchedule
from app.models.daily_log import DailyLog
from app.models.dsa import DSAProblem, DSATopic
from app.models.system_design import SystemDesignTopic, SystemDesignCase
from app.models.ai_llm import AILLMTopic
from app.models.github import GithubProject, GithubTask
from app.models.application import Application

__all__ = [
    "UserProfile", "SalaryTarget", "WeeklySchedule",
    "DailyLog",
    "DSAProblem", "DSATopic",
    "SystemDesignTopic", "SystemDesignCase",
    "AILLMTopic",
    "GithubProject", "GithubTask",
    "Application",
]
