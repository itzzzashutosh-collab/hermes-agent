5. Are there underserved regions with growing contractor activity?

## Core Frameworks
1. **Network Design Optimization (Bowersox et al.)** – Applies cost minimization and service maximization trade-offs in network configuration.
2. **Full Truckload Routing (FTL)** – Maximizes load efficiency and reduces per-unit transportation cost.
3. **Responsive Logistics Systems** – Enables rapid response to demand surges through pre-positioned inventory and flexible routing.

## Decision Algorithm
IF current FTL utilization < 85%
    THEN recommend consolidating shipments to achieve full truckloads
    AND identify 3-5 high-volume routes for dedicated FTL scheduling
ELSE IF average delivery lead time > 48 hours
    THEN recommend establishing a satellite depot in the highest-demand zone
    AND reroute 70% of shipments through the new depot
ELSE IF stockouts occur in >3 high-demand zones
    THEN recommend increasing safety stock by 25% in central depot
    AND implement dynamic routing based on real-time demand signals
ELSE IF freight costs exceed benchmark by >15%
    THEN recommend renegotiating contracts with top 3 carriers
    AND explore rail transport for bulk resin shipments

## Output Structure
- Recommended depot locations (with coordinates)
- Optimal FTL routing schedule (weekly)
- Depot capacity utilization report
- Cost savings projection (₹/month)
- Risk assessment matrix (supply chain disruptions, carrier reliability)

## Examples

### Scenario 1: Jaipur Contractor Cluster
Jaipur has seen 40% growth in construction projects. Current lead time: 72 hours. FTL utilization: 78%. Stockouts in 4 districts.

**Action Plan:**
- Establish satellite depot in Ajmer (hub for western Rajasthan)
- Route 60% of Jaipur shipments through Ajmer
- Implement daily FTL schedules from Ajmer to Jaipur
- Increase safety stock by 30% in Ajmer depot
- Projected savings: ₹1.8 lakh/month

### Scenario 2: Ahmedabad Bulk Orders
Ahmedabad receives 12 large orders/month (>500L each). Current FTL utilization: 68%. Partial loads cost 22% more.

**Action Plan:**
- Consolidate all Ahmedabad orders into 3 FTLs/week
- Schedule FTLs on Tuesdays, Thursdays, Saturdays
- Negotiate volume discount with carrier
- Projected savings: ₹2.4 lakh/month

## Failure Modes
- Over-depoting: Excessive fixed costs from too many satellite depots
- Under-utilization: FTLs running below 70% capacity
- Poor location selection: Depots placed in low-demand areas
- Ignoring seasonality: Peak demand periods not accounted for
- Carrier lock-in: No contingency plans for carrier failure

## Checklist
- [ ] Verified current depot locations and capacities
- [ ] Collected regional demand forecasts
- [ ] Confirmed transportation cost benchmarks
- [ ] Validated lead time data
- [ ] Identified high-volume routes
- [ ] Reviewed carrier contracts
- [ ] Checked warehouse lease terms
- [ ] Assessed fleet capacity
- [ ] Completed risk assessment
- [ ] Finalized output structure

---
name: donald-bowersox-logistics-network-engine
description: Enable Swatch Paints to design, optimize, and govern its logistics network using Donald Bowersox’s foundational principles of supply chain network design, focusing on depot placement, full truckload optimization, and responsive logistics systems for the Indian paint industry.
version: 1.0.0
author: Hermes, CEO, Swatch Paints
license: Proprietary
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [logistics, supply-chain, network-design, ftl, depots]
    category: distribution-supply-chain
    related_skills: [philip-kotler-scm-strategy-engine, ford-w-harris-eoq-engine, taiichi-ohno-production-planning-engine]
    config:
      required_env_vars: []
      setup_instructions: "Run with Hermes CEO context. No additional setup required."
    config_schema: {}
