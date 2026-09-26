# Schema: Venue Profile

\`\`\`yaml
venue:
year:
status: verified_official | unverified_target_year | historical_reference
verified_date:
official_sources: []
template:
  required:
  source:
submission:
  anonymity:
  main_page_limit:
  references_count_toward_limit:
  appendix_policy:
  supplementary_policy:
  single_pdf_requirement:
  max_pdf_size:
camera_ready:
  main_page_limit:
  notes:
mandatory_elements: []
format_notes: []
refresh_triggers:
  - official target-year author guide appears
  - target-year template changes
  - submission policy update
notes:
\`\`\`

## Rules

- Hard constraints must come from official venue sources.
- Conference name without year is insufficient.
- A previous year's profile may guide provisional planning but cannot authorize final submission formatting.
- Preserve the source and verification date for every profile.
