# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Bio Builder MCP Server
FastMCP standard interface for persona vector synthesis and career trajectory velocity scoring.
"""

import json
from typing import Dict, Any, List
from client import OpenClawGenParkBioBuilder

try:
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("openclaw-genpark-bio-builder")
except ImportError:
    class MockFastMCP:
        def __init__(self, name):
            self.name = name
        def tool(self):
            def decorator(f):
                return f
            return decorator
    mcp = MockFastMCP("openclaw-genpark-bio-builder")

bio_builder = OpenClawGenParkBioBuilder()

@mcp.tool()
def synthesize_executive_persona_vector(
    experiences: List[Dict[str, Any]],
    skills: List[str],
    domain_authority_score: float = 85.0
) -> str:
    """
    Synthesizes executive persona profile metrics: Seniority Depth Index and Concentration HHI.
    """
    res = bio_builder.synthesize_executive_persona_vector(experiences, skills, domain_authority_score)
    return json.dumps(res, indent=2)

@mcp.tool()
def calculate_career_trajectory_velocity(
    career_milestones: List[Dict[str, Any]]
) -> str:
    """
    Calculates career promotion cadence velocity and career acceleration gradient.
    """
    res = bio_builder.calculate_career_trajectory_velocity(career_milestones)
    return json.dumps(res, indent=2)

@mcp.tool()
def generate_credential_merkle_leaf_hash(
    candidate_id: str,
    credential_type: str,
    issuing_authority: str,
    issue_timestamp_utc: int
) -> str:
    """
    Generates cryptographic double-SHA256 leaf hash for verifiable credentials.
    """
    res = bio_builder.generate_credential_merkle_leaf_hash(candidate_id, credential_type, issuing_authority, issue_timestamp_utc)
    return json.dumps(res, indent=2)

def main():
    print("Testing Bio Builder:")
    print(generate_credential_merkle_leaf_hash("usr_991", "EXECUTIVE_MBA", "STANFORD_GSB", 1729000000))

if __name__ == "__main__":
    main()
