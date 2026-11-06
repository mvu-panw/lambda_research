# Lambda identity security research (Nov 6, 2026)

Collected for `site/identity.html`. Sources: public DNS, HTTP headers, the Ashby job-board API (`https://api.ashbyhq.com/posting-api/job-board/lambda`), and the SafeBase trust portal (`trust.lambda.ai` -> `trust.lambda.com`).

## DNS and HTTP (observed Nov 6, 2026)

- `lambda.ai`, `lambda.com`, `lambdalabs.com`: MX -> Google (`smtp.google.com` / `aspmx.l.google.com`), SPF includes `_spf.google.com`.
- `lambda.ai` TXT verifications: openai, anthropic, apple, google-site, notion, stripe, reachdesk, speakeasy. SPF also includes HubSpot and Mailgun. `lambdalabs.com` SPF adds SendGrid and Greenhouse.
- `_dmarc.lambda.ai`: `p=quarantine`, rua to dmarc-reports.cloudflare.net.
- `cloud.lambda.ai/login` redirects to `cloud.lambda.com/login` (Cloudflare, Turnstile challenge). `trust.lambda.ai` redirects to `trust.lambda.com` (SafeBase).
- Okta `/.well-known/okta-organization`: `lambda.okta.com` exists (cell ok14, pipeline idx = Identity Engine, itpEnabled=true). `lambdal.okta.com` exists (cell ok5, pipeline v1 = Classic). A random nonexistent name returns HTML, not JSON. Ownership of either tenant is NOT verified.

## Trust portal control text (SafeBase page source)

> Authentication: Authentication to Lambda’s identity and access management platform requires the use of passwords with a minimum length of characters, complexity, and the use of multifactor authentication (6.5). Lambda utilizes the platform to authenticate to several applications, tools, and platforms that support business operations and client services. System administrator-level access privileges to Lambda’s identity and access management platform are restricted to only those individuals who require such access to perform their respective job functions (6.6).

> Access Management: Lambda has established an access management policy that governs the provisioning and management of system access (6.1).

- Least Privilege | full | Lambda subscribes to the principle of “least privilege”.
- Password Security | full | Lambda maintains a password security standard for all applications and systems.
- Mobile Device Management | na | Lambda’s mobile device management platforms: -configured to automatically encrypt all Mac, Windows, and Linux workstations -configured to automatically install antimalware software onto all Mac, Windows, and Linux workstations -configured to require the automatic install of updates onto all Mac, Windows, and Linux workstations -configured to automatically lock workstations after a modest period of inactivity -configured to require workstation authentication prior to usage
- IDS/IPS | full | IDS/IPS is implemented only for vendor's internal traffic. Customer traffic is excluded.
- Pentest Report | full | Cobalt conducted a pentest of the cloud.lambdalabs.com + network perimeter application and API to assess its risk posture and identify security issues that could negatively affect Lambda's data, systems, or reputation. The scope of the assessment covered cloud.lambdalabs.com + network perimeter and included credentials for various levels of privilege within the scope. A Cobalt pentest team of 3 conducted this engagement between May 11, 2026 and May 25, 2026.  The web application pentest was a manual assessment of the security of the application’s functionality, business logic, and vulnerabilities, such as those cataloged in the Open Web Application Security Project (OWASP) Top 10. The assessment also included a review of security controls and requirements listed in the OWASP Application Security Verification Standard (ASVS).

## Security job postings (Ashby), identity-relevant lines

### Security Engineer (2026-07-16, San Francisco Office (Fremont St))
https://jobs.ashbyhq.com/Lambda/e5453baf-d2ec-43d1-9d3b-8fb3d5cdc9d1

- Build and Tune Detections: Develop and refine detection content across our SIEM and EDR to catch threats targeting customer data, model weights, and infrastructure.
- Experience driving or providing significant evidence for compliance audits such as SOC 2, ISO 27001, PCI-DSS, HIPAA/HITECH, or FedRAMP.
- You've built or deployed critical security infrastructure such as SIEM, SOAR, EDR, IDS/IPS, or canary/honeypot systems.

