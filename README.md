# PortSwigger Web Security Academy Labs

**A practical, continuously evolving record of web application security research and learning.**

This repository documents my progress through [PortSwigger Web Security Academy](https://portswigger.net/web-security), focusing on understanding web vulnerabilities through hands-on experimentation, technical analysis, and structured documentation.

I am studying **Network Infrastructure and Cybersecurity at Jönköping University, Sweden**, and use these labs to strengthen my practical understanding of web application security and develop a systematic approach to identifying, analyzing, and understanding vulnerabilities.

**Connect with me:** [LinkedIn — Matin Sadeghi](https://www.linkedin.com/in/matin-sadeghi-863487321/)

## Objectives

- Develop practical web application security skills through hands-on labs.
- Understand the underlying mechanisms behind common web vulnerabilities.
- Document investigation methodologies, HTTP requests, relevant payloads, and evidence.
- Analyze root causes and identify appropriate remediation strategies.
- Track learning progress and identify areas requiring further practice.
- Build a technical portfolio demonstrating practical knowledge, reasoning, and continuous improvement.

## Topics

My learning focuses on web application vulnerabilities, including:

- SQL Injection
- Access Control
- Authentication
- Path Traversal
- Cross-Site Scripting (XSS)
- Server-Side Request Forgery (SSRF)
- Cross-Site Request Forgery (CSRF)
- File Upload Vulnerabilities
- Business Logic Vulnerabilities
- API Security
- Other web security topics as my studies progress

This list represents areas of study, not a claim that I have completed labs in each category.

## Methodology

The goal is to understand **why a vulnerability exists, how it can be identified, and how it can be prevented**—not simply to reproduce a successful payload.

Where relevant, lab reports will include:

- **Investigation:** Initial observations, relevant endpoints, parameters, and hypotheses.
- **Exploitation:** Testing methodology, sanitized HTTP requests, and relevant payloads.
- **Evidence:** Minimal evidence demonstrating the observed behavior.
- **Root Cause:** The underlying application weakness.
- **Remediation:** Practical recommendations for preventing the vulnerability.
- **Lessons Learned:** Technical insights, unsuccessful approaches, and concepts requiring further study.

Each report will distinguish between independently solved labs and solutions completed with hints or external assistance.

## Tools & Environment

Tools used throughout my practical work may include:

- **Kali Linux** — Security testing environment.
- **Burp Suite** — HTTP interception, request analysis, and manual testing.
- **sqlmap** — Automated SQL injection testing in authorized lab environments.
- **curl** — Command-line HTTP requests and reproducible testing.
- **Linux command-line tools** — Request analysis, text processing, and supporting tasks.

The tools used for each lab will be documented individually where relevant.

## Repository Structure

```text
portswigger-web-security-labs/
├── README.md
├── PROGRESS.md
├── METHODOLOGY.md
├── TOOLS.md
└── labs/
    ├── sql-injection/
    ├── access-control/
    ├── authentication/
    └── ...
```

Individual lab reports will be organized by vulnerability category. Additional documentation and evidence will be included when they contribute meaningfully to understanding the investigation.

The structure will evolve as the repository grows.

## Progress

This repository is a work in progress. New lab reports, technical notes, and lessons learned will be added continuously as I advance through the Academy.

The emphasis is on **technical understanding, reproducibility, and consistent improvement rather than the number of completed labs**.

## Scope & Ethics

All practical testing documented here is intended for PortSwigger Web Security Academy labs and other explicitly authorized environments.

This repository is an educational portfolio documenting my personal learning. It does not represent professional penetration-testing experience, and documenting a vulnerability technique does not imply that it has been tested against real-world systems.

PortSwigger's original learning materials remain available through the official Academy. This repository focuses on my own investigations, observations, and explanations.

## References

- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [PortSwigger Web Security Academy — All Topics](https://portswigger.net/web-security/all-topics)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)

---

*Continuously maintained as part of my development in cybersecurity and web application security.*