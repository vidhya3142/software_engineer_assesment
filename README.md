# Software Engineer Assessment - Solution

**Candidate:** Kalisetty Vidhya Bharathi  
**Email:** vidhyabharathi3142@gmail.com  

This repository contains my solution and exploration for the 4-layer engineering assessment.

## Assessment Overview

The platform provides a REST API that implements a progressive puzzle with four layers:

- **Layer 1**: Fetch the full dataset efficiently and prove byte-level integrity (`content_hash`)
- **Layer 2**: Decrypt the dataset using a key issued by the platform (`decrypted_hash`)
- **Layer 3**: Extract a hidden alphabetic string (`transcript`)
- **Layer 4**: Provide interesting analysis of the data (`analysis`)

## Repository Structure

```bash
├── src/
│   └── main.py                 # Main script for fetching and processing data
├── data/                       # Generated outputs (gitignored)
├── requirements.txt
├── .gitignore
└── README.md


Key Learnings & Tradeoffs

Pagination handling: Efficient memory usage with streaming-style accumulation
Error resilience: Graceful handling of rate limits and partial failures
Reproducibility: All outputs saved locally for verification
Security: API key handled carefully (not committed in production setup)

Challenges Faced

Understanding the exact decryption scheme for Layer 2
Identifying the correct endpoint for the decryption key
Handling different possible cipher modes and IV placement

Future Improvements (if time allows)

Add automated submission script
Implement retry logic with exponential backoff
Add comprehensive logging and debugging helpers
Containerize the solution (Docker)


Repository URL submitted (as per instructions):
https://github.com/vidhya3142/software_engineer_assesment.git