### Senior Security Engineer - Detection & Response (2026-11-03, San Francisco Office (Fremont St))
https://jobs.ashbyhq.com/Lambda/ee553f81-7e7c-4646-8434-ec684e10a557

- Architect automated response capabilities and orchestration pipelines (SOAR) to programmatically isolate compromised assets and revoke compromised credentials
- Proven experience writing detection rules (SIEM, YARA, Sigma, Falco, or EDR queries) and managing detections through software development best practices
- Experience driving or providing significant evidence for compliance audits, such as SOC 2, ISO 27001, PCI-DSS, HIPAA/HITECH, or FedRAMP.

### Senior Security Engineer - Enterprise Security (2026-09-24, Bellevue Office)
https://jobs.ashbyhq.com/Lambda/8d2158d9-9785-4a2a-87ea-5690ff0cabe5

- As a Senior Security Engineer on Enterprise Security, you'll secure Lambda as a business with people who use computers: the identities, devices, SaaS, and AI tools our employees and contractors use every day.
- Near term, that means identity automation that keeps access matched to each person's role, secure access for contractors and personal devices, controls on where agents can send company data, and secure environments for running AI agents off laptops.
- Lambda's people rapidly adopt frontier AI tools and agents, and making that safe is an engineering problem rather than a policy memo.
- Make the safe way to use AI tools and agents the easy way, with approved tools, connectors, and agent environments.
- Make sure humans, agents, and integrations move sensitive data only along reviewed paths, following Lambda's data protection strategy.
- Decide what a person, device, contractor, or agent must prove before reaching company systems, then engineer the checks and access paths that enforce it.
- Keep every corporate device hardened, monitored, and patched, building on the MDM and EDR platforms IT runs.
- Hands-on depth in workforce identity: identity providers and SSO (e.g., Okta, Entra ID), federation and provisioning standards (SAML, OIDC, SCIM), MFA, and privileged access.
- Practical experience securing corporate SaaS, managed endpoints (MDM, EDR), and network access built on zero trust principles.
- Ships high-quality automation in Python, Go, or similar, including security work done with LLMs or agents that wasn't practical by hand.
- Practical understanding of how people use AI assistants and agents at work, and where they create data and access risk.
- Experience securing contractor or personal-device access without managing the device.
- Experience managing identity, SaaS, or endpoint configuration as code (e.g., Terraform).
- Experience supporting SOC 2, ISO 27001, or FedRAMP audits with evidence from corporate controls.
- Curiosity about how securing a workforce changes when much of its work is done by AI agents, and excitement to help work that out.

### Staff Security Architect (2026-10-08, Bellevue Office)
https://jobs.ashbyhq.com/Lambda/de01a9eb-184f-445e-a9f2-94849f860b7f

- Excitement about leveraging our direct access to state-of-the-art LLMs to revolutionize enterprise security—imagine AI-assisted access reviews, automated SaaS risk assessments, and intelligent policy generation.
- Experience building enterprise security and IAM programs at high-growth tech companies or cloud providers
- Familiarity with compliance frameworks (SOC 2, ISO 27001, FedRAMP, HIPAA) and audit preparation
- Experience implementing Infrastructure as Code (Terraform) for managing enterprise identity and SaaS configurations
- Experience driving or providing significant evidence for compliance audits, such as SOC 2, ISO 27001, PCI-DSS, HIPAA/HITECH, or FedRAMP.

### Senior Product Security Engineer (2026-11-04, San Francisco Office (Second St))
https://jobs.ashbyhq.com/Lambda/140ec386-5d50-4cfb-b24c-eeb2b0c08afc

- Reads application code and infrastructure as code (e.g., Terraform, Ansible, Kubernetes manifests) fluently enough to explain a vulnerability's root cause, not just a scanner's verdict.
- Experience supporting enterprise customer security reviews, or providing significant evidence for compliance audits such as SOC 2, ISO 27001, or FedRAMP.

