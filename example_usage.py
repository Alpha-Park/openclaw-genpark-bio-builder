# -*- coding: utf-8 -*-
from client import OpenClawGenParkBioBuilder

bio = OpenClawGenParkBioBuilder()

exps = [
    {"title": "Senior Software Engineer", "duration_months": 24},
    {"title": "Lead Infrastructure Architect", "duration_months": 36},
    {"title": "VP of Engineering", "duration_months": 30}
]
skills = ["ai:llm", "ai:agents", "infra:kubernetes", "infra:distributed", "mgmt:executive"]

# 1. Executive Persona Vector
persona = bio.synthesize_executive_persona_vector(exps, skills, domain_authority_score=90.0)
print(f"Persona Synthesis: Tier={persona['executive_persona_tier']} (Influence: {persona['composite_influence_score']})")
print(f"  Seniority Depth: {persona['seniority_depth_index']}, Specialization HHI: {persona['domain_specialization_hhi']}")

# 2. Career Trajectory Velocity
milestones = [
    {"role": "L3 Engineer", "seniority_level": 3.0, "tenure_years": 1.5},
    {"role": "L5 Senior", "seniority_level": 5.0, "tenure_years": 2.0},
    {"role": "L7 Director", "seniority_level": 7.0, "tenure_years": 2.5}
]
traj = bio.calculate_career_trajectory_velocity(milestones)
print()
print(f"Trajectory Velocity: Velocity={traj['career_velocity_index']} ({traj['trajectory_status']}, Accel={traj['acceleration_gradient']})")

# 3. Cryptographic Credential Leaf
leaf = bio.generate_credential_merkle_leaf_hash("usr_7701", "AI_ARCHITECT_CERTIFIED", "OPENCLAW_FOUNDATION", 1730000000)
print()
print(f"Verifiable Credential Leaf: {leaf['merkle_leaf_hash']} ({leaf['credential_type']})")
