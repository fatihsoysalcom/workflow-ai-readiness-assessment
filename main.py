class Workflow:
    def __init__(self, name, description, is_repetitive, is_rule_based,
                 is_data_intensive, requires_learning_adaptation,
                 involves_unstructured_data, current_manual_effort_hours_per_week):
        self.name = name
        self.description = description
        self.is_repetitive = is_repetitive
        self.is_rule_based = is_rule_based
        self.is_data_intensive = is_data_intensive
        self.requires_learning_adaptation = requires_learning_adaptation
        self.involves_unstructured_data = involves_unstructured_data
        self.current_manual_effort_hours_per_week = current_manual_effort_hours_per_week

def assess_ai_readiness(workflow):
    """
    Assesses a workflow's readiness for AI automation based on predefined criteria.
    The scoring reflects the article's emphasis on repetitive, data-intensive,
    complex, and adaptive tasks.
    """
    score = 0
    recommendation = ""
    reasons = []

    # Criteria from the article: "tekrarlayan, kural tabanlı veya veri yoğun görevleri otomatikleştirme"
    # (repetitive, rule-based, or data-intensive tasks automation)
    # and "öğrenme ve adaptasyon yetenekleri sayesinde daha karmaşık ve dinamik süreçleri yönetebilir."
    # (can manage more complex and dynamic processes through learning and adaptation capabilities.)

    if workflow.is_repetitive:
        score += 2
        reasons.append("Highly repetitive task (Tekrarlayan).")
    if workflow.is_rule_based:
        score += 1
        reasons.append("Rule-based, suitable for initial automation; AI can enhance (Kural Tabanlı).")
    if workflow.is_data_intensive:
        score += 3
        reasons.append("Data-intensive, benefits from AI processing large datasets (Veri Yoğun).")
    if workflow.requires_learning_adaptation:
        score += 5
        reasons.append("Requires learning and adaptation, core strength of AI (Öğrenme ve Adaptasyon).")
    if workflow.involves_unstructured_data:
        score += 4
        reasons.append("Involves unstructured data (e.g., text, images), ideal for NLP/CV (Yapılandırılmamış Veri).")

    # Manual effort indicates potential ROI for automation
    effort_score = min(workflow.current_manual_effort_hours_per_week // 10, 5)
    score += effort_score
    if effort_score > 0:
        reasons.append(f"Significant manual effort ({workflow.current_manual_effort_hours_per_week} hrs/week).")

    # Determine recommendation based on score
    if score >= 10:
        recommendation = "High AI Automation Potential"
    elif score >= 5:
        recommendation = "Moderate AI Automation Potential"
    else:
        recommendation = "Low AI Automation Potential (Consider traditional automation first)"

    return score, recommendation, reasons

# --- Sample Workflows ---
# These examples are designed to illustrate different levels of AI readiness
# based on the criteria discussed in the article.
workflows = [
    Workflow(
        name="Customer Support Ticket Routing",
        description="Categorizing incoming customer support emails and assigning to appropriate departments.",
        is_repetitive=True,
        is_rule_based=True, # Can be rule-based, but AI improves with sentiment/context
        is_data_intensive=True, # Many tickets, text data
        requires_learning_adaptation=True, # New issues, evolving language
        involves_unstructured_data=True, # Email text (NLP)
        current_manual_effort_hours_per_week=40
    ),
    Workflow(
        name="Invoice Processing",
        description="Extracting data from vendor invoices and entering it into an accounting system.",
        is_repetitive=True,
        is_rule_based=False, # Can be rule-based but often involves variations and exceptions
        is_data_intensive=True, # Many invoices, varied formats
        requires_learning_adaptation=True, # Adapting to new invoice formats (Computer Vision/ML)
        involves_unstructured_data=True, # Scanned documents (Computer Vision, OCR)
        current_manual_effort_hours_per_week=30
    ),
    Workflow(
        name="Employee Onboarding Checklist Management",
        description="Tracking completion of tasks for new employees (e.g., IT setup, HR forms).",
        is_repetitive=True,
        is_rule_based=True,
        is_data_intensive=False, # Limited data per employee
        requires_learning_adaptation=False, # Mostly fixed process
        involves_unstructured_data=False,
        current_manual_effort_hours_per_week=10
    ),
    Workflow(
        name="Social Media Sentiment Analysis",
        description="Monitoring social media for brand mentions and analyzing sentiment (positive, negative, neutral).",
        is_repetitive=True,
        is_rule_based=False, # Sentiment is complex, not purely rule-based
        is_data_intensive=True, # Vast amounts of social media data
        requires_learning_adaptation=True, # Evolving language, slang, context (NLP, ML)
        involves_unstructured_data=True, # Text data (NLP)
        current_manual_effort_hours_per_week=25
    ),
    Workflow(
        name="Simple Data Entry (Structured Forms)",
        description="Entering data from pre-defined, structured digital forms into a database.",
        is_repetitive=True,
        is_rule_based=True,
        is_data_intensive=True,
        requires_learning_adaptation=False, # No learning needed for structured forms
        involves_unstructured_data=False,
        current_manual_effort_hours_per_week=20
    )
]

# --- Run Assessment ---
print("--- AI Automation Readiness Assessment ---")
print("This script simulates identifying AI-ready workflows based on criteria like repetitiveness, data intensity, and need for learning/adaptation, as discussed in the article.")
print("-" * 50)

for workflow in workflows:
    score, recommendation, reasons = assess_ai_readiness(workflow)
    print(f"\nWorkflow: {workflow.name}")
    print(f"  Description: {workflow.description}")
    print(f"  AI Readiness Score: {score}")
    print(f"  Recommendation: {recommendation}")
    print("  Key Factors:")
    for reason in reasons:
        print(f"    - {reason}")
    print("-" * 50)
