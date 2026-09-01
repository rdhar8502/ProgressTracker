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
    quality_of_life_rank = Column(String(255), default="")     # e.g. "#1 Worldwide", "#8 Worldwide"
    happiness_rank = Column(String(255), default="")           # e.g. "#22 Worldwide (TheGlobalEconomy 2026 - Score: 6.75)"
    safety_score = Column(String(255), default="")            # e.g. "Top 3 Globally · Near-Zero Violent Crime"
    retirement_suitability = Column(Text, default="")          # Healthcare, peaceful suburbs, pension portability
    scenic_pollution_rating = Column(Text, default="")         # Pristine air, nature, parks, low pollution
    peaceful_scenic_motivation = Column(Text, default="")      # Motivation for living: peaceful scenic areas, lakes, mountains
    best_cities_states = Column(Text, default="")              # Best state/province/canton & city recommendations
    keep_in_mind_notes = Column(Text, default="")              # Key practical gotchas (letters, housing search, etc.)

    # 🎯 8+ YOE Senior/Staff Interview Style, Process & Employer Behavior
    interview_style_summary = Column(Text, default="")         # Core interview philosophy & technical style
    interview_process_stages = Column(Text, default="")        # Full hiring pipeline & stage breakdown
    employer_behavior_culture = Column(Text, default="")       # Employer communication, directness, debate, 'I don't know' handling
    senior_8yoe_focus = Column(Text, default="")               # Senior/Staff 8+ YOE specific expectations (tradeoffs, autonomy, architecture)

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

    # ── Purchasing Power & Asset Affordability Metrics ───────────
    @property
    def is_tier1_priority(self) -> bool:
        """Germany, Netherlands, USA, and Canada are Tier-1 Core Priority countries."""
        return self.country_name in ["Germany", "Netherlands", "USA", "Canada"]

    @property
    def priority_label(self) -> str:
        if self.country_name in ["Germany", "Netherlands", "USA", "Canada"]:
            return "Tier-1 Priority Target"
        elif self.country_name == "Singapore":
            return "Tier-1 APAC (Mother LTVP)"
        else:
            return "Target Country"

    @property
    def standard_car_cost_local(self) -> float:
        """
        Baseline cost of a standard new car (e.g. Toyota Corolla / Camry / Sedan).
        Local standard market price with typical sales tax.
        """
        prices = {
            "USA": 26000.0,         # USD ~$26k
            "Canada": 32000.0,      # CAD ~$32k
            "Germany": 26000.0,     # EUR ~€26k
            "Netherlands": 27000.0, # EUR ~€27k
            "Switzerland": 28000.0, # CHF ~CHF 28k
            "Ireland": 28000.0,     # EUR ~€28k
            "Sweden": 320000.0,     # SEK ~320k kr
            "Norway": 340000.0,     # NOK ~340k kr
            "Australia": 36000.0,   # AUD ~$36k
            "New Zealand": 38000.0, # NZD ~$38k
            "Poland": 115000.0,     # PLN ~115k zł
            "Singapore": 125000.0,  # SGD ~$125k (inclusive of COE certificate)
        }
        return prices.get(self.country_name, 26000.0)

    @property
    def car_months_take_home_salary(self) -> float:
        """How many months of net in-hand salary needed to buy a new car outright."""
        if self.monthly_take_home_local <= 0:
            return 0.0
        return round(self.standard_car_cost_local / self.monthly_take_home_local, 1)

    @property
    def car_months_savings(self) -> float:
        """How many months of net savings (after living expenses) needed to buy a new car outright."""
        if self.monthly_savings_local <= 0:
            return 0.0
        return round(self.standard_car_cost_local / self.monthly_savings_local, 1)

    @property
    def iphone_work_days(self) -> float:
        """How many working days (assuming 21.6 work days/month) of net salary to buy a flagship iPhone ($1,200)."""
        daily_take_home = self.monthly_take_home_local / 21.66 if self.monthly_take_home_local > 0 else 1.0
        iphone_local_costs = {
            "USA": 1199.0,
            "Canada": 1599.0,
            "Germany": 1299.0,
            "Netherlands": 1299.0,
            "Switzerland": 1199.0,
            "Ireland": 1349.0,
            "Sweden": 15490.0,
            "Norway": 15990.0,
            "Australia": 1849.0,
            "New Zealand": 2049.0,
            "Poland": 5799.0,
            "Singapore": 1649.0,
        }
        cost = iphone_local_costs.get(self.country_name, 1200.0)
        return round(cost / daily_take_home, 1) if daily_take_home > 0 else 5.0

    # Helper formatting for Indian numbering system (Lakhs & Crores)
    def format_inr(self, amount: float) -> str:
        if amount >= 10000000:
            return f"₹{amount / 10000000:.2f} Cr"
        elif amount >= 100000:
            return f"₹{amount / 100000:.2f} L"
        else:
            return f"₹{amount:,.0f}"

