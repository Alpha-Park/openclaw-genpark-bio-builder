# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Bio Builder Client
Pure Python Standard Library (Zero External Dependencies)
Implements executive persona vector synthesis, career trajectory velocity scoring,
and cryptographic credential Merkle tree leaf hash generation.
"""

import math
import hashlib
from typing import Dict, Any, List, Optional

class OpenClawGenParkBioBuilder:
    """
    Algorithmic executive profiling and verifiable credential synthesis engine.
    """

    def __init__(self):
        self.seniority_weights = {
            "c_level": 5.0,
            "vp": 4.0,
            "director": 3.0,
            "lead": 2.0,
            "senior": 1.5,
            "staff": 2.5,
            "principal": 3.5
        }

    def synthesize_executive_persona_vector(
        self,
        experiences: List[Dict[str, Any]],
        skills: List[str],
        domain_authority_score: float = 85.0
    ) -> Dict[str, Any]:
        """
        Synthesizes executive persona profile metrics:
          - Seniority Depth Index
          - Domain Specialization Concentration (Herfindahl-Hirschman Index HHI on skill tags)
          - Executive Voice Tier
        """
        if not experiences:
            return {"persona_tier": "EMERGING", "seniority_depth_index": 0.0, "specialization_hhi": 0.0}

        total_weighted_months = 0.0
        total_months = 0.0

        for exp in experiences:
            months = float(exp.get("duration_months", 12))
            role_title = exp.get("title", "").lower()
            
            weight = 1.0
            for k, w in self.seniority_weights.items():
                if k in role_title:
                    weight = max(weight, w)
            
            total_weighted_months += months * weight
            total_months += months

        seniority_index = round((total_weighted_months / max(1.0, total_months)), 2)

        # Skill concentration HHI
        if skills:
            skill_freq = {}
            for s in skills:
                cat = s.split(":")[0].strip().lower() if ":" in s else "general"
                skill_freq[cat] = skill_freq.get(cat, 0) + 1
            tot = sum(skill_freq.values())
            shares = [count / tot for count in skill_freq.values()]
            hhi = round(sum(s**2 for s in shares), 4)
        else:
            hhi = 0.0

        # Voice Tier
        composite = (seniority_index * 15.0) + (domain_authority_score * 0.4) + (hhi * 20.0)
        if composite >= 75:
            tier = "VISIONARY_EXECUTIVE_L7"
        elif composite >= 55:
            tier = "SENIOR_LEADERSHIP_L6"
        else:
            tier = "PRACTITIONER_LEAD_L5"

        return {
            "executive_persona_tier": tier,
            "seniority_depth_index": seniority_index,
            "domain_specialization_hhi": hhi,
            "total_experience_months": int(total_months),
            "composite_influence_score": round(composite, 1)
        }

    def calculate_career_trajectory_velocity(
        self,
        career_milestones: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Calculates career promotion cadence velocity and career acceleration gradient:
          Velocity = sum( seniority_jump / max(0.5, years_in_role) ) / total_transitions
        """
        if len(career_milestones) < 2:
            return {
                "trajectory_status": "STABLE_BASE",
                "career_velocity_index": 1.0,
                "acceleration_gradient": 0.0
            }

        velocities = []
        for i in range(1, len(career_milestones)):
            prev = career_milestones[i - 1]
            curr = career_milestones[i]

            prev_level = float(prev.get("seniority_level", 1.0))
            curr_level = float(curr.get("seniority_level", 1.0))
            years = max(0.5, float(curr.get("tenure_years", 2.0)))

            jump = max(0.0, curr_level - prev_level)
            v = jump / years
            velocities.append(v)

        avg_velocity = round(sum(velocities) / len(velocities), 3)

        # Acceleration (derivative of velocity)
        gradient = round(velocities[-1] - velocities[0], 3) if len(velocities) >= 2 else 0.0

        if avg_velocity >= 1.0:
            status = "HYPER_GROWTH_FAST_TRACK"
        elif avg_velocity >= 0.5:
            status = "HEALTHY_ASCENDING_TRAJECTORY"
        else:
            status = "STEADY_TENURED_PACING"

        return {
            "trajectory_status": status,
            "career_velocity_index": avg_velocity,
            "acceleration_gradient": gradient,
            "total_milestone_transitions": len(velocities)
        }

    def generate_credential_merkle_leaf_hash(
        self,
        candidate_id: str,
        credential_type: str,
        issuing_authority: str,
        issue_timestamp_utc: int
    ) -> Dict[str, Any]:
        """
        Generates cryptographic double-SHA256 leaf hash for verifiable credentials on-chain:
          Leaf = SHA256( SHA256( candidate_id || type || authority || timestamp ) )
        """
        payload = f"{candidate_id}:{credential_type}:{issuing_authority}:{issue_timestamp_utc}".encode("utf-8")
        h1 = hashlib.sha256(payload).digest()
        h2 = hashlib.sha256(h1).hexdigest()

        return {
            "candidate_id": candidate_id,
            "credential_type": credential_type,
            "issuing_authority": issuing_authority,
            "issue_timestamp_utc": issue_timestamp_utc,
            "merkle_leaf_hash": f"0x{h2}"
        }
