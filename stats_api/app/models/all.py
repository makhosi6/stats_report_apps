from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class DLBenefit(db.Model):
    __tablename__ = "dl_benefit"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_entered = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    modified_user_id = db.Column(db.String(36))
    created_by = db.Column(db.String(36))
    description = db.Column(db.Text)
    deleted = db.Column(db.Boolean)
    assigned_user_id = db.Column(db.String(36))
    external_reference = db.Column(db.String(255))
    duplicate_benefit_id = db.Column(db.String(36))
    type = db.Column(db.String(255))
    product_code = db.Column(db.String(255))
    product_version = db.Column(db.String(255))
    addon_code = db.Column(db.String(255))
    addon_version = db.Column(db.String(255))
    benefit_amount = db.Column(db.Numeric(20, 2))
    benefit_accidental_amount = db.Column(db.Numeric(20, 2))
    currency_id = db.Column(db.String(36))
    premium_amount = db.Column(db.Numeric(20, 2))
    benefit_escalation = db.Column(db.Numeric(20, 2))
    premium_escalation = db.Column(db.Numeric(20, 2))
    expiry = db.Column(db.DateTime)
    policy_id = db.Column(db.String(36))
    claim_id = db.Column(db.String(36))
    agent_id = db.Column(db.String(36))
    provider_id = db.Column(db.String(36))
    sales_process_id = db.Column(db.String(36))
    invoiced_date = db.Column(db.DateTime)
    benefit_status = db.Column(db.String(255))
    pricing_id = db.Column(db.String(36))
    benefit_start_date = db.Column(db.DateTime)
    waiting_period = db.Column(db.Integer)
    deferment_period = db.Column(db.Integer)
    parent_product_benefit_id = db.Column(db.String(36))
    cancellation_effective_date = db.Column(db.DateTime)
    sale_date = db.Column(db.DateTime)
    benefit_start_date_original = db.Column(db.DateTime)
    converted_from_benefit_id = db.Column(db.String(36))
    benefit_prev_amount = db.Column(db.Numeric(20, 2))
    benefit_original_amount = db.Column(db.Numeric(20, 2))
    change_reason = db.Column(db.String(255))
    acase_id = db.Column(db.String(36))
    product_master_id = db.Column(db.String(36))
    retention_proportion = db.Column(db.Numeric(20, 2))
    immediate_start_date = db.Column(db.DateTime)
    term = db.Column(db.Integer)
    payout_term_months = db.Column(db.Integer)
    expiry_date = db.Column(db.DateTime)
    payout_defer_months = db.Column(db.Integer)
    benefit_dependant_id = db.Column(db.String(36))
    cover_max = db.Column(db.Numeric(20, 2))
    ask_order = db.Column(db.Integer)
    payment_type = db.Column(db.String(255))
    benefit_order = db.Column(db.Integer)
    link_code = db.Column(db.String(255))
    external_agent_id = db.Column(db.String(36))
    waiting_period_descriptions = db.Column(db.Text)
    is_summed_in_total_cover = db.Column(db.Boolean)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "date_entered": (
                self.date_entered.isoformat() if self.date_entered else None
            ),
            "date_modified": (
                self.date_modified.isoformat() if self.date_modified else None
            ),
        }


class DLPolicy(db.Model):
    __tablename__ = "dl_policy"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_entered = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    modified_user_id = db.Column(db.String(36))
    created_by = db.Column(db.String(36))
    description = db.Column(db.Text)
    deleted = db.Column(db.Boolean)
    assigned_user_id = db.Column(db.String(36))
    policy_status = db.Column(db.String(255))
    premium = db.Column(db.Numeric(20, 2))
    cover_start_date = db.Column(db.DateTime)
    sales_process_id = db.Column(db.String(36))
    policy_holder_id = db.Column(db.String(36))
    primary_contact_id = db.Column(db.String(36))
    life_insured_id = db.Column(db.String(36))
    premium_payer_id = db.Column(db.String(36))
    project_code = db.Column(db.String(255))
    collection_reference_number = db.Column(db.String(255))
    debit_order_due_date = db.Column(db.DateTime)
    sequence_number = db.Column(db.Integer)
    cancellation_effective_date = db.Column(db.DateTime)
    sale_date = db.Column(db.DateTime)
    cover_start_date_original = db.Column(db.DateTime)
    anniversary_process_date = db.Column(db.DateTime)
    prev_premium = db.Column(db.Numeric(20, 2))
    currency_id = db.Column(db.String(36))
    original_premium = db.Column(db.Numeric(20, 2))
    anniversary_effective_date = db.Column(db.DateTime)
    original_policy_id = db.Column(db.String(36))
    cancellation_reason = db.Column(db.String(255))
    initiation_premium = db.Column(db.Numeric(20, 2))
    initiation_premium_date = db.Column(db.DateTime)
    no_initiation_reason = db.Column(db.String(255))
    converted = db.Column(db.Boolean)
    reinstatement_reason = db.Column(db.String(255))
    ngo_id = db.Column(db.String(36))
    naedo = db.Column(db.Boolean)
    qa_decision = db.Column(db.String(255))
    trans_union_strike_day = db.Column(db.DateTime)
    immediate_start_date = db.Column(db.DateTime)
    do_not_reinstate = db.Column(db.Boolean)
    payment_type = db.Column(db.String(255))
    immediate_premium_date = db.Column(db.DateTime)
    reversal_counter = db.Column(db.Integer)
    migrated_on_date = db.Column(db.DateTime)
    synchronised_on_date = db.Column(db.DateTime)
    dl_scheme_id = db.Column(db.String(36))
    legacy_policy_id = db.Column(db.String(36))
    legacy_client_id = db.Column(db.String(36))
    dl_branch_id = db.Column(db.String(36))
    sub_branch_id = db.Column(db.String(36))
    dl_agent_id = db.Column(db.String(36))
    policy_cover_option = db.Column(db.String(255))
    policy_plan_code = db.Column(db.String(255))
    product_category = db.Column(db.String(255))
    external_agent_id = db.Column(db.String(36))
    lead_provider_id = db.Column(db.String(36))
    bypass_salary_check = db.Column(db.Boolean)
    conversion_case_number = db.Column(db.String(255))
    in_migration = db.Column(db.Boolean)
    mandate_status = db.Column(db.String(255))
    policy_renewal_date = db.Column(db.DateTime)
    activated_by_user_id = db.Column(db.String(36))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "date_entered": (
                self.date_entered.isoformat() if self.date_entered else None
            ),
            "date_modified": (
                self.date_modified.isoformat() if self.date_modified else None
            ),
        }


