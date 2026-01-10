---
name: fee-inquiry
description: Load this skill for all conversations related to fee inquiries, transactions history and fee reversal requests
---

# Process
- if client is asking for reversal of a transaction, make sure to check if the transaction is of type "fee", other type of transactions cannot be reversed
- before proceeding with reversal provide a warning if the client already reversed fees in the past
- be concise, don't repeat the same information multiple times (ie no need to summarize information if it's already provided earlier)
