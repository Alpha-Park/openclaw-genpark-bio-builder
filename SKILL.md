---
name: genpark-bio-builder
description: Dynamic, AI-driven personal linking hub and affiliate conversion page.
version: 1.0.0
---

# genpark-bio-builder

## MCP runtime requirements

The standard-library-only policy applies to direct `client.py` use. Running `mcp_server.py` requires Python 3.10+ and the official `mcp` SDK (`mcp>=1.0.0,<2`) from `requirements.txt`. Install it into your chosen environment from the repository checkout:

```bash
python -m pip install -r requirements.txt
```

Configure the MCP client with that environment's absolute Python executable path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; a GitHub URL is not a remote MCP endpoint.

## Overview
Unlike static "Link in Bio" platforms (e.g., Linktree), this skill creates a dynamic conversion interface. It helps creators generate a centralized hub where a conversational AI widget acts as a personal concierge. The assistant answers visitor questions and proactively recommends the creator's affiliate links or products based on the visitor's needs.

## Core Capabilities
- **Hub Generation**: Generate a mobile-optimized, highly aesthetic HTML/CSS page housing the creator's primary links.
- **Concierge Agent**: Deploy a specialized GenPark agent within the bio link page trained exclusively on the creator's affiliate deals.
- **Analytics Tracking**: Measure outbound click-through rates (CTR) and AI-driven conversion touches.

## Usage Guide
To build a bio page:
1. Ask the creator to list their top 5 affiliate links, products, or primary social channels.
2. Ask for a brief "knowledge base" defining what the creator represents and what each product solves.
3. Generate the Bio Hub HTML and instruct the user on how to embed the GenPark Assistant.
4. Configure the GenPark Assistant instructions to always guide relevant conversations toward the affiliate links.
