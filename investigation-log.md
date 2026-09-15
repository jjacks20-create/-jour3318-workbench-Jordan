# Active Investigation Log & Chain of Custody

> **Discipline of Verification:** This document records your active investigations, the evidence gathered, archival snapshots, and triangulation matrices.

---

## Active Investigations Index

| ID | Title / Target | Phase / Task | Status | Primary Verification Vector |
| :---: | :---: | :---: | :---: | :---: |
| `INV-01` | [Job Vetting: LinkedIn Forensics Lab](#inv-01-linkedin-job-vetting) | Performance Task 1 (Day 0) | `Completed` | Recruiter Forensics + SOS Registry + WHOIS |
| `INV-02` | [Health Misinformation: TikTok Seed Oil Claims](#inv-02-health-misinformation) | Performance Task 2 | `Pending` | PubMed Triangulation + Ad Network Tracking |
| `INV-03` | [Video Forensics: Protest Footage Verification](#inv-03-video-forensics) | Performance Task 3 | `Pending` | InVID Keyframes + Shadow/Satellite Mapping |
| `INV-04` | [Summative Capstone Investigation](#inv-04-capstone-investigation) | Performance Task 4 | `Pending` | Python Scraper + Google Pinpoint Document Index |

---

## Detailed Investigation Files

### INV-01: LinkedIn Job Posting Vetting
- **Investigation Date:** `2026-9-3`
- **Case Selected:** Case 1 Ashley R.
- **Target URL / Entity:** Ashley R. ,Recruiter at TD Bank | HR, Recruiting, Compliance
- **Archived Snapshot / Artifact:** Sandbox Screenshot

#### 1. Evidence & Chain of Custody
| Item Screenshot | Description photo looking into the meta data of pfp 
| :---: | :--- | :--- | :--- |
| `E-01` | Recruiter Profile / InMail Screenshot |evidence/Code_Generated_Image (13).jpeg
| `E-02` | Corporate Registry Filing / Search Screenshot | https://www.td.com/ca/en/business-banking/small-business/starting-your-business/business-registration
| `E-03` | Domain WHOIS / Infrastructure Lookup | evidence/Code_Generated_Image (4).jpeg

#### 2. Triangulation Matrix
| Vector | Tool / Source Used | Observations & Evidence | Confidence |
| :--- | :--- | :--- | :---: |
| **Vector 1: Recruiter Profile** | `evidence/Code_Generated_Image (12).jpeg , This image highlighted someone that has the same exact name and works for TD bank working a similar position , but the profile also has no profile picture and not many postings so this could be a completely different person. This is evidence that the person from the job posting may not be a real person.
 |Low| |Low|
| **Vector 2: Corporate Registry** | `https://opencorporates.com/companies/us_tx/0001840903, This image highlighted someone that has the same exact name and works for TD bank working a similar position , but the profile also has no profile picture and not many postings so this could be a completely different person. This is evidence that the person from the job posting may not be a real person.
` |Low| |Low|
| **Vector 3: Domain Age / MX** | `This domain was registered less than 2 weeks ago,The email domain attached to the job posting was only made two weeks ago, which highlights that it could be a job posting fresh on the market. Also when google searching (career@eiexecutive.ph) the email comes up as one associated with work related scams 
|Low| |Low|
| **Vector 4: Official Portal** | `https://td.wd3.myworkdayjobs.com/TD_Bank_Careers, This is the official job posting website link from the TD bank website , the job that is mentioned for TD bank through the listing has no posting to be seen on their official website. Highlighting how the company behind the posting is real, but the job itself may not be real !|Low| |Low|

#### 3. Editorial Verdict
- **Classification:** `PHISHING SCAM`
- **Information Disorder Taxonomy:** `Fabricated Content`
- **Confidence Level:** `[High]` (Triangulated across independent vectors)
- **Public Warning / Reporter Summary:** Even though this profile does a good job at putting on the illusion that the this is a legit job offer , but after taking a deep dive on the message sent by Ashley R. who is a Recruiter at TD Bank. The photo used for the profile came up with no matches on verification data bases, the email connected to the message is connected to known online scams, along with no record of a Ashley R. ever worked for TD Bank.

---

### INV-02: Health Misinformation
- **Investigation Date:** `YYYY-MM-DD`
- **Subject / Claim:** 

#### 1. Chain of Custody & Evidence Archival
| Item # | Description | Permanent Archive URL / Evidence File |
| :---: | :--- | :--- |
| `E-01` | Viral video snapshot | `https://archive.today/...` |

#### 2. Triangulation Matrix
| Vector | Source / Tool Used | Findings & Evidence | Confidence |
| :--- | :--- | :--- | :---: |
| **Vector 1 (Claim):** | Peer-Reviewed Clinical Trial | | |
| **Vector 2 (Incentive):** | Meta Ad Library / Affiliate Link | | |

#### 3. Investigative Findings & Conclusion
- **Taxonomy Category:** 
- **Summary:** 

---

### INV-03: Video Forensics
- **Investigation Date:** `YYYY-MM-DD`
- **Subject / Target Video:** 

#### 1. Chronolocation & Geolocation Triangulation
- **Coordinates Identified:** `Lat, Long` (e.g., `50.4501° N, 30.5234° E`)
- **Keyframe Evidence:** `evidence/inv03_keyframe_04.png`
- **SunCalc / Shadow Angle Check:** 
- **Satellite Cross-Reference:** (Google Earth / Sentinel Hub match details)

---

### INV-04: Capstone Investigation
- **Investigation Date:** `YYYY-MM-DD`
- **Hypothesis:** 
- **Dataset / Scraper Used:** `scripts/capstone_scraper.py`
- **Google Pinpoint Document Collection:** `[Link to collection]`
- **Triangulation & Findings Summary:** 
