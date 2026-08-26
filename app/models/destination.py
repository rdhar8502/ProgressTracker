from sqlalchemy import Column, Integer, String, Float, Text, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base


class RelocationDestination(Base):
    __tablename__ = "relocation_destinations"

    id = Column(Integer, primary_key=True, index=True)
    rank = Column(Integer, nullable=False, default=1)
    country_name = Column(String(100), nullable=False)
    flag_emoji = Column(String(10), nullable=False)
    summary_verdict = Column(String(255), nullable=False)  # User's summary rank note
    
    # Currency and Exchange Rates
    currency_code = Column(String(10), nullable=False, default="EUR")
    currency_symbol = Column(String(10), nullable=False, default="€")
    exchange_rate_inr = Column(Float, nullable=False, default=111.20)  # 1 Local Unit = X INR

    # Compensation Economics in Local Currency
    salary_min = Column(Float, nullable=False, default=85000.0)
    salary_max = Column(Float, nullable=False, default=120000.0)
    salary_median = Column(Float, nullable=False, default=95000.0)
    estimated_tax_rate = Column(Float, nullable=False, default=41.0)  # percentage, e.g., 41.0 for 41%
    monthly_expense_local = Column(Float, nullable=False, default=2100.0)  # rent + living expenses

    # Relocation, Visa & PR Practicalities
    sponsor_visa_pathway = Column(String(255), nullable=False)  # Best way to move / Sponsor Visa
    pr_criteria_timeline = Column(Text, nullable=False)        # Permanent Residency criteria and timeline
    language_requirements = Column(String(255), nullable=False) # Language requirements (English/Local)
    family_mother_feasibility = Column(Text, nullable=False)   # Mother & family visa feasibility
    family_mother_badge = Column(String(50), default="High")   # Legacy / family feasibility category
    
    # Lifestyle, Environment, Safety & Quality of Life Rankings
    quality_of_life_rank = Column(String(50), default="")      # e.g. "#1 Worldwide", "#9 Worldwide"
    happiness_rank = Column(String(50), default="")            # e.g. "#7 Worldwide (2026)", "#11 Worldwide"
    safety_score = Column(String(100), default="")             # e.g. "Top 3 Globally · Near-Zero Violent Crime"
    retirement_suitability = Column(Text, default="")          # Healthcare, peaceful suburbs, pension portability
    scenic_pollution_rating = Column(Text, default="")         # Pristine air, nature, parks, low pollution
    peaceful_scenic_motivation = Column(Text, default="")      # Motivation for living: peaceful scenic areas, lakes, mountains
    best_cities_states = Column(Text, default="")              # Best state/province/canton & city recommendations
    keep_in_mind_notes = Column(Text, default="")              # Key practical gotchas (letters, housing search, etc.)

    # In-depth breakdown details
    tax_breakdown_notes = Column(Text, default="")
    tech_market_notes = Column(Text, default="")
    general_notes = Column(Text, default="")
    
    order_index = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    @property
    def monthly_gross_local(self) -> float:
        return self.salary_median / 12.0

    @property
    def annual_tax_local(self) -> float:
        return self.salary_median * (self.estimated_tax_rate / 100.0)

    @property
    def monthly_take_home_local(self) -> float:
        return (self.salary_median - self.annual_tax_local) / 12.0

    @property
    def monthly_savings_local(self) -> float:
        return max(0.0, self.monthly_take_home_local - self.monthly_expense_local)

    @property
    def annual_savings_local(self) -> float:
        return self.monthly_savings_local * 12.0

    # ── INR Conversions ──────────────────────────────────────────
    @property
    def annual_gross_inr(self) -> float:
        return self.salary_median * self.exchange_rate_inr

    @property
    def monthly_gross_inr(self) -> float:
        return self.monthly_gross_local * self.exchange_rate_inr

    @property
    def monthly_take_home_inr(self) -> float:
        return self.monthly_take_home_local * self.exchange_rate_inr

    @property
    def monthly_expense_inr(self) -> float:
        return self.monthly_expense_local * self.exchange_rate_inr

    @property
    def monthly_savings_inr(self) -> float:
        return self.monthly_savings_local * self.exchange_rate_inr

    @property
    def annual_savings_inr(self) -> float:
        return self.annual_savings_local * self.exchange_rate_inr

    # Helper formatting for Indian numbering system (Lakhs & Crores)
    def format_inr(self, amount: float) -> str:
        if amount >= 10000000:
            return f"₹{amount / 10000000:.2f} Cr"
        elif amount >= 100000:
            return f"₹{amount / 100000:.2f} L"
        else:
            return f"₹{amount:,.0f}"
