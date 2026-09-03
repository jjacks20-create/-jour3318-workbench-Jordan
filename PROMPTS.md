# AI Prompt & Hallucination Audit Log

> **UbD Course Requirement:** In JOUR 3318, you are encouraged to use generative AI (such as the Course Gemini Gem, Google AI Studio, and LLMs) as an investigative teaching assistant. However, **you must maintain editorial oversight**. You are evaluated on your *process of inquiry*, meaning every AI interaction used in your investigations must be documented and critically evaluated below.

---

## AI Interaction Ledger

| Entry # | Date | Tool / Model | Investigation Task | Verdict (`ACCEPTED` / `MODIFIED` / `REJECTED`) | Link to Detail |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `001` | 2026-09-10 | Gemini 1.5 Pro | Job Vetting: Company registration lookup | `[MODIFIED]` | [Jump to Entry #001](#entry-001) |
| `002` | 2026-09-18 | Course Gemini Gem | Video Forensics: Keyframe shadow angle analysis | `[ACCEPTED]` | [Jump to Entry #002](#entry-002) |
| `003` | 2026-10-02 | ChatGPT / Claude | Health Debunk: Summarizing PubMed study | `[REJECTED - HALLUCINATION]` | [Jump to Entry #003](#entry-003) |

---

## Detailed Log Entries

### Entry #001
- **Date & Time:** `2026-9-3 1:20`
- **Tool / Model:** Gemini 
- **Task Context:** Converting the screenshots of my evidence to formats github will accept 

#### 1. Input Prompt
```text
Convert these photos to jpegs Github will let me upload
```

#### 2. Raw Model Response
```text
The photos in my evidence folder 
```

#### 3. Critical Evaluation & Hallucination Check
- **Triangulation / Verification Method:** (e.g., Cross-checked company address against the Texas Secretary of State corporate registry.)
- **Errors / Hallucinations Detected:** (e.g., The model claimed the company was incorporated in 2012, but state records show it was created in 2024.)
- **Editorial Decision & Rationale:** 
  - [ ] **Accepted:** Factually accurate and verified.
---

### Entry #002
- **Date & Time:** `2026-9-3 1:25`
- **Tool / Model:** Gemini search feature
- **Task Context:** none

#### 1. Input Prompt
```text
Ashley R td bank
```

#### 2. Raw Model Response
```text
There is no single public figure or universally known entity named "Ashley R" associated with TD Bank, as several professionals with the first name Ashley and last initial R work across various roles at the company, including talent acquisition and regional positions
```

#### 3. Critical Evaluation & Hallucination Check
- **Triangulation / Verification Method:** NA
- **Errors / Hallucinations Detected:** NA
- **Editorial Decision & Rationale:** ACCEPTED 

---

### Entry #003
- **Date & Time:** `YYYY-MM-DD HH:MM`
- **Tool / Model:** 
- **Task Context:** 

#### 1. Input Prompt
```text
[Your prompt]
```

#### 2. Raw Model Response
```text
[Raw output]
```

#### 3. Critical Evaluation & Hallucination Check
- **Triangulation / Verification Method:** 
- **Errors / Hallucinations Detected:** 
- **Editorial Decision & Rationale:** `[ACCEPTED / MODIFIED / REJECTED]`