class DLBranch(db.Model):
    __tablename__ = "dl_branch"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_entered = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    modified_user_id = db.Column(db.String(36))
    created_by = db.Column(db.String(36))
    description = db.Column(db.Text)
    deleted = db.Column(db.Boolean)
    assigned_user_id = db.Column(db.String(36))
    province = db.Column(db.String(36))
    phone_number = db.Column(db.String(36))
    address_city = db.Column(db.String(36))
    address_postalcode = db.Column(db.String(36))
    address = db.Column(db.String(255))
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "date_entered": (
                self.date_entered.isoformat() if self.date_entered else None
            ),
            "date_modified": (
                self.date_modified.isoformat() if self.date_modified else None
            ),
        }

class DLClaim(db.Model):
    __tablename__ = "dl_claim"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_entered = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    modified_user_id = db.Column(db.String(36))
    created_by = db.Column(db.String(36))
    description = db.Column(db.Text)
    deleted = db.Column(db.Boolean)
    assigned_user_id = db.Column(db.String(36))
    claim_no = db.Column(db.String(255))
    admission = db.Column(db.Boolean)
    status = db.Column(db.String(255))
    sub_status = db.Column(db.String(255))
    acase_id = db.Column(db.String(36))
    dl_policy_id = db.Column(db.String(36))
    contact_id = db.Column(db.String(36))
    dl_benefit_id = db.Column(db.String(36))
    claim_event_date = db.Column(db.DateTime)
    claim_event = db.Column(db.String(255))
    resolution = db.Column(db.String(255))
    claim_amount_paid = db.Column(db.Numeric(20, 2))
    payment_date = db.Column(db.DateTime)
    date_concluded = db.Column(db.DateTime)
    date_claim_submitted_at_branch = db.Column(db.DateTime)
    date_of_forms_completion = db.Column(db.DateTime)
    work_province_of_deceased = db.Column(db.String(255))
    province_of_deceased = db.Column(db.String(255))
    cause_of_death = db.Column(db.String(255))
    claimant_banking_details_id = db.Column(db.String(36))
    second_claim_amount_paid = db.Column(db.Numeric(20, 2))
    second_payment_date = db.Column(db.DateTime)
    capture_user_name = db.Column(db.String(255))
    paid_out_by = db.Column(db.String(255))
    non_payment_reason = db.Column(db.String(255))
    relationship = db.Column(db.String(255))
    beneficiary_relationship = db.Column(db.String(255))
    ex_gratia = db.Column(db.Boolean)
    is_finished_with_text = db.Column(db.Boolean)
    deceased_id_number = db.Column(db.String(255))
    courier_tracking_number = db.Column(db.String(255))
    legacy_id = db.Column(db.String(36))
    original_claim_amount = db.Column(db.Numeric(20, 2))
    real_internal_cost = db.Column(db.Numeric(20, 2))
    real_external_cost = db.Column(db.Numeric(20, 2))
    estimated_external_cost = db.Column(db.Numeric(20, 2))
    estimated_internal_cost = db.Column(db.Numeric(20, 2))
    court = db.Column(db.String(255))
    payment_reference_number = db.Column(db.String(255))
    court_date = db.Column(db.DateTime)
    province = db.Column(db.String(255))
    represented_by = db.Column(db.String(255))
    dl_attorney_id = db.Column(db.String(36))
    salary_number = db.Column(db.String(255))
    funeral_parlour_id = db.Column(db.String(36))
    claim_member_requests_id = db.Column(db.String(36))
    province_of_claim_submitted = db.Column(db.String(255))
    legal_matter = db.Column(db.String(255))
    beneficiary_id = db.Column(db.String(36))
    original_claim_id = db.Column(db.String(36))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "amount": self.original_claim_amount,
            "sub_status": self.sub_status,
            "date_entered": (
                self.date_entered.isoformat() if self.date_entered else None
            ),
            "type": (self.claim_event if self.claim_event else None),
            "date_modified": (
                self.date_modified.isoformat() if self.date_modified else None
            ),
        }
