# CodeScan QA fixture

Synthetic scanner input. XML is well formed; invented custom fields and repeated permissions
may not be deployable to Salesforce. Candidate permission blocks are NOT verified findings.
Use the same Quality Profile and scanner build for baseline and comparison.

1. Extract and push this directory to a NEW isolated repository. Commit on main.
2. Scan main. Record scanner exit, actual findings per rule/file, SARIF size,
   scanner heap/GC, CE task state, CE heap and elapsed times.
3. Create a branch. Run `python3 qa_pr_change.py`, commit, and open a PR.
4. Run your own trusted CodeScan workflow with `scanChangedFilesOnly: false` and
   `codescan.pullRequest.filterIssuesByChangedLines=false`; never copy production secrets.
5. Confirm class deletion and Profile edits in PR; compare before/after findings.

Profile count and XML line counts are recorded in qa_manifest.csv. No target
runtime, heap ceiling or findings count is guaranteed without rule calibration.
The deep fixture has deliberately nonstandard children and tests parser rejection
or bounded failure, not Salesforce deployability or the customer's JS stack error.
