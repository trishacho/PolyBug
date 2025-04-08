# PolyBug 🐛

We propose **PolyBug**, a new benchmark for evaluating Large Language Models (LLMs) on real-world debugging tasks across multiple programming languages.

We have curated 7–10 real bugs from open-source projects across a variety of bug categories—from off-by-one errors to null references—in languages such as **Python, Java, TypeScript, C/C++,** and more.

These bugs were collected using the GitHub API from ~70 repositories and each comes with:
- A **buggy code snippet**
- The **corrected version** from the real bug-fix commit
- A **manually written unit test** that captures the bug and validates the fix

> ⚠️ **Work in progress**: This repository currently contains the buggy/fixed code pairs and unit tests. We are actively expanding the benchmark and preparing LLM evaluation scripts.